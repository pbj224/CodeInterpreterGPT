from subprocess import Popen, PIPE, TimeoutExpired
import os, logging, time, hashlib

class CommandShellExecutor:
    def __init__(self, manager_scope):
        self.scope = manager_scope
        self.prev_env_hash = self.hash_env()
        self.command_history = []
        logging.basicConfig(filename='cmd_logs.log', level=logging.INFO, format='%(asctime)s - %(message)s')
        
    def hash_env(self):
        return hashlib.md5(str(os.environ).encode()).hexdigest()

    def execute_cmd_shell(self, cmd_str, timeout=60):
        try:
            start = time.time()
            proc = Popen(cmd_str, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, env=os.environ)
            out, errs = proc.communicate(timeout=timeout)
            ret_code, exec_time = proc.returncode, time.time() - start
            curr_env_hash = self.hash_env()
            
            out, errs = out.decode().strip()[:3000], errs.decode().strip()
            
            # Logging and updating command history
            logging.info(f"Cmd: {cmd_str}, Time: {exec_time:.2f}s, Return Code: {ret_code}, Output: {out}, Errors: {errs}")
            self.command_history.append({'cmd': cmd_str, 'output': out, 'errors': errs, 'return_code': ret_code, 'exec_time': exec_time})
            
            # Updating scope to maintain statefulness
            self.scope.update({'output': out, 'errors': errs, 'return_code': ret_code, 'exec_time': exec_time, 'env_changed': self.prev_env_hash != curr_env_hash})
            self.prev_env_hash = curr_env_hash
            
            return f"Output:\n{out}\nErrors:\n{errs}\nReturn Code: {ret_code}\nExec Time: {exec_time:.2f}s\nEnv Changed: {self.prev_env_hash != curr_env_hash}"
        except TimeoutExpired:
            proc.kill()
            logging.error(f"Cmd: {cmd_str} timed out")
            return "Command timed out"
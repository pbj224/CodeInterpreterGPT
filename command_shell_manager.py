from command_shell_executor import CommandShellExecutor

class CommandShellManager:
    def __init__(self, initial_scope):
        self.scope = initial_scope
        self.command_shell = CommandShellExecutor(self.scope)

    def get_scope(self):
        return self.scope

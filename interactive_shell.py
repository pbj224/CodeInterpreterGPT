from IPython import InteractiveShell
import os

class InteractiveShellManager:
    def __init__(self, conda_env_path):
        self.shell = InteractiveShell()
        self.scope = {}
        self.conda_env_path = conda_env_path

    def activate_conda_env(self):
        os.environ['CONDA_PREFIX'] = self.conda_env_path

    def get_scope(self):
        return self.scope
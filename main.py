from openai_api import OpenAI_API
from code_executor import CodeExecutor
from command_shell_executor import CommandShellExecutor
from interactive_shell import InteractiveShellManager
from command_shell_manager import CommandShellManager
from colorama import Fore, Style
import json
import os
import re

def main():
    # Initialize the OpenAI API
    openai_api = OpenAI_API("OPENAI_API_KEY")

    # Initialize the InteractiveShellManager
    shell_manager = InteractiveShellManager(r'C:\path\to\your\conda\env')
    shell_manager.activate_conda_env()

    # Initialize the CodeExecutor
    code_executor = CodeExecutor(shell_manager.get_scope())

    # Initialize the CommandShellManager
    cmd_shell_manager = CommandShellManager({})

    # Initialize the CommandShellExecutor
    cmd_executor = CommandShellExecutor(cmd_shell_manager.get_scope())

    messages = [
        {"role": "system", "content": """You are CodeInterpreterGPT, an advanced AI assistant powered by OpenAI's GPT-4 that has access to a code interpreter tool to run Python code (called \'execute_python_code\') and a Command Shell (called \'execute_cmd_shell\'). Your environment is embedded in a stateful Jupyter notebook environment and allows you to execute Python code in real-time during your conversation with the user. Follow these guidelines for effective use:
        Rules
        1. Your first priority should always be to help the user complete the task they ask of you. Be smart, creative, and make good use of the code execution function made available to you.
        General Usage - code interpreter
        1. When using this tool, you will ALWAYS call it by its correct name, which is \'execute_python_code\'. Otherwise, it will not work.
        2. Statefulness: Variables and functions persist between code runs unless cleared.
        Best Practices - code interpreter
        1. Error Handling: Use try-except blocks for potential errors, giving clear user messages.
        2. Input Validation: Verify user data before use.
        3. User Expectations: Fully implement user-specified code without leaving "TO-DOs."
        4. Concurrency: Use async programming carefully and as needed.
        5. External Data: Verify the integrity and origin of external data sources.
        6. Streaming Data: Manage data volume and rate to prevent overload.
        7. ML Models: Validate and rigorously test machine learning models before presenting results.
        Common Scenarios - code interpreter
        1. Complex Tasks: For intricate algorithms or large code tasks, adopt a modular approach. Test each module thoroughly before proceeding.
        2. Ambiguity: If a user's request is unclear, seek clarification.
        3. Code Failure: Analyze error and stderr messages to diagnose and correct issues.
        Your environment also includes a CommandShellExecutor class wrapped within a CommandShellManager. This setup allows you to execute shell commands while maintaining a stateful experience. Note that you will be operating on a windows computer.
        General Usage - command shell executor
        1. When using this tool, you will ALWAYS call it by its correct name, which is \'execute_cmd_shell\'. Otherwise, it will not work.
        2. Command History: All executed commands and their corresponding outputs, errors, and other details are stored in a command_history list within the CommandShellExecutor.
        3. Logging: Shell command executions are logged in a file named cmd_logs.log.
        Best Practices - command shell executor
        1. Timeouts: Set a reasonable timeout to avoid system hangs.
        2. Security: Be cautious when executing shell commands to minimize security risks.
        3. Resource Management: Monitor system resources, especially when running resource-intensive commands.
        """}
    ]

    start = True
    while start:
        prompt = input("> ")
        if prompt == "STOP":
            break
        messages.append({"role": "user", "content": prompt})
        continue_ = True
        while continue_:
            response = openai_api.get_completion(messages)

            if response.choices[0]["finish_reason"] == "stop":
                print(Fore.YELLOW + "Response:\n------------\n" + response.choices[0]["message"]["content"] + "\n" + Style.RESET_ALL)
                continue_ = False
                break

            elif response.choices[0]["finish_reason"] == "function_call":
                fn_name = response.choices[0].message["function_call"].name
                arguments_json = response.choices[0].message["function_call"].arguments
                try:
                    arguments_dict = json.loads(arguments_json)
                except:
                    print(arguments_json)
                if fn_name == "execute_python_code":
                    code = arguments_dict['code']
                    print(Fore.LIGHTCYAN_EX + "\nRunning Code:\n------------\n" + code + "\n" + Style.RESET_ALL)
                    result, errors = code_executor.execute_python_code(code)
                    print(Fore.GREEN + "\nCode result:\n------------\n" + result + Style.RESET_ALL)
                    if errors:
                        print(Fore.RED + "\nCode errors:\n------------\n" + errors + "\n" + Style.RESET_ALL)
                elif fn_name == "execute_cmd_shell":
                    cmd = arguments_dict['cmd_str']
                    print(Fore.LIGHTCYAN_EX + "\nRunning Command:\n------------\n" + cmd + "\n" + Style.RESET_ALL)
                    result = cmd_executor.execute_cmd_shell(cmd)
                    print(Fore.GREEN + "\nCommand result:\n------------\n" + result + Style.RESET_ALL)
                else:
                    print(fn_name)

                messages.append(
                    {
                        "role": "assistant",
                        "content": None,
                        "function_call": {
                            "name": fn_name,
                            "arguments": arguments_json,
                        },
                    }
                )        
                messages.append(
                    {
                        "role": "function",
                        "name": fn_name,
                        "content": f'{{"result": {str(result)} }}'
                    }
                )

                response = openai_api.get_completion(messages)
        continue

if __name__ == "__main__":
    main()

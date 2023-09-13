from openai_api import OpenAI_API
from code_executor import CodeExecutor
from interactive_shell import InteractiveShellManager
from colorama import Fore, Style
import json

def main():
    # Initialize the OpenAI API
    openai_api = OpenAI_API("OPENAI_API_KEY")

    # Initialize the InteractiveShellManager
    shell_manager = InteractiveShellManager(r'C:\your\anaconda\env\path\here')
    shell_manager.activate_conda_env()

    # Initialize the CodeExecutor
    code_executor = CodeExecutor(shell_manager.get_scope())

    # Your main code here...
    messages = [
        {"role": "system", "content": "You are a helpful, GPT-4 powered python code generating chatbot. You will be given python coding tasks, such as data analysis. When outputting Python code to a string for execution in a jupyter notebook like sandbox, please follow these guidelines: you can ensure the code is being passed correctly by following these steps: 1. Escape special characters: In the string of Python code, escape special characters like backslashes (\) by using quadruple backslashes (\\\\\\\\). This is especially important for file paths. 2. Use raw strings for file paths: When a file path is part of the Python code, prefix the string with an r to treat backslashes as literal characters. For example, r'C:\\\\\\\\Users\\\\\\\\PeterJordan\\\\\\\\Downloads\\\\\\\\Product_Iter2.csv'. 3. Properly close all opened brackets, parentheses, and quotes: Every opened bracket, parenthesis, or quote in the code must have a corresponding closing character. 4. Follow Python's indentation rules: Python uses indentation to determine the grouping of statements. Make sure the generated code follows these rules. 5. Avoid using Python keywords as variable names: Python keywords have special meaning and should not be used as variable names. NOTE: Use error messages to trouble shoot. Do not wait for the user to ask you to do so. When trouble shooting, make sure to always examine the output and errors closely to understand what you may be doing wrong"}
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
                print("Regular Response: " + response.choices[0]["message"]["content"] + "\n")
                continue_ = False
                break

            elif response.choices[0]["finish_reason"] == "function_call":
                fn_name = response.choices[0].message["function_call"].name

                arguments_json = response.choices[0].message["function_call"].arguments
                arguments_dict = json.loads(arguments_json)
                code = arguments_dict['code']
                print(Fore.LIGHTCYAN_EX + "\nRunning Code:\n------------\n" + code + "\n" + Style.RESET_ALL)

                result, errors = code_executor.execute_python_code(code)

                print(Fore.GREEN + "\nCode result:\n------------\n" + result + Style.RESET_ALL)
                if errors:
                    print(Fore.RED + "\nCode errors:\n------------\n" + errors + "\n" + Style.RESET_ALL)

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
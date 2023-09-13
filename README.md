# CodeInterpreterGPT

CodeInterpreterGPT is a comprehensive project that leverages the power of OpenAI's API and Anaconda Powershell Prompt to reverse-engineer ChatGPT's Advanced Data Analysis, formerly known as Code Interpreter. This project was primarily a hobby project.

## Features

* **Code interpretation and execution**: Using OpenAI's API, CodeInterpreterGPT can interpret and execute code snippets in a Jupyter Notebook like fashion just like ChatGPT's Advanced Data Analysis.
* **Integration with Anaconda Powershell Prompt**: self explanatory
* **Advanced data analysis**: The project utilizes the GPT-4 model for advanced data analysis.

## Key Files

* **main.py**: Acts as the main entry point of the application and is responsible for initializing the CodeExecutor class and starting the application.
* **code_executor.py**: Houses the CodeExecutor class, which is primarily responsible for executing the code snippets.
* **openai_api.py**: Contains the functions necessary for interacting with the OpenAI API.
* **interactive_shell.py**: Sets up an interactive shell for executing commands.
* **app.py**: Contains the main application logic, including the routes for the web server.

## Usage

To use CodeInterpreterGPT, ensure Python is installed on your machine. Then, clone the repository and install the necessary dependencies. Once the setup is complete, run the `main.py` file to start the application.

> **Note**: An OpenAI API key is required to use this application. You can obtain this key from the OpenAI website.

## Dependencies

* OpenAI API
* Anaconda Powershell Prompt
* Python

## Limitations

The current version of CodeInterpreterGPT is a proof of concept and has some limitations. It can only interpret and execute simple code snippets. Complex code snippets or those that require additional dependencies might not work correctly.

## Future Work

Future versions of CodeInterpreterGPT will aim to enhance the code execution capabilities, include streaming outputs like ChatGPT, and im not sure what else. Additional features such as code debugging and performance profiling are also planned.

## Contributing

Contributions to CodeInterpreterGPT are always welcome. Feel free to submit a pull request or open an issue on the GitHub repository.

## License

CodeInterpreterGPT is open-source software, licensed under the MIT license.

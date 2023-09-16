# CodeInterpreterGPT - Python Code Interpreter

CodeInterpreterGPT is a project that utilizes the GPT-4 model provided by OpenAI and the PowerShell Prompt of Anaconda to create a system that can interpret and execute Python code in a manner similar to the Advanced Data Analysis feature of ChatGPT. This project aims to provide a highly interactive and useful tool for Python programmers, data scientists, and machine learning enthusiasts.

The project is structured to use OpenAI's API to interpret and execute Python code snippets in an environment that resembles a Jupyter Notebook. This environment is facilitated by the integration of Anaconda PowerShell Prompt, which provides a robust and versatile command-line interface for Python code execution. Utilizing the capabilities of the GPT-4 model, the project can conduct data analysis tasks, making it a useful tool for data exploration and comprehension.

## Table of Contents

- [Getting Started](#getting-started)
- [Core Features](#core-features)
- [Primary Components](#primary-components)
- [Installation](#installation)
- [Usage](#usage)
- [Required Dependencies](#required-dependencies)
- [Known Limitations](#known-limitations)
- [Future Developments](#future-developments)
- [Contribution Guidelines](#contribution-guidelines)
- [License Information](#license-information)

## Getting Started

To begin with CodeInterpreterGPT, you need to have Python and Anaconda installed on your system. Once you have these prerequisites, clone the repository and install the necessary dependencies. After setting up the environment, you can run the `main.py` file to start the application.

## Core Features

### Code Interpretation and Execution

CodeInterpreterGPT uses OpenAI's API to interpret and execute Python code snippets within a Jupyter Notebook-like environment.

### Anaconda PowerShell Prompt Integration

CodeInterpreterGPT integrates seamlessly with Anaconda PowerShell Prompt, offering a robust environment for executing Python code.

### Data Analysis

The project leverages the power of the GPT-4 model for data analysis tasks.

## Primary Components

- `main.py`: The main entry point of the application, responsible for initializing the `CodeExecutor` class and starting the execution.
- `code_executor.py`: This file houses the `CodeExecutor` class, which takes care of executing Python code snippets.
- `openai_api.py`: This module contains the necessary functions for interacting with the OpenAI API.
- `interactive_shell.py`: This script creates an interactive shell for executing commands.

## Installation

Follow these steps to install and set up CodeInterpreterGPT:

1. Ensure that Python and Anaconda are installed on your system.
2. Clone the CodeInterpreterGPT repository to your local machine.
3. Navigate to the cloned repository and install the required dependencies using the `requirements.txt` file.
4. Run the `main.py` script to start the application.

## Usage

To use CodeInterpreterGPT, follow these steps:

1. Open the Anaconda PowerShell prompt and navigate to the directory containing the `main.py` file.
2. Run `python main.py` to launch the application.
3. You will be prompted to enter Python code snippets for interpretation and execution.

**Note:** You will need an OpenAI API key to use the application, which you can obtain from the OpenAI website.

## Required Dependencies

- OpenAI API
- Anaconda PowerShell Prompt
- Python

## Known Limitations

CodeInterpreterGPT is currently in the proof-of-concept stage. It can interpret and execute simple Python code snippets effectively. However, more complex code or code requiring additional dependencies may not function as expected.

## Future Developments

Future versions of CodeInterpreterGPT will concentrate on enhancing its code execution capabilities, potentially introducing features like streaming outputs similar to ChatGPT. Other possible improvements include code debugging, performance profiling, and code optimization.

## Contribution Guidelines

Contributions to CodeInterpreterGPT are welcomed. Feel free to submit pull requests or open issues on the GitHub repository if you have suggestions, improvements, or fixes.

## License Information

CodeInterpreterGPT is open-source software released under the MIT license. For further details, please refer to the `LICENSE` file in the repository.

import openai
import json

class OpenAI_API:
    def __init__(self, api_key):
        openai.api_key = api_key

    def get_completion(self, messages):
        response = openai.ChatCompletion.create(
            model="gpt-4-0613",
            messages=messages,
            functions=[
                {
                    "name": "execute_python_code",
                    "description": "Execute python code in a stateful conda virtual jupyter like environment",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "code": {
                                "type": "string",
                                "description": "string of python code you want to execute",
                            },
                        },
                        "required": ["code"],
                    },
                    "name": "execute_cmd_shell",
                    "description": "Execute shell commands while maintaining a stateful experience",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "cmd_str": {
                                "type": "string",
                                "description": "string containing a shell command you want to execute",
                            },
                        },
                        "required": ["cmd_str"],
                    },
                }
            ],
            temperature=0,
        )
        return response

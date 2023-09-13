import io
import sys
import ast
import pandas as pd

class CodeExecutor:
    def __init__(self, scope):
        self.scope = scope

    def execute_python_code(self, code):
        try:
            # Capture stdout and stderr
            old_stdout, old_stderr = sys.stdout, sys.stderr
            sys.stdout, sys.stderr = io.StringIO(), io.StringIO()

            # Execute the code
            errors = ""
            last_expr = None
            try:
                block = ast.parse(code, mode='exec')

                # If the last statement is an expression, evaluate it separately
                if isinstance(block.body[-1], ast.Expr):
                    last = ast.Expression(block.body.pop().value)
                    exec(compile(block, '<string>', mode='exec'), self.scope)
                    last_expr = eval(compile(last, '<string>', mode='eval'), self.scope)
                else:
                    exec(code, self.scope)
            except Exception as e:
                errors += str(e)

            # Get the output
            output = sys.stdout.getvalue().strip()
            errors += sys.stderr.getvalue().strip()

            # Print the value of each variable
            output_dict = {}
            for var_name, var_value in self.scope.items():
                if not var_name.startswith("__"):
                    if isinstance(var_value, pd.DataFrame):
                        output_dict[var_name] = f"\n{var_name} (head):\n{var_value.head()}\n"
                    else:
                        output_dict[var_name] = f"\n{var_name}:\n{var_value}\n"

            # Store the output in the scope dictionary
            self.scope['output'] = output_dict

            # Add the last expression to the output
            if last_expr is not None:
                output += '\n' + str(last_expr)

            # Return only the output of the most recent execution
            return_str = "Output:\n" + output[:3000] + ("..." if len(output) > 3000 else "") + "\nErrors:\n" + errors
            return return_str, errors
        finally:
            # Reset stdout and stderr
            sys.stdout, sys.stderr = old_stdout, old_stderr
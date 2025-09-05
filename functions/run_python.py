import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_dir,
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
	name = "run_python_file",
	description = 'run a python file specified by the relative file_path within the working directory. If any argument is provided make sure to run the file with those',
	parameters = types.Schema(
		type=types.Type.OBJECT, 
		properties = {
			'file_path': types.Schema(
				type = types.Type.STRING, 
				description = 'The path of the file you need to run relative to the working directory',
				),
			'args': types.Schema(
				type = types.Type.STRING,
				description = 'Specifies the additional arguments to run the function with. Can be empty too. These will be later added automatically to "commands" variable after the interpreter and the file path',
				),
			'commands': types.Schema(
				type = types.Type.ARRAY,
				description = """ At the index zero you'll find the interpreter to run the file with, on index one you can find the absolute path of the file to run. if you find anything in this list after, those are the additional argument to run the file with""",
				),
		},
	),
)

import os
from google import genai
from google.genai import types

def get_files_info(working_directory, directory="."):
	full_path = os.path.join(working_directory, directory)
	abs_working_dir_path = os.path.abspath(working_directory)
	abs_attempt_path = os.path.abspath(full_path)
	if abs_attempt_path.startswith(abs_working_dir_path) == False:
		error = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
		return error
	if os.path.isdir(abs_attempt_path) == False:
		return f'Error: "{directory}" is not a directory'
	try:
		content = [f for f in os.listdir(abs_attempt_path)]
	except Exception as e:
		return f'Error: Issues with os.listdir. {e}'
	lst = []
	for file in content:
		try:
			name = file
			file_path = os.path.join(abs_attempt_path, name)
			size = os.path.getsize(file_path)
			is_dir = os.path.isdir(file_path)
			lst.append(f'- {name}: file_size={size} bytes, is_dir={is_dir}\n')
		except Exception as e:
			return f'Error: failed to process file. {e}'
	return "\n".join(lst)

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

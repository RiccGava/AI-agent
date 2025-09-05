import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'

schema_get_file_content = types.FunctionDeclaration(
	name = "get_files_info", 
	description = "Get the content of a file from a specified path within the working directory",
	parameters = types.Schema(
		type = types.Type.OBJECT,
		properties = {
			'file_path': types.Schema(
				type = types.Type.STRING,
				description = 'The relative file path of the file you need to get the content of relative to working directory',
			),
		},
	),
)

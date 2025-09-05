import os
from google.genai import types

def write_file(working_directory, file_path, content):
	try:
		abs_wd = os.path.abspath(working_directory)
		abs_f = os.path.abspath(os.path.join(working_directory,file_path))
	except Exception as e:
		return f'Error: error during path conversion'
	if (abs_f.startswith(abs_wd) == False):
		return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
	try:
		if os.path.exists(os.path.dirname(abs_f)) == False:
			os.makedirs(os.path.dirname(abs_f))
		with open(abs_f, 'w') as f:
			f.write(content)
	except Exception as e:
		return f'Error: "{e}"'
	return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
	name = 'write_file',
	description = 'Write the content of an input in the specified file path relative to a working directory.',
	parameters = types.Schema(
		type = types.Type.OBJECT,
		properties = {
			'content': types.Schema(
				type = types.Type.STRING,
				description = 'The string content needed to be written in the specified file',
				),
			'file_path': types.Schema(
				type = types.Type.STRING,
				description = """The relative path of the file that needs to be modified. If the path doesn't exists, the function will create it""",
				),
		},
	),
)

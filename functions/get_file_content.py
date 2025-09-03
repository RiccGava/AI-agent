import os

def get_file_content(working_directory, file_path):
	try:
		abs_wd = os.path.abspath(working_directory)
		abs_f = os.path.abspath(os.path.join(working_directory,file_path))
	except Exception as e:
		return f'Error: error during path conversion'
	if (abs_f.startswith(abs_wd) == False):
		return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
	if os.path.isfile(abs_f) == False:
		return f'Error: File not found or is not a regular file: "{file_path}"'
	

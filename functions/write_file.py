import os

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
	

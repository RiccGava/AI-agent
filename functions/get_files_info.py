import os

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
	for file in content:
		try:
			name = file
			file_path = os.path.join(abs_attempt_path, name)
			size = os.path.getsize(file_path)
			is_dir = os.path.isdir(file_path)
			yield(f'- {name}: file_size={size} bytes, is_dir={is_dir}')
		except Exception as e:
			return f'Error: failed to process file. {e}'
			

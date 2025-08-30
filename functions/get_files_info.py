import os

def get_files_info(working_directory, directory="."):
	full_path = us.path.join(working_directory, directory)
	abs_working_dir_path = os.path.abspath(working_directory)
	abs_attempt_path = os.path.abspath(full_path)
	if abs_attempt_path.startswith(abs_working_dir_path) == False:
		error = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
		return error
	if os.path.isdir(abs_attempt_path) == False:
		return f'Error: "{directory}" is not a directory'
	content = [f for f in os.listdir(abs_path_attempt)]
	for file in content:
		file_path = os.path.join(abs_attempt_path, name)
		name = file
		size = os.path.getsize(file_path)
		is_dir = os.path.isdir(file_path)
		print(f'- {name}: file_size={size} bytes, is_dir={is_dir}')
		

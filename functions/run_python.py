import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
	try:
		abs_wd = os.path.abspath(working_directory)
		abs_f = os.path.abspath(os.path.join(working_directory, file_path))
	except Exception as e:
		return f'Error during path conversion'
	if (abs_f.startswith(abs_wd) == False):
		return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
	if os.path.exists(abs_f) == False:
		return f'Error: File "{file_path}" not found.'
	if file_path.endswith('.py') == False:
		return f'Error: "{file_path}" is not a Python file.'
	try:
		process_obj = subprocess.run(f'python {abs_f} {args}', capture_output = True, timeout = 30, cwd = abs_wd, check = False, text = True)
		stdout = process_obj.stdout
		stderr = process_obj.stderr
		rs = f'STDOUT: {stdout}\nSTDERR: {stderr}\n'
		if (process_obj.returncode != 0):
			rs += f'Process exited with code "{process_obj.returncode}"'
		if not stdout or not stderr:
			return f'No output produced.'
	except Exception as e:
		return f"Error: executing Python file: {e}"
	return rs

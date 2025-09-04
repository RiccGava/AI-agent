import os
from functions.config import *

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
	try:
		with open(abs_f, 'r') as f:
			f_string = f.read(MAX_CHAR)
			if f.read(1)!="":
				f_string += f'[...File "{file_path}" truncated at 10000 characters]'
	except Exception as e:
		return f'Error: Could not read file "{e}"'
	return f_string
		

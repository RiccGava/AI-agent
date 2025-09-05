from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_file import schema_write_file


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
	schema_get_file_content,
	schema_run_python_file,
	schema_write_file,
    ]
)

def call_function(function_call_part, verbose = False):
	if not verbose:
		print(f"Calling function: {function_call_part.name}({function_call_part.args})")
	else:
		print(f" - Calling function: {function_call_part.name}")
	working_directory = './calculator'
	function_map = {
		"write_file": write_file,
		'run_python_file': run_python_file,
		'get_files_info': get_files_info,
		'get_file_content': get_file_content,
	}
	function_call_part.args.working_directory = working_directory
	function_to_call = function_map[function_call_part.name]
	result = function_to_call(**function_call_part.args)
	

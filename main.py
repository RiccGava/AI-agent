import sys
import os
from google import genai
from dotenv import load_dotenv
from google.genai import types
import argparse
from functions.get_files_info import schema_get_files_info

available_functions = types.Tool(
		function_declarations=[
		schema_get_files_info,
		]
		)
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

model_name = "gemini-2.0-flash-001"

def main():
	load_dotenv()
	parser = argparse.ArgumentParser()

	parser.add_argument("-v", "--verbose", action='store_true')
	parser.add_argument('prompt', nargs='+', help='User prompt')
	args = parser.parse_args()
	if not args.prompt:
		print("AI Code Assistant")
		print('\nUsage: python main.py "your prompt here"')
		print('Example: python main.py "How do I build a calculator app?"')
	sys.exit(1)

	api_key = os.environ.get("GEMINI_API_KEY")
	client = genai.Client(api_key=api_key)

	user_prompt = " ".join(args.prompt)
	messages = [
		types.Content(role="user", parts=[types.Part(text=user_prompt)]),
	]

	generate_content(client, messages, user_prompt, args.verbose)


def generate_content(client, messages, user_prompt, verbose):
	response = client.models.generate_content(
		model=model_name,
		contents=messages,
		config = types.GenerateContentConfig(tools = [available_functions], system_instruction = system_prompt),
				)
	if verbose:
		print('User prompt: ' + user_prompt)
		print("Prompt tokens:", response.usage_metadata.prompt_token_count)
		print("Response tokens:", response.usage_metadata.candidates_token_count)
	print("Response:")
	print(response.text)
	if(response.function_call != None):
		print(f"Calling function: {response.function_call.name}({response.function_call.args})")


if __name__ == "__main__":
	main()


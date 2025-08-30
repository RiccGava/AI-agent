import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import argparse

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
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    if verbose:
        print('User prompt: ' + user_prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()


import requests
import json
import openai
import os


def call_gpt_api(prompt_text):
    api_key = os.getenv("OPENAI_API_KEY")

    openai.api_key = api_key

    print("Calling Chat GPT API with the entered python code query")
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt_text,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print("The call to the GPT API was successful")
    except Exception as e:
        print(f"An exception occurred while calling Chat GPT: {e}")
        raise e

    return response.choices[0].text


def create_python_for_gpt_response(file_name, text_for_file):
    print("Creating a new .py file based on the response from the GPT response")

    try:
        # create a new .py file
        with open(file_name, 'w') as f:
            f.write(text_for_file)
            # Close the file
            f.close()
            print(f"The file {file_name} was created successfully")
    except Exception as e:
        print(f"There was an exception raised when trying to save the new file named {file_name}: {e}")
        raise e


def append_python_for_gtp_response(existing_file_name, text_for_file):
    # First check that the file exists
    if not os.path.isfile(existing_file_name):
        print(f"The existing file entered {existing_file_name} does not exist")
        raise FileNotFoundError(f'The file "{existing_file_name}" does not exist.')

    # Open the file in append mode
    with open(existing_file_name, 'a') as f:
        # Write the new python text to the end of the file
        f.write(text_for_file)

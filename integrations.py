import openai
import os


def call_gpt_api(prompt_text):
    """Calls the GPT API using the prompt text passed in.

        Args:
            prompt_text: The prompt text to use when calling the API.
    """
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


def create_python_file(file_name, python_code):
    """Creates a python file using the code/text passed in

            Args:
                file_name: The file name to create with the python code.
                python_code: The text (python code) to use in the file.
        """
    print("Creating a new .py file based on the response from the GPT response")
    try:
        # create a new .py file
        with open(file_name, 'w') as f:
            f.write(python_code)
            # Close the file
            f.close()
            print(f"The file {file_name} was created successfully")
    except Exception as e:
        print(f"There was an exception raised when trying to save the new file named {file_name}: {e}")
        raise e


def append_python_file(existing_file_name, python_code):
    """Appends python code to an existing file

        Args:
            existing_file_name: The existing file name to append the python code to.
            python_code: The text (python code) to append to the file.
    """
    # First check that the file exists
    if not os.path.isfile(existing_file_name):
        print(f"The existing file entered {existing_file_name} does not exist")
        raise FileNotFoundError(f'The file "{existing_file_name}" does not exist.')

    # Open the file in append mode
    with open(existing_file_name, 'a') as f:
        # Write the new python text to the end of the file
        f.write(python_code)

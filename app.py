from integrations import call_gpt_api
from integrations import create_python_file
from integrations import append_python_file


def check_if_user_requests_exit(user_input):
    """Checks if the user input passed in is request an exit from the program.

        Args:
            user_input: the user input to check for the string 'exit'
    """
    # Check if the user entered "exit"
    if user_input.lower() == 'exit':
        print("Existing script")
        return True
    return False


def prompt_for_python_code_to_file(method_to_use_for_gpt_response,
                                   file_prompt_text):
    """Prompts the user for a file name and prompt to GPT to generate python code and
        add it to the file specified (new or existing files)

        Args:
            method_to_use_for_gpt_response: method to use to process the GPT response to a file (for new
                or existing files)
            file_prompt_text: The prompt text to the user for the file; will differ depending on if
                the file is new or an existing file

        Returns:
            An indicator if the user specified to exist the program
    """
    file_name_input = input(file_prompt_text)
    if check_if_user_requests_exit(file_name_input):
        return True

    code_question_input = input("Enter in a prompt for python code: ")
    if check_if_user_requests_exit(code_question_input):
        return True

    gpt_response_text = call_gpt_api(code_question_input)
    method_to_use_for_gpt_response(file_name_input, gpt_response_text)
    return False


if __name__ == '__main__':
    while True:
        print("Hint: type 'exit' to quit at any time")

        selection_input = input("Enter 1 to prompt for python code for a new file or enter 2 to prompt "
                                "for python code to add to an existing file: ")

        if check_if_user_requests_exit(selection_input):
            break
        if selection_input == "1":
            if prompt_for_python_code_to_file(create_python_file,
                                              "Enter a file name for the generated python code to be created in: "):
                break
        elif selection_input == "2":
            if prompt_for_python_code_to_file(append_python_file,
                                              "Enter a file name for an existing file to append the "
                                              "generated python code to: "):
                break
        else:
            print(f"The value entered was invalid (valids inputs are '1' or '2'): {selection_input}")

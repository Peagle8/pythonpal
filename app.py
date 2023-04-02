from integrations import call_gpt_api
from integrations import create_python_for_gpt_response
from integrations import append_python_for_gtp_response


def user_requests_exit(user_input):
    # Check if the user entered "exit"
    if user_input.lower() == 'exit':
        print("Existing script")
        return True
    return False


def prompt_for_new_python_file():
    file_name_input = input("Enter a file name for the generated python code to be created in: ")
    if user_requests_exit(file_name_input):
        return True

    code_question_input = input("Enter in a prompt for python code: ")
    if user_requests_exit(code_question_input):
        return True

    gpt_response_text = call_gpt_api(code_question_input)
    create_python_for_gpt_response(file_name_input, gpt_response_text)
    return False


def prompt_for_an_exiting_file():
    file_name_input = input("Enter a file name for an existing file to append the generated python code to: ")
    if user_requests_exit(file_name_input):
        return True

    code_question_input = input("Enter in a prompt for python code: ")
    if user_requests_exit(code_question_input):
        return True

    gpt_response_text = call_gpt_api(code_question_input)
    append_python_for_gtp_response(file_name_input, gpt_response_text)
    return False


if __name__ == '__main__':
    while True:
        print("Hint: type 'exit' to quit at any time")

        selection_input = input("Enter 1 to prompt for python code for a new file or enter 2 to prompt "
                                "for python code to add to an existing file: ")

        if user_requests_exit(selection_input):
            break
        if selection_input == "1":
            if prompt_for_new_python_file():
                break
        elif selection_input == "2":
            if prompt_for_an_exiting_file():
                break
        else:
            print(f"The value entered was invalid (valids inputs are '1' or '2'): {selection_input}")

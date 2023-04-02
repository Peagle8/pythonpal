import requests
import json


def call_chat_gpt():
    # Replace with your own API key
    api_key = 'your_api_key_here'

    # Set up the API request headers
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    # Set up the API request payload
    payload = {
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': 'What is the capital of France?'}
        ]
    }

    # Make the POST request to the Chat GPT API
    response = requests.post(
        'https://api.openai.com/v1/assistant/completions',
        headers=headers,
        data=json.dumps(payload)
    )

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the assistant's response from the API response
        assistant_response = response.json()['choices'][0]['message']['content']
        print(f"Assistant: {assistant_response}")
    else:
        print(f"Request failed with status code {response.status_code}")


if __name__ == '__main__':
    call_chat_gpt()



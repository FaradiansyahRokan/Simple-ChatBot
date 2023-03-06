import json
import re
import random_responses


# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully!")
        return json.load(bot_responses)


# Store JSON data
response_data = load_json("bot.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return random_responses.random_string()


while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))

# import openai

# openai.api_key = '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'

# def get_api_response(prompt: str) -> str | None:
#     text: str | None = None

#     try:
#         response: dict = openai.Completion.create(
#             model='text-davinci-003',
#             prompt=prompt,
#             temperature=0.9,
#             max_tokens=150,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0.6,
#             stop=[' Human:', ' AI:']
#         )

#         choices: dict = response.get('choices')[0]
#         text = choices.get('text')

#     except Exception as e:
#         print('ERROR:', e)

#     return text


# def update_list(message: str, pl: list[str]):
#     pl.append(message)


# def create_prompt(message: str, pl: list[str]) -> str:
#     p_message: str = f'\nHuman: {message}'
#     update_list(p_message, pl)
#     prompt: str = ''.join(pl)
#     return prompt


# def get_bot_response(message: str, pl: list[str]) -> str:
#     prompt: str = create_prompt(message, pl)
#     bot_response: str = get_api_response(prompt)

#     if bot_response:
#         update_list(bot_response, pl)
#         pos: int = bot_response.find('\nAI: ')
#         bot_response = bot_response[pos + 5:]
#     else:
#         bot_response = 'Something went wrong...'

#     return bot_response


# def main():
#     prompt_list: list[str] = ['You are a potato and will answer as a potato',
#                               '\nHuman: What time is it?',
#                               '\nAI: I have no idea, I\'m a potato!']

#     while True:
#         user_input: str = input('Rokan: ')
#         response: str = get_bot_response(user_input, prompt_list)
#         print(f'AI: {response}')


# if __name__ == '__main__':

#     main()

import prompt


def welcome_user(game_intro=""):
    print("Welcome to the Brain Games!")
    if game_intro:
        print(f"{game_intro}")
    print()
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name

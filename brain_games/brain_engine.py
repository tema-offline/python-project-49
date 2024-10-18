import prompt


def run(game):
    max_score = 3
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.RULES)
    for _ in range(max_score):
        question, answer = game.game_logic()
        print(f'Question: {question}')
        player_answer = prompt.string("Your answer: ")
        if player_answer != str(answer):
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')

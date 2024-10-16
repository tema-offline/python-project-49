import prompt


def game_run(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.RULES)
    correct_answer = 0
    for _ in range(3):
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
        correct_answer += 1
    if correct_answer == 3:
        print(f'Congratulations, {name}!')

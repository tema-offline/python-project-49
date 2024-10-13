from brain_games.cli import welcome_user
import prompt


def game_run(game):
    player_name = welcome_user()
    print(game.RULES)
    quanity = 0
    while quanity < 3:
        question, answer = game.run_game()
        print(f'Question: {question}')
        player_answer = prompt.string("Your answer: ")
        if player_answer != str(answer):
            print(f"'{player_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {player_name}!")
            break
        else:
            print('Correct!')
        quanity += 1
    if quanity == 3:
        print(f'Congratulations, {player_name}!')

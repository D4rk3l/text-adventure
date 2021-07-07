def show_man(attempts):
    if attempts == 0:
        print("   ____")
        print("  |    |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("__|__")

    elif attempts == 1:
        print("   ____")
        print("  |    |")
        print("  |    o")
        print("  |")
        print("  |")
        print("  |")
        print("__|__")

    elif attempts == 2:
        print("   ____")
        print("  |    |")
        print("  |    o")
        print("  |   /|\\")
        print("  |")
        print("  |")
        print("__|__")

    elif attempts == 3:
        print("   ____")
        print("  |    |")
        print("  |    o")
        print("  |   /|\\")
        print("  |    |")
        print("  |")
        print("__|__")

    elif attempts == 4:
        print("   ____")
        print("  |    |")
        print("  |    o")
        print("  |   /|\\")
        print("  |    |")
        print("  |   / ")
        print("__|__")

    elif attempts == 5:
        print("   ____")
        print("  |    |      ")
        print("  |    o      ")
        print("  |   /|\\     ")
        print("  |    |")
        print("  |   / \\")
        print("__|__")


def show_board(failed_attempts, letters_discovered, secret):
    show_man(failed_attempts)
    for i in secret:
        if i in letters_discovered:
            print(str(i)+" ", end='')
        else:
            print("_ ", end='')


def verify_guess(secret, guess, letters_discovered):
    try:
        secret = secret.remove(letters_discovered)
    except:
        pass

    if guess in secret:
        return True
    return False


def verify_winning_condition(secret, letters_discovered):
    return all(item in letters_discovered for item in secret)


def verify_game_over(failed_attempts):
    return True if failed_attempts >= 5 else False


def text_based_hangman():
    secret = ""
    while len(secret.strip()) < 1:
        secret = input("Hello Player 1, tell me the secret word!: ")

    secret = list(secret)
    letters_discovered = []
    failed_attempts = 0
    show_board(failed_attempts, letters_discovered, secret)
    while True:
        guess = input("\nPlayer 2, try to guess some letter: ")
        if verify_guess(secret, guess, letters_discovered):
            letters_discovered.append(guess)
        else:
            failed_attempts += 1

        show_board(failed_attempts, letters_discovered, secret)
        if verify_winning_condition(secret, letters_discovered):
            print("\nYes!!! it was \"" + "".join(secret) + "\", you did it!")
            break
        if verify_game_over(failed_attempts):
            print("\nGame over :(\nThe word was \"" + "".join(secret))
            break


text_based_hangman()

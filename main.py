# made by Ksenia Braginsky
HANGMAN_PHOTOS = {
    1: """
            x-------x""",
    2: """
            x-------x
            |
            |
            |
            |
            |
        """,
    3: """
            x-------x
            |       |
            |       0
            |
            |
            |
        """,
    4: """
            x-------x
            |       |
            |       0
            |       |
            |
            |
        """,
    5: """
            x-------x
            |       |
            |       0
            |      /|\\
            |
            |
        """,
    6: """
            x-------x
            |       |
            |       0
            |      /|\\
            |      /
            |
        """,
    7: """
            x-------x
            |       |
            |       0
            |      /|\\
            |      / \\
            |
        """
}
HANGMAN_ASCII_ART = """
      _    _
     | |  | |
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
     |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                          __/ |
                         |___/
    """
DEAD = """
               ...
             .####_  .
           ;#|\\_|/__/|
         ;##/ / \\/ \\  \\
        ;##/__|O||O|__ \\
       ,##|/_ \\_/\\_/ _\\ |        OOO\\
       ###| | (____) | ||       OOOOO\\
       ;##\\/\\___/\\__/\\ //      OOOOOOOO
      ,;####`.      \\_)/       / OOOOOOO
    ;#########`. ,,,;./       /  / DOOOOOO
  .';#################;,     /  /     DOOOO
 ,######;######;;;;####;,   /  /        DOOO
;`######`'######;;;##### ,H/  /          DOOO
#`#######`;######;;### ;##H  /            DOOO
##`#######`;######## ;####H /              DOO
`#`#######`;###### ;######H/               DOO
 ###`#######`;; ;#########HH                OO
 ####`#######`;########;###H                OO
 `#####`############;'`#;##H                O
  `#####`########;' /  / `#H
   ######`#####;'  /  /   `H
"""
WIN = """
⢸⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⡷⡄
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ |
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ |
⢸⠀⠀⠀⠀⢀⠖⠒⠒⠒⢤⠀⠀⠀⠀|
⢸⠀⠀⣀⢤⣼⣀⡠⠤⠤⠼⠤⡄
⢸⠀⠀⠑⡤⠤⡒⠒⠒⡊⠙⡏⠀⢀
⢸⠀⠀⠀⠇⠀⣀⣀⣀⣀⢀⠧⠟⠁
⢸⠀⠀⠀⠸⣀⠀⠀⠈⢉⠟⠓
⢸⠀⠀⠀⠀⠈⢱⡖⠋⠁
⢸⠀⠀⠀⠀⣠⢺⠧⢄⣀⠀⠀⣀⣀
⢸⠀⠀⠀⣠⠃⢸⠀⠀⠈⠉⡽⠿⠯⡆
⢸⠀⠀⣰⠁⠀⢸⠀⠀⠀⠀⠉⠉⠉
⢸⠀⠀⠣⠀⠀⢸⢄
⢸⠀⠀⠀⠀⠀⢸⠀⢇
⢸⠀⠀⠀⠀⠀⡌⠀⠈⡆
⢸⠀⠀⠀⠀⢠⠃⠀⠀⡇
⢸⠀⠀⠀⠀⢸⠀⠀⠀⠁
"""
MAX_TRIES = 7


# hangman_ex1.4.2
def opening_screen(hangman_ascii_art, max_tries):
    """Check if the input is a valid single alphabet char.
        :param: hangman_ascii_art
        :param:  max_tries
        :type: str
        :type: int
        :return: print opening screen and rules
        :rtype: none
        """
    print(f"""{hangman_ascii_art}
    1. Choose only a single English alphabet
    2. Words less then 2 letters or containing non-alphabet chars are emitted from the chosen file 
    3. If you try a letter you've already tried before you won't lose an attempt
    4. Repeating letters will be filled in all occurrences in the word.
    you have {max_tries - 1} tries, hang in there.
    Good luck!
    """)


# hangman_ex5.5.1
def check_valid_input(letter_guessed, old_letters_guessed):
    """Check if the input is a valid single alphabet char.
    :param: letter_guessed
    :param: old_letters_guessed
    :type: str
    :type: list
    :return: True if input is a single alphabet char
    :rtype: bool
    """
    if len(letter_guessed) != 1:
        print("E1 please enter only 1 letter")
        return False
    elif not (letter_guessed.isalpha()):
        print("E2 please choose letters only")
        return False
    elif letter_guessed in old_letters_guessed:
        print("You already tried this letter")
        return False
    else:
        return True


# hangman_ex642
def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    """If the guessed letter is valid and hasn't been guessed before, add it to
    the list of guessed letters, otherwise print the guessed tries thus far sorted.
    :param: letter_guessed
    :param: old_letters_guessed
    :param: secret_word
    :type: str
    :type: list
    :type: str
    :return: True if letter guessed is valid
    :rtype: bool
    """
    joined_sorted_old_letters = " -> ".join(old_letters_guessed)
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        print(f"Letter '{letter_guessed.lower()}' added to guessed letters: {joined_sorted_old_letters}")
        if not(letter_guessed in secret_word):
            return True
    else:
        print("X: Invalid char or you tried this before \n Guessed letters: ", joined_sorted_old_letters)
        return False


# hangman_ex731
def show_hidden_word(secret_word, old_letters_guessed):
    """Show all appearances of guessed letters in secret word.
    :param: secret_word
    :param: old_letters_guessed
    :type: str
    :type: list
    :return: print secret word with revealed letters
    :rtype: none
    """
    secret_word_list = hint = list(secret_word)
    for i in range(len(secret_word_list)):
        for j in range(len(secret_word_list)):
            if not (secret_word_list[i] in old_letters_guessed):
                hint[i] = "_"
    print(" ".join(hint))


# hangman_ex732
def check_win(secret_word, old_letters_guessed):
    """Return True if all th secret word letters are in the users guess list, otherwise return False.
     :param: secret_word
     :param: old_letters_guessed
     :type: str
     :type: list
     :return: True/False if all secret word letters have been guessed.
     :rtype: bool
     """
    secret_word_letters_list = list(secret_word)
    if all(char in old_letters_guessed for char in secret_word_letters_list):
        print(f"""YOU WIN! GOOD JOB
        {WIN}""")
        return True
    else:
        return False


# hangman_ex841
def print_hangman(num_of_tries):
    """print the current dudes state in ASCII"""
    print(HANGMAN_PHOTOS[num_of_tries])


# hangman_ex941
def choose_word(file_path, index):
    """Choose a word in the index selected by the user, in a file which path was given by the user.
    :param: index
    :param: file_path
    :type: str
    :type: int
    :return: the selected word at the chosen index
    :rtype: str
    """
    with open(file_path.strip()) as text_file:
        words_list = []
        for line in text_file:
            for word in line.split():
                if len(word) > 2 and word.isalpha():
                    words_list.append(word)
        file_length = len(words_list)
        # if chosen index is higher then file length continue count from beginning of the file
        idx_iterate = (file_length + int(index)) % file_length
        selected_word = words_list[idx_iterate - 1]
        # tuple_return = file_length, selected_word
    return selected_word


# helpers
def check_lose(max_tries, attempts, secret_word):
    """Check if number of allowed attempts is equal to number of the users attempts.
        :param: max_tries
        :param: attempts
        :param: secret_word
        :type: int
        :type: int
        :type: str
        :return: print lose if game over
        :rtype: none
        """
    if max_tries == attempts:
        print(f"""{print_hangman(7)} 
        YOU LOSE
        secret word was '{secret_word}'
        {DEAD}""")


def guesses_left(max_tries, num_of_tries):
    """Check how many guesses are left.
            :param: max_tries
            :param: num_of_tries
            :type: int
            :type: int
            :return: no return value
            :rtype: none
            """
    print(f"Guesses left: {max_tries - num_of_tries}")


def main():
    num_of_tries = 1
    guessed_letters_list = []
    opening_screen(HANGMAN_ASCII_ART, MAX_TRIES)
    file_path = input("Please enter file path: ")
    index = input("Please pick a random number: ")
    while not(str(index).isnumeric()):
        index = input("Please pick a random NUMBER: ")
    secret_word = choose_word(file_path, index)
    # print(f"selected_word: {secret_word}")
    while MAX_TRIES > num_of_tries and not(check_win(secret_word, guessed_letters_list)):
        print_hangman(num_of_tries)
        letter_guessed = input("Guess a letter: ")
        if try_update_letter_guessed(letter_guessed, guessed_letters_list, secret_word):
            num_of_tries += 1
        show_hidden_word(secret_word, guessed_letters_list)
        check_lose(MAX_TRIES, num_of_tries, secret_word)
        guesses_left(MAX_TRIES, num_of_tries)


if __name__ == "__main__":
    main()


# C:\Users\user\Desktop\qveen_herby.txt
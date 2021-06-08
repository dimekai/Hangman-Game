from random import randint
from os import system

class Prettier:
    def __init__(self):
        ''' 
        Provides different methods to draw 
        the hangman game process in console.
        '''
        self.header = """\
            ================================================
            ================================================
             _   _    _    _   _  ____ __  __    _    _   _ 
            | | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
            | |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
            |  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
            |_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|
            
            ================================================
            ================================================
                            by Jesus Diaz
            
            """

        self.game_over = """\
            ========================================================
            ========================================================
              ____    ___     _______    _____     _______ ____  _ 
             / ___|  / \ \   / / ____|  / _ \ \   / / ____|  _ \| |
            | |  _  / _ \ \ / /|  _|   | | | \ \ / /|  _| | |_) | |
            | |_| |/ ___ \ V / | |___  | |_| |\ V / | |___|  _ <|_|
             \____/_/   \_\_/  |_____|  \___/  \_/  |_____|_| \_(_)
            ========================================================
            ========================================================
            """

        self.won = """\
            ========================================================
            ========================================================
                \ \ / / _ \| | | | \ \      / / _ \| \ | | | |
                 \ V / | | | | | |  \ \ /\ / / | | |  \| | | |
                  | || |_| | |_| |   \ V  V /| |_| | |\  | |_|
                  |_| \___/ \___/     \_/\_/  \___/|_| \_| (_)
            ========================================================
            ========================================================
            """
        
        self.lost = """\
                            |_______________``\\
                    [/]           [  ]
                    [\]           | ||
                    [/]           |  |
                    [\]           |  |
                    [/]           || |
                   [---]          |  |
                   [---]          |@ |
                   [---]          |  |
                  oOOOOOo         |  |
                 oOO___OOo        | @|
                oO/|||||\Oo       |  |
                OO/|||||\OOo      |  |
                *O\ x x /OO*      |  |
                /*|  c  |O*\      |  |
                   \_O_/    \     |  |
                    \#/     |     |  |
                 |       |  |     | ||
                 |       |  |_____| ||__
                _/_______\__|  \  ||||  \\
                /         \_|\  _ | ||\  \\
                |    V    |\  \//\  \  \  \\
                |    |    | __//  \  \  \  \\
                |    |    |\|//|\  \  \  \  \\
                ------------\--- \  \  \  \  \\
                \  \  \  \  \  \  \  \  \  \  \\
                _\__\__\__\__\__\__\__\__\__\__\\
                __|__|__|__|__|__|__|__|__|__|__|
                |___| |___|
                |###/ \###|
                \##/   \##/
                ``     ``
            ========================================================
            ========================================================
                __   _____  _   _   _     ___  ____ _____   _ 
                \ \ / / _ \| | | | | |   / _ \/ ___|_   _| | |
                 \ V / | | | | | | | |  | | | \___ \ | |   | |
                  | || |_| | |_| | | |__| |_| |___) || |   |_|
                  |_| \___/ \___/  |_____\___/|____/ |_|   (_)
            ========================================================
            ========================================================
            """
        
        self.HANGMANPICS = ['''
                    +---+
                    |   |
                        |
                        |
                        |
                        |
                    =========''', '''
                    +---+
                    |   |
                    O   |
                        |
                        |
                        |
                    =========''', '''
                    +---+
                    |   |
                    O   |
                    |   |
                        |
                        |
                    =========''', '''
                    +---+
                    |   |
                    O   |
                   /|   |
                        |
                        |
                    =========''', '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                        |
                        |
                    =========''', '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                   /    |
                        |
                    =========''', '''
                    +---+
                    |   |
                    O   |
                   /|\  |
                   / \  |
                        |
                    =========''']
        self.base = self.HANGMANPICS[0]
    
    def get_hang_pick(self, strike:int) -> str:
        ''' 
        Gets the image to draw on the terminal, 
        according to the number of attempts.

        params
        ------
            - strike : int
                Represent the attempt number
        
        return
        ------
            - hangpick : str
                It is the drawing of the hanged man.
        '''
        return self.HANGMANPICS[strike]

    def showHeader(self):
        ''' 
        Prints the game header
        '''
        print(self.header)
    
    def showWon(self):
        '''
        Print the winner's legend
        '''
        print(self.won)
    
    def showLost(self):
        '''
        Print the loser's legend
        '''
        print(self.lost)


class Data:
    def __init__(self):
        '''
        Provides methods necessary to retrieve words 
        from a file and return a word randomly.
        '''
        self.__PATH = "./archivos/data.txt"
        
    def __get_data(self):
        '''
        Read the words from a text file to store them
        into a list of strings using list comprehenssion
        '''
        with open(self.__PATH, "r", encoding="utf-8") as f:
            self.__data = [word.replace('\n','') for word in f]

    def __normalize(self, word:str) -> str:
        '''
        Changes special characters with accents in a word.

        params
        ------
            - word : str
                Represent the word which contains accents
            
        return
        ------
            The word without accents
        '''
        new_word = word.maketrans('áéíóú', 'aeiou')
        return word.translate(new_word)
    
    def choose_random_word(self) -> str:
        '''
        Gets a word, randomly, from the word list: self.__data
        Word does not contains any accents
        
        
        return
        ------
            Random word without accents
        '''
        self.__get_data()
        rand_idx = randint(0,len(self.__data) - 1)
        return self.__normalize(self.__data[rand_idx])
        
    
class Hangman:
    def __init__(self):
        self.ans = ""
        self.pretty = Prettier()
    
    def get_spaces(self, word:str) -> str:
        '''
        It generates a string with dashes with
        the size of the word to be guessed.


        params
        ------
            - word: str
                Represent the word to be guessed
            
        return
        ------
            Dashes string.
            Represents the hidden word.

        '''
        return "_" * len(word)

    def show_menu(self, spaces:str = "", strike:int = 0):
        '''
        Displays the Hangman menu with the 
        draws in the terminal

        params
        ------
            - spaces: str
                It is the hidden word
            
            - strike: int
                It is the number of user attempts
        '''
        self.pretty.showHeader()
        print(self.pretty.HANGMANPICS[strike])
        print("Guess the word!\n")
        print("\t\t\t\t", " ".join(spaces))
        print("\n")
    
    def play(self, word:str = "", spaces:str = "", showWord:bool = False):
        '''
        Allows you to play Hangman. The user enters a letter to guess the word. 
        If the letter is not in the word, the number of strikes is increased 
        (maximum number of attempts is 7).

        params
        ------
            - word : str
                It is the word to be guessed
            
            - spaces : str
                It is the hidden word to be guessed
            
            - [showWord] : bool
                Display the word to be guessed just once
        '''
        if showWord: 
            print(word)
        
        word_lst = list(word)
        ans_lst = list(spaces)
        strikes = 0
        
        while ans_lst != word_lst and (strikes < len(word) + 2):

            letter_usr = input("Type a letter and press enter:\t")
            letter_usr = letter_usr.upper()
            is_strike = True

            system("clear")
            assert len(letter_usr) == 1 and letter_usr.isalpha(), "Escribe una sola letra del alfabeto"
            for i, letter in enumerate(word_lst):
                if letter == letter_usr:
                    ans_lst[i] = letter
                    is_strike = False
            
            if is_strike: 
                strikes += 1

            if (strikes > 6):
                is_strike = True
                break
            else:
                self.show_menu(ans_lst, strikes)
                print("Strikes:   ",strikes)
            
        if strikes < 7 and not is_strike:
            self.pretty.showWon()
        else:
            self.pretty.showLost()

        print(f"\t\t\t  The word was {word}")


def run():
    '''
    Start the Hangman game
    '''
    system("clear")
    hangman = Hangman()
    word = Data().choose_random_word().upper()
    spaces = hangman.get_spaces(word)
    hangman.show_menu(spaces)
    hangman.play(word, spaces)


if __name__ == '__main__':
    run()
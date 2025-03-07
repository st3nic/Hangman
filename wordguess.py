import tkinter as tk
import random

class HangmanGame:
    def __init__(self, word_file):
        self.wordlist = self.load_wordlist(word_file)
        self.window = tk.Tk()
        self.window.title("Y4SBW/McG Word Guessing Game")
        self.initialize_game()

        # Start the GUI event loop
        self.window.mainloop()

    def load_wordlist(self, word_file):
        # Load words from a text file and return as a list
        try:
            with open(word_file, 'r') as file:
                wordlist = file.read().splitlines()
            return wordlist
        except FileNotFoundError:
            print(f"Error: The file {word_file} was not found.")
            return []

    def initialize_game(self):
        # Select a new secret word
        self.secret_word = random.choice(self.wordlist).upper() if self.wordlist else ""
        self.guessed_letters = []
        self.wrong_attempts = 0
        self.max_attempts = 8

        self.heading = tk.Label(self.window, text=('Y4SBW/McG Word Guessing Game'), font=("Arial", 30))
        self.heading.pack(pady=20)

        # Label to display the current word (with blanks for unguessed letters)
        self.word_label = tk.Label(self.window, text=self.get_display_word(), font=("Arial", 30))
        self.word_label.pack(pady=20)

        # Label to show the number of wrong attempts
        self.attempts_label = tk.Label(self.window, text=f"Wrong attempts: {self.wrong_attempts}/{self.max_attempts}", font=("Arial", 14))
        self.attempts_label.pack()

        # Entry box to input guesses
        self.guess_entry = tk.Entry(self.window, font=("Arial", 14))
        self.guess_entry.pack(pady=10)

        # Button to submit the guess
        self.guess_button = tk.Button(self.window, text="Guess", font=("Arial", 14), command=self.check_guess)
        self.guess_button.pack(pady=10)

        # Label to display the game status (win/lose message)
        self.status_label = tk.Label(self.window, text="", font=("Arial", 14))
        self.status_label.pack(pady=20)

        # Button to try again after a win or loss (initially hidden)
        self.try_again_button = tk.Button(self.window, text="Try Again", font=("Arial", 14), command=self.try_again, state=tk.DISABLED)
        self.try_again_button.pack(pady=10)

    def get_display_word(self):
        # Display the word with blanks for unguessed letters
        return ' '.join([letter if letter in self.guessed_letters else "_" for letter in self.secret_word])

    def check_guess(self):
        # Get the user's guess from the entry box
        guess = self.guess_entry.get().upper()
        self.guess_entry.delete(0, tk.END)  # Clear the entry box
        
        # Ensure the guess is a single letter
        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                self.status_label.config(text="You've already guessed that letter!")
            elif guess in self.secret_word:
                self.guessed_letters.append(guess)
                self.status_label.config(text="Good guess!")
            else:
                self.wrong_attempts += 1
                self.guessed_letters.append(guess)
                self.status_label.config(text="Wrong guess!")

            # Update the word display and attempts label
            self.word_label.config(text=self.get_display_word())
            self.attempts_label.config(text=f"Wrong attempts: {self.wrong_attempts}/{self.max_attempts}")
            
            # Check for win/lose conditions
            if all(letter in self.guessed_letters for letter in self.secret_word):
                self.status_label.config(text="Congratulations, you win!")
                self.guess_button.config(state=tk.DISABLED)  # Disable further guessing
                self.try_again_button.config(state=tk.NORMAL)  # Enable the "Try Again" button
            elif self.wrong_attempts >= self.max_attempts:
                self.status_label.config(text=f"Game over! The word was {self.secret_word}.")
                self.guess_button.config(state=tk.DISABLED)  # Disable further guessing
                self.try_again_button.config(state=tk.NORMAL)  # Enable the "Try Again" button
        else:
            self.status_label.config(text="Please enter a valid single letter.")

    def try_again(self):
        # Clear the previous game state and reset the game
        self.guessed_letters = []
        self.wrong_attempts = 0

        # Select a new secret word
        self.secret_word = random.choice(self.wordlist).upper() if self.wordlist else ""

        # Update the UI elements to reflect the new game state
        self.word_label.config(text=self.get_display_word())  # Show new word with blanks
        self.attempts_label.config(text=f"Wrong attempts: {self.wrong_attempts}/{self.max_attempts}")
        self.status_label.config(text="")  # Clear any previous win/loss message
        self.guess_button.config(state=tk.NORMAL)  # Re-enable the guess button
        self.try_again_button.config(state=tk.DISABLED)  # Disable the "Try Again" button

# Example word file path (make sure to replace this with your own file path)
word_file = "words.txt"

# Start the game
if __name__ == "__main__":
    game = HangmanGame(word_file)

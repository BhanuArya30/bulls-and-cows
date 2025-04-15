#!/usr/bin/env python3
"""
Command Line Interface for the Bulls and Cows game.
This module provides a terminal-based interface for playing the game.
"""

import os
import sys
import time
from typing import List, Dict, Tuple

# Add the parent directory to the path so we can import the game_logic module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.game_logic import (
    generate_secret_number,
    evaluate_guess,
    is_valid_guess
)


class BullsAndCowsCLI:
    """Command Line Interface for Bulls and Cows game."""
    
    def __init__(self):
        """Initialize the game with a new secret number and empty history."""
        self.secret = generate_secret_number()
        self.attempts = 0
        self.history = []
        self.start_time = time.time()
        
    def display_welcome(self) -> None:
        """Display welcome message and game instructions."""
        print("\n" + "=" * 50)
        print("🐮 BULLS AND COWS GAME 🐂")
        print("=" * 50)
        print("\nI've selected a 4-digit number with unique digits.")
        print("Try to guess it with the following hints:")
        print("  - 🐂 Bulls: Correct digits in the correct position")
        print("  - 🐄 Cows: Correct digits in the wrong position")
        print("\nType 'quit' to exit the game at any time.")
        print("=" * 50 + "\n")
        
    def display_history(self) -> None:
        """Display the history of guesses and their results."""
        if not self.history:
            return
            
        print("\n📜 GUESS HISTORY:")
        print("-" * 30)
        for i, (guess, result) in enumerate(self.history, 1):
            print(f"{i:2d}. {guess} ➜ {result['bulls']} Bulls, {result['cows']} Cows")
        print("-" * 30)
        
    def get_valid_guess(self) -> str:
        """
        Get a valid guess from the user.
        
        Returns:
            str: A valid 4-digit guess or 'quit' to exit
        """
        while True:
            guess = input("Enter your guess (4 unique digits): ").strip().lower()
            
            if guess == 'quit':
                return guess
                
            valid, error_msg = is_valid_guess(guess)
            if valid:
                return guess
            else:
                print(f"❌ Invalid input: {error_msg}. Please try again.")
                
    def play_game(self) -> None:
        """Main game loop."""
        self.display_welcome()
        
        while True:
            self.display_history()
            guess = self.get_valid_guess()
            
            if guess == 'quit':
                print(f"\n👋 Thanks for playing! The secret number was {self.secret}.")
                break
                
            self.attempts += 1
            
            if guess == self.secret:
                elapsed_time = time.time() - self.start_time
                print("\n" + "🎉" * 10)
                print(f"🎊 CONGRATULATIONS! You've guessed the number: {self.secret}")
                print(f"✨ It took you {self.attempts} attempts and {elapsed_time:.1f} seconds!")
                print("🎉" * 10)
                break
                
            result = evaluate_guess(guess, self.secret)
            self.history.append((guess, result))
            print(f"\n🔍 Result: {result['bulls']} Bulls, {result['cows']} Cows")
            
    def play_again(self) -> bool:
        """
        Ask if the user wants to play again.
        
        Returns:
            bool: True if the user wants to play again, False otherwise
        """
        while True:
            response = input("\nDo you want to play again? (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'.")


def main():
    """Main function to run the CLI game."""
    play_again = True
    
    while play_again:
        game = BullsAndCowsCLI()
        game.play_game()
        play_again = game.play_again()
        
    print("\n👋 Thanks for playing Bulls and Cows! See you next time!")


if __name__ == "__main__":
    main()
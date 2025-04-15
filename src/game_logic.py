"""
Core game logic for the Bulls and Cows game.
This module contains functions for generating random numbers,
evaluating guesses, and other game mechanics.
"""

import random
import os
from typing import Dict, Tuple


def generate_secret_number() -> str:
    """
    Generate a 4-digit number with unique digits.
    
    Returns:
        str: A 4-digit number as a string
    """
    digits = random.sample(range(10), 4)
    secret = ''.join(map(str, digits))
    return secret


def save_secret_number(secret: str, filepath: str = "data/secret_number.txt") -> None:
    """
    Save the secret number to a file.
    
    Args:
        secret (str): The secret number to save
        filepath (str): Path to the file where the number will be saved
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, "w") as file:
        file.write(secret)


def load_secret_number(filepath: str = "data/secret_number.txt") -> str:
    """
    Load the secret number from a file.
    
    Args:
        filepath (str): Path to the file containing the secret number
    
    Returns:
        str: The secret number
    
    Raises:
        FileNotFoundError: If the file doesn't exist
    """
    with open(filepath, "r") as file:
        return file.read().strip()


def evaluate_guess(guess: str, secret: str) -> Dict[str, int]:
    """
    Evaluate a guess against the secret number.
    
    Args:
        guess (str): The guessed number
        secret (str): The secret number
    
    Returns:
        Dict[str, int]: Dictionary with 'bulls' and 'cows' counts
    
    Examples:
        >>> evaluate_guess("1234", "1243")
        {'bulls': 2, 'cows': 2}
        >>> evaluate_guess("5678", "1234")
        {'bulls': 0, 'cows': 0}
    """
    result = {
        'bulls': 0,
        'cows': 0
    }

    for idx, digit in enumerate(guess):
        if digit in secret:
            if secret[idx] == digit:
                result['bulls'] += 1
            else:
                result['cows'] += 1
                
    return result


def is_valid_guess(guess: str) -> Tuple[bool, str]:
    """
    Check if a guess is valid (4-digit number with unique digits).
    
    Args:
        guess (str): The guess to validate
    
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not guess.isdigit():
        return False, "Input must contain only digits"
    
    if len(guess) != 4:
        return False, "Input must be exactly 4 digits long"
    
    if len(set(guess)) != 4:
        return False, "All digits must be unique"
        
    return True, ""


def generate_and_save_secret() -> str:
    """
    Generate a new secret number and save it to a file.
    
    Returns:
        str: The generated secret number
    """
    secret = generate_secret_number()
    save_secret_number(secret)
    return secret


if __name__ == "__main__":
    # Simple demonstration of the module
    secret = generate_secret_number()
    print(f"Generated secret: {secret}")
    
    test_guess = "1234"
    result = evaluate_guess(test_guess, secret)
    print(f"Guess: {test_guess}, Result: {result}")
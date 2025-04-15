"""
Streamlit web application for the Bulls and Cows game.
This module provides a web-based interface built with Streamlit.
"""

import os
import sys
import time
import streamlit as st

# Add the parent directory to the path so we can import the game_logic module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.game_logic import (
    generate_secret_number,
    evaluate_guess,
    is_valid_guess
)


def initialize_session_state():
    """Initialize or reset the game session state."""
    if "secret" not in st.session_state:
        st.session_state.secret = generate_secret_number()
        st.session_state.attempts = 0
        st.session_state.history = []
        st.session_state.game_won = False
        st.session_state.last_guess = ""
        st.session_state.start_time = time.time()
        st.session_state.total_games = 0
        st.session_state.victories = 0
        st.session_state.best_score = float('inf')


def reset_game():
    """Reset the game state for a new game."""
    if st.session_state.game_won:
        # Update statistics before resetting
        st.session_state.total_games += 1
        st.session_state.victories += 1
        if st.session_state.attempts < st.session_state.best_score:
            st.session_state.best_score = st.session_state.attempts
    
    st.session_state.secret = generate_secret_number()
    st.session_state.attempts = 0
    st.session_state.history = []
    st.session_state.game_won = False
    st.session_state.last_guess = ""
    st.session_state.start_time = time.time()
    # Clear the input field by setting it to an empty string
    if "guess" in st.session_state:
        st.session_state.guess = ""


def display_stats():
    """Display game statistics."""
    st.sidebar.subheader("📊 Game Statistics")
    
    total_games = st.session_state.total_games
    victories = st.session_state.victories
    win_rate = (victories / total_games * 100) if total_games > 0 else 0
    best_score = st.session_state.best_score if st.session_state.best_score != float('inf') else "-"
    
    stats_cols = st.sidebar.columns(2)
    stats_cols[0].metric("Games Played", total_games)
    stats_cols[1].metric("Victories", victories)
    
    stats_cols2 = st.sidebar.columns(2)
    stats_cols2[0].metric("Win Rate", f"{win_rate:.1f}%")
    stats_cols2[1].metric("Best Score", best_score)


def display_game_rules():
    """Display game rules in the sidebar."""
    with st.sidebar.expander("🎮 Game Rules", expanded=False):
        st.markdown("""
        **Bulls and Cows** is a code-breaking game where:
        
        1. The computer generates a secret 4-digit number with unique digits
        2. You try to guess this number in as few attempts as possible
        3. After each guess, you get feedback in the form of:
           - **Bulls**: Correct digits in the correct position
           - **Cows**: Correct digits in the wrong position
        
        For example, if the secret number is "7846" and you guess "7814", you get:
        - 2 Bulls (7 and 4 are in the correct position)
        - 1 Cow (8 is correct but in the wrong position)
        
        Try to solve the puzzle in as few guesses as possible!
        """)


def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(
        page_title="Bulls and Cows Game", 
        page_icon="🐮",
        layout="wide"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # App header
    st.title("🐮 Bulls and Cows Game")
    st.markdown("---")
    
    # Sidebar content
    display_game_rules()
    if st.session_state.total_games > 0:
        display_stats()
    
    # Game content - Split into two columns
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # Display win message if game is won
        if st.session_state.game_won:
            elapsed_time = time.time() - st.session_state.start_time
            st.success(f"🎉 Congratulations! You guessed the secret number: {st.session_state.secret}")
            st.info(f"It took you {st.session_state.attempts} attempts and {elapsed_time:.1f} seconds!")
            
            if st.button("Play Again", key="play_again_button"):
                reset_game()
                st.rerun()
        
        # Input form
        with st.form(key="guess_form"):
            guess = st.text_input(
                "Enter your 4-digit guess (all digits must be unique):",
                key="guess",
                max_chars=4
            )
            
            submitted = st.form_submit_button("Submit Guess")
            
            if submitted and guess and guess != st.session_state.last_guess and not st.session_state.game_won:
                st.session_state.last_guess = guess
                
                # Validate the guess
                valid, error_msg = is_valid_guess(guess)
                if not valid:
                    st.warning(f"❌ {error_msg}")
                else:
                    st.session_state.attempts += 1
                    
                    # Check if the guess is correct
                    if guess == st.session_state.secret:
                        st.session_state.game_won = True
                        st.rerun()
                    else:
                        # Evaluate the guess
                        result = evaluate_guess(guess, st.session_state.secret)
                        st.session_state.history.append((guess, result))
                        
                        # Display immediate feedback
                        st.info(f"🔍 {result['bulls']} Bulls, {result['cows']} Cows")
    
    with col2:
        # Display guess history
        st.subheader("📜 Guess History")
        
        if not st.session_state.history:
            st.write("No guesses yet. Make your first guess!")
        else:
            # Create a nice table for the history
            history_df = {
                "Attempt": [],
                "Guess": [],
                "Bulls": [],
                "Cows": []
            }
            
            for i, (g, res) in enumerate(st.session_state.history, 1):
                history_df["Attempt"].append(i)
                history_df["Guess"].append(g)
                history_df["Bulls"].append(res["bulls"])
                history_df["Cows"].append(res["cows"])
            
            st.dataframe(history_df, use_container_width=True)
        
        # Give up option
        if not st.session_state.game_won and st.session_state.attempts > 0:
            if st.button("Give Up"):
                st.warning(f"The secret number was: {st.session_state.secret}")
                # Update total games but not victories
                st.session_state.total_games += 1
                reset_game()
                st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("Made with ❤️ | [View on GitHub](https://github.com/yourusername/bulls-and-cows)")


if __name__ == "__main__":
    main()
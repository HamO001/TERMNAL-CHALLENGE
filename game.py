import operator
import json
import random
from challenge import load_challenges_from_file

def load_challenges_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


class Game:
    def __init__(self):
        self.score = 0
        self.rounds = 3  # Number of rounds to play
        self.challenges = load_challenges_from_file('challenges.json')
        self.operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        self.difficulty_levels = {'easy': 1, 'medium': 2, 'hard': 3}
        self.current_round = 1
        self.current_difficulty = 'easy'  # Default difficulty

    def set_difficulty(self):
        print("\nChoose a difficulty level:")
        for level in self.difficulty_levels:
            print(f"{level.capitalize()}")
        choice = input("Enter the desired difficulty level: ").lower()

        if choice in self.difficulty_levels:
            self.current_difficulty = choice
        else:
            print("Invalid choice. Setting difficulty to 'easy'.")

    def generate_math_problem(self):
        num1 = random.randint(1, 10 * self.difficulty_levels[self.current_difficulty])
        num2 = random.randint(1, 10 * self.difficulty_levels[self.current_difficulty])
        operator_symbol = random.choice(list(self.operators.keys()))
        problem = f"{num1} {operator_symbol} {num2}"
        answer = str(self.operators[operator_symbol](num1, num2))
        return problem, answer

    def display_challenges(self):
        print("\nAvailable Challenges:")
        for idx, challenge in enumerate(self.challenges[self.current_difficulty], start=1):
            print(f"{idx}. {challenge}")

    def play_round(self):
        print(f"\n--- Round {self.current_round} ---")
        problem, answer = self.generate_math_problem()

        print(f"Solve the math problem:")
        print(f"Problem: {problem}")
        user_answer = input("Your answer: ")

        if user_answer == answer:
            print("Correct! You earned 10 points.")
            self.score += 10
        else:
            print("Incorrect. The correct answer was:", answer)

        print(f"Score: {self.score}")

        # Increment the round counter
        self.current_round += 1

    def run(self):
        print("Welcome to the Terminal Challenge!")

        self.set_difficulty()

        while self.current_round <= self.rounds:
            self.play_round()

        print(f"\nGame Over. Final Score: {self.score}")

        # Save the player's score to a file
        self.save_score()

    def save_score(self):
        player_name = input("Enter your name to save your score: ")
        score_entry = {'name': player_name, 'score': self.score, 'difficulty': self.current_difficulty}

        # Load existing scores or create an empty list
        try:
            with open('scores.json', 'r') as file:
                scores = json.load(file)
        except FileNotFoundError:
            scores = []

        # Append the new score entry
        scores.append(score_entry)

        # Save the scores back to the file
        with open('scores.json', 'w') as file:
            json.dump(scores, file, indent=2)
    def view_scores(self):
        print("\nView Scores:")
        # Load and display scores from a file or database
        try:
        with open('scores.json', 'r') as file:
            scores = json.load(file)
            for score in scores:
                print(f"Player: {score['name']}, Score: {score['score']}, Difficulty: {score['difficulty']}")
    except FileNotFoundError:
        print("No scores found.")


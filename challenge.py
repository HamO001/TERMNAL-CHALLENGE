class Challenge:
    def __init__(self, description):
        self.description = description

    def get_description(self):
        return self.description

def load_challenges_from_file(file_path):
    # Replace this with your logic to load challenges from a file
    # For simplicity, we are hardcoding challenges in this example
    return [Challenge("Solve a math problem"), Challenge("Guess the correct word"), Challenge("Answer a trivia question")]

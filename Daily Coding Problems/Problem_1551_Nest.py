"""
This problem was asked by Nest.

Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences. If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

The sentence must start with a capital letter, followed by a lowercase letter or a space.
All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
There must be a single space between each word.
The sentence must end with a terminal mark immediately following a word.

"""

class SentenceChecker:
    def __init__(self):
        # Initialize the current sentence being processed
        self.current_sentence = ""
        # Flag to track if a word has started
        self.word_started = False
        # Flag to track if a sentence has started
        self.sentence_started = False

    # Helper methods to categorize characters
    def is_lowercase(self, char):
        return char.islower()

    def is_uppercase(self, char):
        return char.isupper()

    def is_separator(self, char):
        return char in [',', ';', ':']

    def is_terminal_mark(self, char):
        return char in ['.', '?', '!', '‽']

    def check_stream(self, stream):
        for char in stream:
            # Check if a sentence has not started yet
            if not self.sentence_started:
                if self.is_uppercase(char):
                    # Start a new sentence with an uppercase letter
                    self.current_sentence += char
                    self.sentence_started = True
                continue

            # Handle the second character of the sentence
            if len(self.current_sentence) == 1:
                if self.is_lowercase(char) or char == ' ':
                    self.current_sentence += char
                    # Mark word as started if it's a lowercase letter
                    self.word_started = True if char != ' ' else False
                else:
                    # Invalid second character, reset the sentence
                    self.reset()
                continue

            # Handle subsequent characters
            if char == ' ':
                if self.word_started:
                    # Add space if it follows a word
                    self.current_sentence += char
                    self.word_started = False
                else:
                    # Extra space, reset the sentence
                    self.reset()
            elif self.is_lowercase(char):
                # Add lowercase letter and mark word as started
                self.current_sentence += char
                self.word_started = True
            elif self.is_separator(char):
                if self.word_started:
                    # Add separator if it follows a word
                    self.current_sentence += char
                else:
                    # Separator not following a word, reset
                    self.reset()
            elif self.is_terminal_mark(char):
                if self.word_started:
                    # Valid end of sentence
                    self.current_sentence += char
                    print(self.current_sentence)
                    self.reset()
                else:
                    # Terminal mark not following a word, reset
                    self.reset()
            else:
                # Any other character is invalid, reset
                self.reset()

    def reset(self):
        # Reset all state variables to start fresh
        self.current_sentence = ""
        self.word_started = False
        self.sentence_started = False

# Test the SentenceChecker
checker = SentenceChecker()
test_stream = "This is a valid sentence. This is another one! What about this? This is not valid because of CAPS. Neither is this one because of extra  spaces. This one is okay, it has separators. The last one is fine‽"
checker.check_stream(test_stream)
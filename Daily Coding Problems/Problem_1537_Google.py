import random

def run_markov_chain(start, transitions, num_steps):
  """Runs a Markov chain for a given number of steps and returns the state visit counts.

  Args:
    start: The starting state of the Markov chain.
    transitions: A list of tuples (from_state, to_state, probability).
    num_steps: The number of steps to run the Markov chain.

  Returns:
    A dictionary mapping states to the number of times they were visited.
  """

  state_counts = {}
  current_state = start

  # Initialize state counts
  for from_state, _, _ in transitions:
    state_counts[from_state] = 0

  for _ in range(num_steps):
    state_counts[current_state] += 1

    # Get possible next states and their probabilities
    next_state_probs = [(to_state, prob) for from_state, to_state, prob in transitions if from_state == current_state]

    # Choose the next state randomly based on probabilities
    current_state = random.choices([state for state, _ in next_state_probs], weights=[prob for _, prob in next_state_probs])[0]

  return state_counts

# Example usage
transitions = [
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]

start_state = 'a'
num_steps = 5000

state_counts = run_markov_chain(start_state, transitions, num_steps)
print(state_counts)

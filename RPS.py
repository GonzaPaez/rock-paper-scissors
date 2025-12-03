# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], play_order={}):
    # Initialization
    if not prev_play:
        # Reset history and play order
        opponent_history.clear()
        play_order.clear()
        prev_play= "R" # Default first move
    
    # Update opponent history
    opponent_history.append(prev_play)

    # Default prediction
    guess = "P"
    
    # Order of the markov model
    n = 4

    # Learning logic
    if len(opponent_history) > n:
        last_pattern = "".join(opponent_history[-(n+1):])
        play_order[last_pattern] = play_order.get(last_pattern, 0) + 1

        # Predict future move
        current_pattern = "".join(opponent_history[-n:])

        # Generate potential move
        potential_moves = [
            current_pattern + "R",
            current_pattern + "P",
            current_pattern + "S"
        ]

        # Look for the most likely next move based on history
        likely_move_seq = max(potential_moves, key=lambda k: play_order.get(k, 0))
        # The last character in that sequences is what we believe the opponent will play
        likely_next_move = likely_move_seq[-1]
        
        # Play the counte move (beat their likely move)
        beat = {"R": "P", "P": "S", "S": "R"}
        guess = beat[likely_next_move]

    return guess

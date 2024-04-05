# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[],patterns={}):
    if prev_play != "":
        opponent_history.append(prev_play)


    guess = "R"
    pattern_lenght=3
    
    if len(opponent_history) > pattern_lenght:
        
        curr_pattern = "".join(opponent_history[-pattern_lenght:])
        
        if "".join(opponent_history[-(pattern_lenght+1):]) not in patterns:
            patterns["".join(opponent_history[-(pattern_lenght+1):])] = 1
        else:
            patterns["".join(opponent_history[-(pattern_lenght+1):])] += 1
        
        
        possible_patterns = [curr_pattern + "R", curr_pattern + "P", curr_pattern + "S"]
        for i in possible_patterns:
            if i not in patterns:
                patterns[i] = 0

        op_guess = max(possible_patterns, key=lambda key: patterns[key])
        if op_guess[-1] == "P":
            guess = "S"
        if op_guess[-1] == "R":
            guess = "P"
        if op_guess[-1] == "S":
            guess = "R"

    return guess

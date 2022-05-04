#!/usr/bin/python3
def best_score(a_dictionary):
    highest_score = 0
    best_score = ""
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > highest_score:
                highest_score = v
                best_score = k
        return best_score
    return None

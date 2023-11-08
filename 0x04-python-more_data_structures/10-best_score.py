#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best_score_key = None
    for key, val in a_dictionary.items():
        if best_score_key is None or a_dictionary[best_score_key] < val:
            best_score_key = key
    return best_score_key

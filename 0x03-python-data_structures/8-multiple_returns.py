#!/usr/bin/python3
def multiple_returns(sentence):
    # return the length of the sentence and the first character
    # if sentence is empty first character should be equal to None
    if len(sentence) != 0:
        return((len(sentence), sentence[0]))
    else:
        return((len(sentence, None))

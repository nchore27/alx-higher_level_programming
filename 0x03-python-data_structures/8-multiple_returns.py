#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    return (size, None if size == 0 else sentence[0])

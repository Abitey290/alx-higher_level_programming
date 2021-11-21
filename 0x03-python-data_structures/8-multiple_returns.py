#!/usr/bin/python3


def multiple_returns(sentence):
    cnt = len(sentence)
    if cnt == 0:
        fst = None
        return cnt, fst
    else:
        fst = sentence[0]
        return cnt, fst

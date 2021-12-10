import os
import collections
import statistics

puzzle = open(os.path.join(os.path.dirname(__file__),"input")).read().splitlines()

pairs = {"<" : ">", "{" : "}", "(" : ")", "[":"]"}

def first_illegal(line):
    stack = []
    for symbol in line:
        if symbol in ["<", "{", "(", "["]:
            stack.append(symbol)
        elif len(stack) == 0:
            return symbol
        elif pairs[stack.pop()] != symbol:
            return symbol
    return None
c = collections.Counter([first_illegal(line) for line in puzzle])
print(c)
print(3 * c[")"] + 57 * c["]"] + 1197 * c["}"] + 25137* c[">"])

new_puzzle = [line for line in puzzle if first_illegal(line) is None]
print(new_puzzle)

def completion(line):
    stack = []
    for symbol in line:
        if symbol in ["<", "{", "(", "["]:
            stack.append(symbol)
        elif len(stack) == 0:
            return None
        elif pairs[stack.pop()] != symbol:
            return None
    stack.reverse()
    return "".join(map(lambda t: pairs[t], stack))

score_values = {")":1, "]":2, "}":3, ">":4}

def score(completion):
    result = 0
    for character in completion:
        result = 5 * result + score_values[character]
    return result
scores = [score(completion(line)) for line in new_puzzle]
print(statistics.median(scores))


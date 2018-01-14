"""
Probability

Code from Chapter 6 of Data Science from Scratch
"""
import random


def random_kid():
    return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0
n = 10000

random.seed(0)
for _ in range(n):
    younger = random_kid()
    older = random_kid()

    if older == "girl":
        older_girl += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

print("P(both):", both_girls/n)
print("P(older):", older_girl/n)
print("P(either):", either_girl/n)

print("P(both | older):", both_girls / older_girl) # 0.514 ~ 1/2
print("P(both | either): ", both_girls / either_girl) # 0.342 ~ 1/3

import sys
from helpers import p, inp

lines = inp(__file__)

# Rock      A   X
# Paper     B   Y
# Scissor   C   Z

# Lose      0
# Draw      3
# Win       6

shapescore = dict(X=1, Y=2, Z=3)
pointscore = dict(
    X=dict(A=3, B=0, C=6),
    Y=dict(A=6, B=3, C=0),
    Z=dict(A=0, B=6, C=3),
)

pointscore_p2 = dict(
    X=0,
    Y=3,
    Z=6,
)
choice = dict(
    A=dict(X="Z", Y="X", Z="Y"),
    B=dict(X="X", Y="Y", Z="Z"),
    C=dict(X="Y", Y="Z", Z="X"),
)

total = 0
total_p2 = 0
for line in lines:
    other, mine = line.split()
    score = shapescore[mine] + pointscore[mine][other]

    total += score

p(f"Total score part 1: {total}")

# Rock      A   X   Must lose
# Paper     B   Y   Must draw
# Scissor   C   Z   Must win

# Lose      0
# Draw      3
# Win       6


total_p2 = 0
for line in lines:
    other, result = line.strip().split()
    mine_p2 = choice[other][result]

    score_p2 = shapescore[mine_p2] + pointscore_p2[result]

    total_p2 += score_p2

p(f"Total score part 2: {total_p2}")

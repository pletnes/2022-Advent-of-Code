from helpers import inp

lines = inp(__file__)

groups = list(
    map(lambda gs: sum(map(int, str.split(gs))), "\n".join(lines).split("\n\n"))
)

answer_1 = max(groups)

print(f"The answer to part 1 is {answer_1}")

assert answer_1 == 70764

print(f"The answer to part 3 is {sum(sorted(groups)[-3:])}")

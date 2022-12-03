import string

from helpers import p, pp, inp

prio = dict(zip(string.ascii_letters, range(1, 123456789)))

total = 0
for line in inp():
    half = len(line) // 2
    left, right = line[:half], line[-half:]

    in_both = set(left) & set(right)
    dupe_item = list(in_both)[0]

    item_prio = prio[dupe_item]
    total += item_prio

assert total == 8298
print(f"Answer is {total}")

import string

from helpers import p, pp, inp

prio = dict(zip(string.ascii_letters, range(1, 123456789)))

lines = inp('')

total = 0
for line in lines:
    half = len(line) // 2
    left, right = line[:half], line[-half:]

    in_both = set(left) & set(right)
    dupe_item = list(in_both)[0]

    item_prio = prio[dupe_item]
    total += item_prio

assert total == 8298
print(f"Answer is {total}")


def group_3(items):
    ones = items[0::3]
    twos = items[1::3]
    threes = items[2::3]
    return list(zip(ones, twos, threes))


def find_unique(group):
    first, second, third = [set(g) for g in group]
    unique = first & second & third

    p(f'{unique=} {len(unique)=}')
    assert len(unique) == 1

    return list(unique)[0]


groups = group_3(lines)

unique = map(find_unique, groups)
total_p2 = sum(prio[c] for c in unique)

p(f"Answer to part 2 is {total_p2}")

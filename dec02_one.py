# Oneline solution, wrap in a "print(...)" if you want.

total = sum(dict(X=1, Y=2, Z=3)[mine] + dict(X=dict(A=3, B=0, C=6), Y=dict(A=6, B=3, C=0), Z=dict(A=0, B=6, C=3),)[mine][other] for other, mine in map(str.split, map(str.strip, open('input/dec02.txt', "r").readlines())))

assert total == 10624

print(f"Total score part 1: {total}")

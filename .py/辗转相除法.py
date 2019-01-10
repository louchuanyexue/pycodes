line1 = input()


def solution(line):
    list1 = line.split('/')
    zi = int(list1[0])
    mu = int(list1[1])
    bb = max(zi, mu)
    ss = min(zi, mu)
    r = 1
    while r != 0:
        r = bb % ss
        bb = ss
        ss = r
    zi = zi/bb
    mu = mu/bb
    return "{:.0f}/{:.0f}".format(zi, mu)


print(solution(line1))
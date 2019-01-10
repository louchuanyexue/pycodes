line1 = input()


def solution(line):
    list1 = line.split('/')
    zi = int(list1[0])
    mu = int(list1[1])
    bb = max(zi, mu)
    ss = min(zi, mu)

    while bb % 2 == 0:
        bb = bb/2
    while ss % 2 == 0:
        ss = ss/2

    ji = ss
    mi = bb
    ji = mi - ji
    while ji != mi:

        ma = max(ji, mi)
        mi = min(ji, mi)
        ji = ma - mi

    zi = zi/mi
    mu = mu/mi
    return "{:.0f}/{:.0f}".format(zi, mu)


print(solution(line1))
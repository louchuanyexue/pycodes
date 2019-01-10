s = input()


def solution(line):
    list1 = line.split()
    n1 = int(list1[0])
    n2 = int(list1[1])
    n3 = int(list1[2])

    n4 = min(n1, n2, n3)
    if n4 == n1:
        while n2 < n1+1 or n3 < n1+2:
            n1 = n1-1
        return 3*n1+3
    elif n4 == n2:
        while n1 < n2-1 or n3 < n2+1:
            n2 = n2-1
        return 3*n2
    elif n4 == n3:
        while n1 < n3-2 or n2 < n3-1:
            n3 = n3-1
        return 3*n3-3


print(solution(s))
# 주사위 게임 3
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181916
# 알고리즘: 조건문
# 작성자: 백관민
# 작성일: 2026. 08. 06. 10:31:14

def solution(a, b, c, d):
    dice = [a, b, c, d]
    counts = {}

    for num in dice:
        counts[num] = counts.get(num, 0) + 1

    if len(counts) == 1:
        p = dice[0]
        return 1111 * p

    if 3 in counts.values():
        p = max(counts, key=counts.get)
        q = min(counts, key=counts.get)
        return (10 * p + q) ** 2

    if len(counts) == 2:
        p, q = counts.keys()
        return (p + q) * abs(p - q)

    if len(counts) == 3:
        q_r = [num for num, count in counts.items() if count == 1]
        return q_r[0] * q_r[1]


    return min(dice)
        
# 옹알이 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120956
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 29. 09:11:51

def solution(babbling):
    answer = ['aya','ye','woo','ma']
    result = 0
    for i in babbling:
        b = ''
        for j in answer:
            if j in i:
                b += j
        if sorted(i) == sorted(b):
            result += 1
    return result

            
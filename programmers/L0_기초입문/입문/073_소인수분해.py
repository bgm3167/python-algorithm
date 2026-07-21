# 소인수분해
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120852
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 14:29:54

def solution(n):
    answer = []
    i = 2

    while n > 1:
        if n % i == 0:
            if i not in answer:
                answer.append(i)
            n //= i
        else:
            i += 1

    return answer
        
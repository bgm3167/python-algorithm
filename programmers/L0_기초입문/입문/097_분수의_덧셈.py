# 분수의 덧셈
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120808
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 28. 11:49:39

def solution(numer1, denom1, numer2, denom2):
    a = numer1 * denom2 + numer2 * denom1
    b = denom1 * denom2
    n = 2

    while n <= min(a, b):
        if a % n == 0 and b % n == 0:
            a //= n
            b //= n
        else:
            n += 1

    return [a, b]
        

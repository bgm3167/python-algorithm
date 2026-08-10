# 최대공약수와 최소공배수
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12940
# 알고리즘: 수학
# 작성자: 백관민
# 작성일: 2026. 08. 10. 10:38:55

def solution(n, m):
    a = 0
    for i in range(1,n+1):
        if n % i == 0 and m % i == 0:
            a = i
    return [a, n * m / a]
            
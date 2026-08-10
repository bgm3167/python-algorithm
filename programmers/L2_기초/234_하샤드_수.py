# 하샤드 수
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 알고리즘: 수학, 문자열
# 작성자: 백관민
# 작성일: 2026. 08. 10. 09:27:51

def solution(x):
    ans = 0
    num = x

    while num > 0:
        ans += num % 10
        num //= 10

    return x % ans == 0
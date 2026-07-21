# 팩토리얼
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120848
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 14:06:31

def solution(n):
    answer = 1
    fact = 1

    while fact <= n:
        answer += 1
        fact *= answer

    return answer - 1
        
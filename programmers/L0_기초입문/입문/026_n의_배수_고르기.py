# n의 배수 고르기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120905
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 10:22:16

def solution(n, numlist):
    answer = []

    for num in numlist:
        if num % n == 0:
            answer.append(num)

    return answer
            
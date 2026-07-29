# n보다 커질 때까지 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181884
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 09:32:13

def solution(numbers, n):
    a = 0
    b = 0
    while a <= n:
        a += numbers[b]
        b += 1
    return a
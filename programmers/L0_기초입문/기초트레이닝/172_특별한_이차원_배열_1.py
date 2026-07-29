# 특별한 이차원 배열 1
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181833
# 알고리즘: 이차원 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 11:03:01

def solution(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
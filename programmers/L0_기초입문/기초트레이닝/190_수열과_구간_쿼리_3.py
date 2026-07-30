# 수열과 구간 쿼리 3
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181924
# 알고리즘: 반복문
# 작성자: 백관민
# 작성일: 2026. 07. 30. 09:42:04

def solution(arr, queries):
    for a, b in queries:
        arr[a], arr[b] = arr[b], arr[a]

    return arr
        
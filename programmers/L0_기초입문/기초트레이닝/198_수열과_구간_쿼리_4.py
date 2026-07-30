# 수열과 구간 쿼리 4
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181922
# 알고리즘: 반복문
# 작성자: 백관민
# 작성일: 2026. 07. 30. 10:33:04

def solution(arr, queries):
    for a, b, c in queries:
        for j in range(a, b + 1):
            if j % c == 0:
                arr[j] += 1

    return arr
                
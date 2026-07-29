# 수열과 구간 쿼리 1
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181883
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 15:18:37

def solution(arr, queries):
    for a, b in queries:
        for i in range(a, b + 1):
            arr[i] += 1
            
    return arr
                
            
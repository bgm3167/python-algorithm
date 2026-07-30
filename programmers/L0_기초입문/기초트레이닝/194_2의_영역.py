# 2의 영역
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181894
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 30. 10:09:56

def solution(arr):
    if 2 not in arr:
        return [-1]

    start = arr.index(2)
    end = len(arr) - 1 - arr[::-1].index(2)

    return arr[start:end + 1]
            
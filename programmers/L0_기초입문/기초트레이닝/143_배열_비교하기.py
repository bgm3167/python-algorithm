# 배열 비교하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181856
# 알고리즘: 함수(메서드)
# 작성자: 백관민
# 작성일: 2026. 07. 28. 13:55:38

def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        if sum(arr1) == sum(arr2):
            return 0
        elif sum(arr1) > sum(arr2):
            return 1
        else:
            return -1
    elif len(arr1) > len(arr2):
        return 1
    else:
        return -1
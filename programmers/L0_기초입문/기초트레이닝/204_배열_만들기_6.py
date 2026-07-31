# 배열 만들기 6
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181859
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 31. 09:06:48

def solution(arr):
    stk = []
    i = 0

    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])

        elif stk[-1] == arr[i]:
            stk.pop()

        else:
            stk.append(arr[i])

        i += 1

    return stk if stk else [-1]
# 배열 만들기 4
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181918
# 알고리즘: 반복문
# 작성자: 백관민
# 작성일: 2026. 07. 31. 10:11:09

def solution(arr):
    stk = []
    i = 0

    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])

        elif stk[-1] < arr[i]:
            stk.append(arr[i])

        else:
            stk.pop()
            i -= 1

        i += 1

    return stk
# 조건에 맞게 수열 변환하기 1
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181882
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 09:28:42

def solution(arr):
    a = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            a.append(i/2)
        elif i < 50 and i % 2 == 1:
            a.append(2*i)
        else:
            a.append(i)
    return a
        
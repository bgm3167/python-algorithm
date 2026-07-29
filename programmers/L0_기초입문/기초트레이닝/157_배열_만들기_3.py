# 배열 만들기 3
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181895
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 09:47:43

def solution(arr, intervals):
    answer = []

    a1, b1 = intervals[0]
    a2, b2 = intervals[1]

    answer.extend(arr[a1:b1+1])
    answer.extend(arr[a2:b2+1])

    return answer
   
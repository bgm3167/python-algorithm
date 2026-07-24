# 조건에 맞게 수열 변환하기 3
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181835
# 알고리즘: 반복문 활용
# 작성자: 백관민
# 작성일: 2026. 07. 24. 11:23:55

def solution(arr, k):
    answer = []
    if k % 2 == 1:
        for i in range(len(arr)):
            answer.append(k*arr[i])
    else:
        for i in range(len(arr)):
            answer.append(arr[i]+k)
    return answer
            
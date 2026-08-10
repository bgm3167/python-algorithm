# 제일 작은 수 제거하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12935
# 알고리즘: 배열
# 작성자: 백관민
# 작성일: 2026. 08. 10. 10:10:03

def solution(arr):
    if len(arr) == 1:
        return [-1]

    min_value = min(arr)
    answer = []

    for i in arr:
        if i != min_value:
            answer.append(i)

    return answer
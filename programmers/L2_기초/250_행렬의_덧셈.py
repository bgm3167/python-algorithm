# 행렬의 덧셈
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12950
# 알고리즘: 배열
# 작성자: 백관민
# 작성일: 2026. 08. 10. 10:32:45

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        row = []
        for j in range(len(arr1[i])):
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)

    return answer
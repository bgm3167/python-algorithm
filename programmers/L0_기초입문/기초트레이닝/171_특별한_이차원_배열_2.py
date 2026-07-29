# 특별한 이차원 배열 2
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181831
# 알고리즘: 이차원 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 15:40:20

def solution(arr):
    for i in range(len(arr)):
        for j in range((len(arr))):
            if not arr[i][j] == arr[j][i]:
                return 0
    return 1
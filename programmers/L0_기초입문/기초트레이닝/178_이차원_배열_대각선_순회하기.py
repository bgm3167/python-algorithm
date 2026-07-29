# 이차원 배열 대각선 순회하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181829
# 알고리즘: 이차원 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 11:11:15

def solution(board, k):
    a = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                a += board[i][j]
    return a
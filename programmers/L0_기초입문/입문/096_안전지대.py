# 안전지대
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120866
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 28. 11:38:35

def solution(board):
    n = len(board)

    danger = [row[:] for row in board]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            danger[ni][nj] = 1

    cnt = 0
    for row in danger:
        cnt += row.count(1)

    return n * n - cnt
                        
                
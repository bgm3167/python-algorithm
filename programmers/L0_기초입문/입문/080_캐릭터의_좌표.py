# 캐릭터의 좌표
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120861
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 22. 10:32:09

def solution(keyinput, board):
    x, y = 0, 0

    max_x = board[0] // 2
    max_y = board[1] // 2

    for key in keyinput:
        if key == "up" and y < max_y:
            y += 1
        elif key == "down" and y > -max_y:
            y -= 1
        elif key == "left" and x > -max_x:
            x -= 1
        elif key == "right" and x < max_x:
            x += 1

    return [x, y]
    
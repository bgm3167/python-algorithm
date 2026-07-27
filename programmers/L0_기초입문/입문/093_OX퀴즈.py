# OX퀴즈
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120907
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 27. 09:27:09

def solution(quiz):
    answer = []

    for expression in quiz:
        left, right = expression.split(" = ")
        x, operator, y = left.split()

        if operator == "+":
            result = int(x) + int(y)
        else:
            result = int(x) - int(y)

        if result == int(right):
            answer.append("O")
        else:
            answer.append("X")

    return answer
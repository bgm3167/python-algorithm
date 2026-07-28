# 간단한 식 계산하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181865
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 28. 14:01:03

def solution(binomial):
    a, op, b = binomial.split()
    a, b = int(a), int(b)

    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b
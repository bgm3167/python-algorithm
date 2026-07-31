# 조건 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181934
# 알고리즘: 조건문
# 작성자: 백관민
# 작성일: 2026. 07. 31. 10:15:17

def solution(ineq, eq, n, m):
    if ineq == '>' and eq == '=':
        return int(n >= m)
    elif ineq == '<' and eq == '=':
        return int(n <= m)
    elif ineq == '>':
        return int(n > m)
    else:
        return int(n < m)
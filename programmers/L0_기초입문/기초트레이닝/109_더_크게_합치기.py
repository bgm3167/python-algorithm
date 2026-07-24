# 더 크게 합치기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181939
# 알고리즘: 연산
# 작성자: 백관민
# 작성일: 2026. 07. 24. 10:32:25

def solution(a, b):
    c = str(a)
    d = str(b)
    if int(c+d) > int(d+c): 
        return int(c+d)
    else:
        return int(d+c)
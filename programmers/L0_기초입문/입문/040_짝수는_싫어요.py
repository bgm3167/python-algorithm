# 짝수는 싫어요
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120813
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 12:32:51

def solution(n):
    a = []
    
    for i in range(n+1):
        if i % 2 == 1:
            a.append(i)
    return a

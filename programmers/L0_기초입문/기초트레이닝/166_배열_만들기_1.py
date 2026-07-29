# 배열 만들기 1
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181901
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 10:12:27

def solution(n, k):
    a = []
    b = k 
    while b <= n:
        a.append(b)
        b += k
    return a
        
        
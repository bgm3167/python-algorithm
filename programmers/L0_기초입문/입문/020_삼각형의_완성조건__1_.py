# 삼각형의 완성조건 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 12:29:05

def solution(sides):
    sides.sort()
    
    if sides[0]+sides[1] > sides[2]:
       return 1
    
    else:
        return 2
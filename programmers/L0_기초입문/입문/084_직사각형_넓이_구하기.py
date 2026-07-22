# 직사각형 넓이 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120860
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 22. 11:13:14

def solution(dots):
    x = [i[0] for i in dots]
    y = [i[1] for i in dots]

    return (max(x) - min(x)) * (max(y) - min(y))
        
    
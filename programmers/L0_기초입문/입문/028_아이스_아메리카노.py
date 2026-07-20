# 아이스 아메리카노
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120819
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 10:26:28

def solution(money):
    
    a = money // 5500
    b = money % 5500

    return[a,b]
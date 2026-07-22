# 치킨 쿠폰
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120884
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 22. 11:26:37

def solution(chicken):
    answer = 0
    coupon = 0
    while chicken > 0:
        coupon += chicken
        chicken = coupon//10
        coupon = coupon % 10
        answer += chicken
    
    return answer
        
        
        
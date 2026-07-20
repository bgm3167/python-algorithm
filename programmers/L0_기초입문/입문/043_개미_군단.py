# 개미 군단
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120837
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 12:40:06

def solution(hp):
    answer = 0
    
    answer += hp // 5  # 장군개미 수
    hp %= 5            # 남은 체력
    
    answer += hp // 3  # 병정개미 수
    hp %= 3            # 남은 체력
    
    answer += hp       # 일개미 수
    
    return answer
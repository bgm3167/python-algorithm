# 순서쌍의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120836
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 10:17:23

def solution(n):
    
    answer = 0
    
    for i in range(n):
        if n % (i+1) == 0:
            answer += 1 
            
    return answer
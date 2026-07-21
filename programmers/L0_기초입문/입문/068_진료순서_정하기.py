# 진료순서 정하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120835
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 12:03:42

def solution(emergency):
    answer = []
    rank = sorted(emergency,reverse = True)
    
    for i in emergency:
        answer.append(rank.index(i)+1)
        
    return answer
# 전국 대회 선발 고사
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181851
# 알고리즘: 함수(메서드)
# 작성자: 백관민
# 작성일: 2026. 08. 06. 09:48:02

def solution(rank, attendance):
    selected = sorted(
        [i for i in range(len(rank)) if attendance[i]],
        key=lambda i: rank[i])[:3]
    
    a, b, c = selected
    return 10000 * a + 100 * b + c
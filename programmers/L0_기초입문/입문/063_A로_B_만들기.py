# A로 B 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120886
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 10:53:42

def solution(before, after):
    return 1 if sorted(before) == sorted(after) else 0
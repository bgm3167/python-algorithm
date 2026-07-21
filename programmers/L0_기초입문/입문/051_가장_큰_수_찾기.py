# 가장 큰 수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120899
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 09:35:05

def solution(array):
    max_value = max(array)
    return [max_value, array.index(max_value)]
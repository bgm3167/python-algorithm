# 문자열 정렬하기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120911
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 09:38:32

def solution(my_string):
    answer = ''
    answer = my_string.lower()
    return "".join(sorted(answer))
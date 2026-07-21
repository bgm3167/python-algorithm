# 중복된 문자 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120888
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 10:31:06

def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
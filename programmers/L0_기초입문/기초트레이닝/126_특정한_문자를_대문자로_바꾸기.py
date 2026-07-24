# 특정한 문자를 대문자로 바꾸기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181873
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 24. 11:16:54

def solution(my_string, alp):
    answer = ''
    return my_string.replace(alp,alp.upper())
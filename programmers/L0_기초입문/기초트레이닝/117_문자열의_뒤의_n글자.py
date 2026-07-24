# 문자열의 뒤의 n글자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181910
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 24. 10:46:28

def solution(my_string, n):
    a = int(len(my_string))
    return my_string[a-n:]
# 세로 읽기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181904
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 29. 10:14:46

def solution(my_string, m, c):
    a =''
    for i in my_string[c-1::m]:
        a += i
    return a
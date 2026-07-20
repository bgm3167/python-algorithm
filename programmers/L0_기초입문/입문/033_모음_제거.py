# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 11:26:03

def solution(my_string):
    for i in "aeiou":
        my_string = my_string.replace(i, "")
    return my_string
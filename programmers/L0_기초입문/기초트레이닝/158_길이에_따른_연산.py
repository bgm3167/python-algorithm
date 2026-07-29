# 길이에 따른 연산
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181879
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 09:25:36

def solution(num_list):
    a = 0
    b = 1
    for i in num_list:
        if len(num_list) > 10:
            a += i
        else:
            b *= i
    return max(a,b)
        
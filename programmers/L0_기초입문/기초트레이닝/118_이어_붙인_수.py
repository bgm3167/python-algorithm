# 이어 붙인 수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181928
# 알고리즘: 조건문
# 작성자: 백관민
# 작성일: 2026. 07. 24. 10:54:40

def solution(num_list):
    a = ''
    b = ''
    for i in num_list:
        if i % 2 == 1:
            a += str(i)
        else: b += str(i)
    return int(a)+int(b)
            
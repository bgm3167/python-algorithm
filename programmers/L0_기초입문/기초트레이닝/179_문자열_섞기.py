# 문자열 섞기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181942
# 알고리즘: 연산
# 작성자: 백관민
# 작성일: 2026. 07. 29. 15:35:04

def solution(str1, str2):
    a = ''
    n = 0
    while n < len(str1):
        a += str1[n]
        a += str2[n]
        n += 1
    return a
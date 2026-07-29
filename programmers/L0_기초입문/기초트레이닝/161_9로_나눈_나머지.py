# 9로 나눈 나머지
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181914
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 29. 10:31:02

def solution(number):
    a = 0
    for i in number:
        a += int(i)
    return a % 9
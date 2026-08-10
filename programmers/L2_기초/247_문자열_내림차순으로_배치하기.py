# 문자열 내림차순으로 배치하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12917
# 알고리즘: 문자열, 정렬
# 작성자: 백관민
# 작성일: 2026. 08. 10. 10:19:30

def solution(s):
    a = ''
    for i in sorted(s)[::-1]:
        a += i
    return a
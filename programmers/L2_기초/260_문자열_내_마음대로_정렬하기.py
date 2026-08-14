# 문자열 내 마음대로 정렬하기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12915
# 알고리즘: 정렬
# 작성자: 백관민
# 작성일: 2026. 08. 14. 09:10:29

def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x))
    return strings
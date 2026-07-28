# 문자열 잘라서 정렬하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181866
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 28. 14:09:24

def solution(myString):
    return sorted([i for i in myString.split("x") if i])
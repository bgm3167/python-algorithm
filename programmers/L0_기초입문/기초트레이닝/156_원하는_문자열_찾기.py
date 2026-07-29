# 원하는 문자열 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181878
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 29. 09:19:56

def solution(myString, pat):
    return int(pat.lower() in myString.lower())
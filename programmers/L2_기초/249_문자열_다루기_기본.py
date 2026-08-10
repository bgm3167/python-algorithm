# 문자열 다루기 기본
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 08. 10. 10:27:27

def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    return False
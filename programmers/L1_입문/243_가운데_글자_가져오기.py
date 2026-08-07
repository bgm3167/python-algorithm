# 가운데 글자 가져오기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 08. 07. 14:00:51

def solution(s):
    a = len(s) // 2

    if len(s) % 2 == 0:
        return s[a-1:a+1]

    return s[a]
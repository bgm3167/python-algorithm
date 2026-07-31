# qr code
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181903
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 31. 09:46:41

def solution(q, r, code):
    answer = ''
    i = 0
    while ((q * i) + r) < len(code):
        answer += code[q * i + r]
        i += 1
    return answer
# 문자열 바꿔서 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181864
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 24. 11:35:36

def solution(myString, pat):
    myString =''.join('B'if ch == 'A'
                     else 'A' for ch in myString)
    if pat in myString:
        return 1
    else:
        return 0
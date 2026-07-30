# 문자열이 몇 번 등장하는지 세기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181871
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 30. 09:24:54

def solution(myString, pat):
    a =[]
    for i in range(len(myString)):
        if i < len(myString) - len(pat)+1:
            a.append(myString[i:i+len(pat):])
    return a.count(pat)
        
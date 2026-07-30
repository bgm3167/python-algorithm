# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181872
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 30. 09:30:50

def solution(myString, pat):
    while not myString.endswith(pat):
        myString = myString[:-1:]
    return myString
        
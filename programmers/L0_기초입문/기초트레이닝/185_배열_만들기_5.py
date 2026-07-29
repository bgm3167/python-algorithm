# 배열 만들기 5
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181912
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 29. 15:48:55

def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        if int(i[s:s+l:]) > k:
            answer.append(int(i[s:s+l:]))
            
    return answer
        
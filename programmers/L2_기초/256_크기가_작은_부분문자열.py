# 크기가 작은 부분문자열
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/147355
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 08. 12. 09:02:10

def solution(t, p):
    a = []
    count = 0
    for i in range(len(t) - len(p) + 1):
        a.append(t[i:i+len(p)])
    for j in a:
        if int(p) >= int(j):
            count +=1
    return count
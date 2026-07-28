# x 사이의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181867
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 28. 14:11:26

def solution(myString):
    answer =[]
    a = [i for i in myString.split("x")]
    for j in a:
        answer.append(len(j))
    return answer

# 배열에서 문자열 대소문자 변환하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181875
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 28. 16:13:12

def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            answer.append(strArr[i].lower())
        else:
            answer.append(strArr[i].upper())
    return answer
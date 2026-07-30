# 세 개의 구분자
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181862
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 30. 09:18:32

def solution(myStr):
    for separator in "abc":
        myStr = myStr.replace(separator, " ")

    answer = myStr.split()

    return answer if answer else ["EMPTY"]
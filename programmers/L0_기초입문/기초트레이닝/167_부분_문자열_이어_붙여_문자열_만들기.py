# 부분 문자열 이어 붙여 문자열 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181911
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 29. 10:28:00

def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        a,b = parts[i]
        answer += my_strings[i][a:b+1]
    return answer
        
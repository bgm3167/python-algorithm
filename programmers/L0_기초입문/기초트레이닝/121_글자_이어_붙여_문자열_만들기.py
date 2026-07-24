# 글자 이어 붙여 문자열 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181915
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 24. 11:00:59

def solution(my_string, index_list):
    answer = ''
    
    for i in index_list:
        answer += my_string[i]
    
    return answer
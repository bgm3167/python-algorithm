# 문자열 겹쳐쓰기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181943
# 알고리즘: 연산
# 작성자: 백관민
# 작성일: 2026. 08. 03. 14:01:13

def solution(my_string, overwrite_string, s):
    a = len(overwrite_string) 
    return my_string[:s]+overwrite_string+my_string[a+s:]
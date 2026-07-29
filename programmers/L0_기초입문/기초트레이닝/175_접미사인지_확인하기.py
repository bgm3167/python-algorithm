# 접미사인지 확인하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181908
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 07. 29. 09:17:54

def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))
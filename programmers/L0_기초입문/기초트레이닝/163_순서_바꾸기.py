# 순서 바꾸기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181891
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 09:41:51

def solution(num_list, n):
    return num_list[n::] + num_list[:n:]
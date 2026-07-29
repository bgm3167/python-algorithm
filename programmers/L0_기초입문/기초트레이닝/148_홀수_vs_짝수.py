# 홀수 vs 짝수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181887
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 09:40:11

def solution(num_list):
    if sum(num_list[::2]) > sum(num_list[1::2]):
        return sum(num_list[::2])
    else:
        return sum(num_list[1::2])
    
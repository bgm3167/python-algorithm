# 첫 번째로 나오는 음수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181896
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 24. 10:28:11

def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
            break
    return -1
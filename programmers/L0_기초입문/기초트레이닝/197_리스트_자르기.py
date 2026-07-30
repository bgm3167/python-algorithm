# 리스트 자르기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181897
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 30. 10:18:22

def solution(n, slicer, num_list):
    a, b, c = slicer

    if n == 1:
        return num_list[:b + 1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b + 1]
    else:
        return num_list[a:b + 1:c]
    
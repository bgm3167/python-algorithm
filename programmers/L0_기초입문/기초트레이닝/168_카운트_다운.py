# 카운트 다운
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181899
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 10:09:33

def solution(start_num, end_num):
    start = []
    for i in range(start_num,end_num-1,-1):
        start.append(i)
    return start
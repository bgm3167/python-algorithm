# 1로 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181880
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 29. 11:19:14

def solution(num_list):
    num = 0
    for i in num_list:
        while i > 1:
            if i % 2 == 0:
                i /= 2
            else:
                i = (i-1)/2
            num += 1
    return num
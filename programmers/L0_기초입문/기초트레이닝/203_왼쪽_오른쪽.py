# 왼쪽 오른쪽
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181890
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 31. 09:42:41

def solution(str_list):
    ans = []
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            return str_list[:i]
        elif str_list[i] == 'r':
            return str_list[i+1:]
    return []
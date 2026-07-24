# 꼬리 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181841
# 알고리즘: 조건문 활용
# 작성자: 백관민
# 작성일: 2026. 07. 24. 11:47:04

def solution(str_list, ex):
    ans = ''
    for i in str_list:
        if not ex in i:            
            ans += i
    return ans
        
    
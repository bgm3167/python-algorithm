# 문자 반복 출력하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120825
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 20. 11:22:32

def solution(my_string, n):
    return ''.join(char * n for char in my_string)
 
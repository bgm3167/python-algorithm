# 두 수의 연산값 비교하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181938
# 알고리즘: 연산
# 작성자: 백관민
# 작성일: 2026. 07. 24. 10:39:07

def solution(a, b):
    c = str(a)
    d = str(b)
    if int(c+d) < 2 * a * b: 
        return 2 * a * b
    else:
        return int(c+d)
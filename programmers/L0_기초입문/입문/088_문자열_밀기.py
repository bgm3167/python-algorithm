# 문자열 밀기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120921
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 23. 10:02:38

def solution(A, B):
    for i in range(len(A)):
        if A == B:
            return i
        A = A[-1] + A[:-1]   # 오른쪽으로 한 칸 회전
    return -1
        
 
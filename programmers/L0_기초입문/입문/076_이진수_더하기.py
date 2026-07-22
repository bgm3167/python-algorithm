# 이진수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120885
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 22. 09:48:23

def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]
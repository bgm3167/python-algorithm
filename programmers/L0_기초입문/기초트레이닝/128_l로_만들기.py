# l로 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181834
# 알고리즘: 반복문 활용
# 작성자: 백관민
# 작성일: 2026. 07. 24. 11:30:40

def solution(myString):
    return ''.join('l' if ch < 'l' 
                   else ch for ch in myString)
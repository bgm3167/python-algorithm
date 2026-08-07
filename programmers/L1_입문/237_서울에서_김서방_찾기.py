# 서울에서 김서방 찾기
# 프로그래머스 L1 (입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12919
# 알고리즘: 배열, 탐색
# 작성자: 백관민
# 작성일: 2026. 08. 07. 13:56:22

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return f"김서방은 {i}에 있다"
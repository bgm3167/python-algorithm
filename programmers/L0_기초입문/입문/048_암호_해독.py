# 암호 해독
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120892
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 09:20:37

def solution(cipher, code):
    answer = ''
    for i in range(0,len(cipher)):
        if (i+1) % code == 0:
            answer += cipher[i]
    return answer
        
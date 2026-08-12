# 시저 암호
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12926
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 08. 12. 09:11:06

def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += ' '
        elif i.isupper():
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        else:
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
    
    return answer
# 이상한 문자 만들기
# 프로그래머스 L2 (기초)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12930
# 알고리즘: 문자열
# 작성자: 백관민
# 작성일: 2026. 08. 10. 14:22:27

def solution(s):
    answer = ''
    index = 0

    for i in s:
        if i == ' ':
            answer += ' '
            index = 0
        else:
            if index % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
            index += 1

    return answer
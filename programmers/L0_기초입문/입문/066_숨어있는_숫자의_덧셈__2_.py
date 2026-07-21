# 숨어있는 숫자의 덧셈 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120864
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 11:20:08

def solution(my_string):
    answer = 0
    number = ''

    for char in my_string:
        if char.isdigit():
            number += char
        else:
            if number:
                answer += int(number)
                number = ''

    # 문자열이 숫자로 끝나는 경우
    if number:
        answer += int(number)

    return answer
# 인덱스 바꾸기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120895
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 21. 09:25:59

def solution(my_string, num1, num2):
    answer = ''
    for i in range(0,len(my_string)):
        if i == num1:
            answer += my_string[num2]
        elif i == num2:
            answer += my_string[num1]
        else:
            answer += my_string[i]
    return answer
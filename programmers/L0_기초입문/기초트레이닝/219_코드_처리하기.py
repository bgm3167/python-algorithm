# 코드 처리하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181932
# 알고리즘: 조건문
# 작성자: 백관민
# 작성일: 2026. 08. 06. 10:14:22

def solution(code):
    answer = ''
    mode = -1
    for i in range(len(code)):
        if code[i] == '1':
            mode *= -1
        else:
            if mode == -1:
                if i%2 == 0:
                    answer += code[i]
            else:
                if i%2 == 1:
                    answer += code[i]
                    
    return answer if answer else 'EMPTY'
                    
                    
            
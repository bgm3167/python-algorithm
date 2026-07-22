# 문자열 계산하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120902
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 22. 09:29:38

def solution(my_string):
    my_string = my_string.replace(" ", "")
    my_string = my_string.replace("-", "+-")
    return sum(map(int, my_string.split("+")))
        
            
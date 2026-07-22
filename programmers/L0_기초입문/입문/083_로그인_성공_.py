# 로그인 성공?
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120883
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 22. 10:51:19

def solution(id_pw, db):
    for i in db:
        if id_pw[0] == i[0]:
            if id_pw[1] == i[1]:
                return "login"
            return "wrong pw"
    return "fail"
# 다항식 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120863
# 알고리즘: 기초
# 작성자: 백관민
# 작성일: 2026. 07. 28. 11:24:24

def solution(polynomial):
    x_sum = 0       # x항의 계수 합
    num_sum = 0     # 상수항의 합

    for term in polynomial.split(" + "):
        if "x" in term:
            if term == "x":
                x_sum += 1
            else:
                x_sum += int(term[:-1])
        else:
            num_sum += int(term)

    answer = []

    # x항 만들기
    if x_sum == 1:
        answer.append("x")
    elif x_sum > 1:
        answer.append(f"{x_sum}x")

    # 상수항 만들기
    if num_sum > 0:
        answer.append(str(num_sum))

    return " + ".join(answer)
            
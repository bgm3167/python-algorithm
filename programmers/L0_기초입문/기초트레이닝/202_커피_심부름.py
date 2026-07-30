# 커피 심부름
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181837
# 알고리즘: 조건문 활용
# 작성자: 백관민
# 작성일: 2026. 07. 31. 08:59:09

def solution(order):
    ame = ["iceamericano", "americanoice",
          "hotamericano", "americanohot",
          "americano","anything"]
    ans = 0
    for i in order:
        if i in ame:
            ans += 4500
        else:
            ans += 5000
    return ans
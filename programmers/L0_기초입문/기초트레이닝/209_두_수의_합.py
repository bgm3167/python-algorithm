# 두 수의 합
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181846
# 알고리즘: 함수(메서드)
# 작성자: 백관민
# 작성일: 2026. 07. 31. 10:18:21

def solution(a, b):
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    answer = []

    while i >= 0 or j >= 0 or carry:
        num_a = int(a[i]) if i >= 0 else 0
        num_b = int(b[j]) if j >= 0 else 0

        total = num_a + num_b + carry

        answer.append(str(total % 10))
        carry = total // 10

        i -= 1
        j -= 1

    return ''.join(answer[::-1])
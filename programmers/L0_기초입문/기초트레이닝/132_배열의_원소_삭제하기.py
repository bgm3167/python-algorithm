# 배열의 원소 삭제하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181844
# 알고리즘: 조건문 활용
# 작성자: 백관민
# 작성일: 2026. 07. 24. 11:40:53

def solution(arr, delete_list):
    return [i for i in arr if i not in delete_list]
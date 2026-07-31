# 조건에 맞게 수열 변환하기 2
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/181881
# 알고리즘: 리스트(배열)
# 작성자: 백관민
# 작성일: 2026. 07. 31. 09:36:42

def solution(arr):
    count = 0

    while True:
        new_arr = []

        for i in arr:
            if i >= 50 and i % 2 == 0:
                new_arr.append(i // 2)
            elif i < 50 and i % 2 == 1:
                new_arr.append(i * 2 + 1)
            else:
                new_arr.append(i)

        # 변환 전후가 같으면 종료
        if new_arr == arr:
            return count

        arr = new_arr
        count += 1
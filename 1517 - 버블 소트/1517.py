import sys
import math

# Inversion Count 문제
# 머지소트를 이용해서 풀 수도 있지만 세그먼트 트리 연습을 위해 세그트리+좌표압축으로 풀었음


def get_new_tree(count):
    p = math.ceil(math.log2(count))
    return [0 for _ in range(2 ** (p+1))]


def update_tree(start, end, current, target):
    if start == end:
        tree[current] += 1
        return 1

    mid = (start+end) // 2
    if mid >= target:
        tree[current] += update_tree(start, mid, current * 2, target)
    else:
        tree[current] += update_tree(mid+1, end, current * 2 + 1, target)
    return 1


def query(start, end, current, left, right):
    # 구간 밖으로 벗어난 경우
    if left > end or right < start:
        return 0

    # 찾는 구간이 맞다면 구간합 리턴
    if left <= start and end <= right:
        return tree[current]

    mid = (start+end) // 2
    sub_sum = query(start, mid, current * 2, left, right) + query(mid + 1, end, current * 2 + 1, left, right)

    return sub_sum


input_count = int(input())
inputs = list(map(int, sys.stdin.readline().split()))

sorted_inputs = sorted(inputs)
compressed = {v: k+1 for k, v in enumerate(sorted_inputs)}
inputs = [compressed[elem] for elem in inputs]

answer = 0

tree = get_new_tree(input_count)

for index in inputs:
    # 세그먼트 트리에 순서대로 값을 하나씩 넣고,
    update_tree(1, input_count, 1, index)
    # 여태까지 들어간 수 중에 자기보다 큰 게 몇 개 있는지 쿼리해서 더한다
    answer += query(1, input_count, 1, index + 1, input_count)

print(answer)
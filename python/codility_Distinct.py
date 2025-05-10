def solution(A):
    dict = {}
    for i in A:
        if dict.get(i):      # 딕셔너리에 값이 있다면 (key가 i인 값의 value가 존재한다면)
            dict[i] += 1       # 기존 value 값에 1 더하기
        else:
            dict[i] = 1
    return len(dict)



def merge_sort(arr):
    # 리스트의 크기가 1 이하인 경우, 더 이상 나누지 않고 그대로 반환
    if len(arr) <= 1:
        return arr

    # 배열을 두 개의 부분으로 나눔
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    print("left_half : ", left_half)
    print("right_half : ", right_half)

    # 재귀적으로 왼쪽과 오른쪽 부분 정렬
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # 두 부분을 병합
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    print(">>>>>>Call merge<<<<<<<")

    # 양쪽 리스트에서 하나씩 꺼내 비교하면서 정렬
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 한 쪽 리스트에 남은 원소들을 result에 추가
    result.extend(left[i:])
    result.extend(right[j:])
    print("result : ", result)
    return result

# 예시 배열
arr = [1, 11 ,9, 5, 3, 8, 4, 2, 7, 12, 2, 6]
sorted_arr = merge_sort(arr)
print(f"정렬된 배열: {sorted_arr}")

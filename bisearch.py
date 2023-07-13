def bisearch(arr: list, target) -> int:
    left, right = 0, len(arr) - 1
    
    while(left <= right):
        mid = left + (right - left) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] == target:
            return mid
    
    return -1

def bisearchL(arr: list, target) -> int:
    left, right = 0, len(arr) - 1
    
    while(left <= right):
        mid = left + (right - left) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] == target:
            right = mid - 1
    
    if left >= len(arr):
        return -1
    return left if arr[left]==target else -1

def bisearchR(arr: list, target) -> int:
    left, right = 0, len(arr) - 1
    
    while(left <= right):
        mid = left + (right - left) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] == target:
            left = mid + 1
    
    if right < 0:
        return -1
    return right if arr[right]==target else -1

if __name__=='__main__':
    a = [1,3,4,4,4,4,5,7,9]
    target = 4
    print(bisearch(a, target), bisearchL(a, target), bisearchR(a, target))
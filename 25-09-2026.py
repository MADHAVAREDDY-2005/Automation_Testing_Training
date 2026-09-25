# 1. Student Attendance Analysis
# Find the longest continuous sub-list containing only unique IDs.
def longest_unique_sequence(lst):
        maxlen=0
        start=0
        seen=set()
        if not lst:
                return 0
        for i in range(len(lst)):
                while lst[i] in seen:
                        seen.remove(lst[start])
                        start+=1
                seen.add(lst[i])
                maxlen=max(maxlen,i-start+1)
        return maxlen

lst=[1, 2, 3, 2, 4, 5, 6, 3, 7]
result = longest_unique_sequence(lst)
print(result)


# 2. Online Shopping Price Analysis       
# Find the continuous sub-list with the largest sum.
def max_discount(discounts):
        curr_sum=discounts[0]
        max_sum=discounts[0]

        for i in range(1,len(discounts)):
                curr_sum=max(discounts[i],curr_sum+discounts[i])
                max_sum=max(max_sum,curr_sum)
        return max_sum

lst=[2, -3, 5, 4, -2]
print(max_discount(lst))


# 3. Rainwater Collection System
# Calculate total water trapped between bars.
def trap(h):
    l, r = 0, len(h) - 1
    lm = rm = water = 0
    while l < r:
        if h[l] <= h[r]:
            lm = max(lm, h[l])
            water += lm - h[l]
            l += 1
        else:
            rm = max(rm, h[r])
            water += rm - h[r]
            r -= 1
    return water
h = list(map(int, input().split()))
print(trap(h))


# 4. Employee Performance Analysis
# Find the continuous sub-list with the maximum sum.
def max_performance(a):
    curr = best = a[0]

    for i in range(1, len(a)):
        curr = max(a[i], curr + a[i])
        best = max(best, curr)

    return best

a = list(map(int, input().split()))
print(max_performance(a))


# 5. Product Sales Analysis
# Find the continuous sub-list with the maximum product.
def max_product(a):
    curr_max = curr_min = result = a[0]
    for x in a[1:]:
        curr_max, curr_min = max(x, x*curr_max, x*curr_min), \
                             min(x, x*curr_max, x*curr_min)
        result = max(result, curr_max)
    return result
a = list(map(int, input().split()))
print(max_product(a))


# 6. Customer Purchase History
# Find the longest continuous sequence containing no duplicate product IDs.
def longest_unique_sequence(lst):
    maxlen = 0
    start = 0
    seen = set()

    if not lst:
        return 0

    for i in range(len(lst)):
        while lst[i] in seen:
            seen.remove(lst[start])
            start += 1

        seen.add(lst[i])
        maxlen = max(maxlen, i - start + 1)

    return maxlen

lst = list(map(int, input().split()))
print(longest_unique_sequence(lst))


# 7. Bank Transaction Analysis
# Count how many continuous sub-lists have a sum exactly equal to the target.
def count_subarrays(a, target):
    count = 0
    curr = 0
    seen = {0: 1}
    for x in a:
        curr += x
        if curr - target in seen:
            count += seen[curr - target]
        seen[curr] = seen.get(curr, 0) + 1
    return count
a = list(map(int, input().split()))
target = int(input())
print(count_subarrays(a, target))


# 8. Employee Skill Grouping
# Group strings together when they are made from the same characters, regardless of their order.
def group_strings(a):
    groups = {}
    for word in a:
        key = ''.join(sorted(word))
        groups.setdefault(key, []).append(word)

    return list(groups.values())
a = input().split()
print(group_strings(a))


# 9. Network Packet Analysis
# find the longest sequence of consecutive numerical values.
def longest_consecutive_sequence(a):
    nums = set(a)
    maxlen = 0
    for x in nums:
        if x - 1 not in nums:
            curr = x
            length = 1

            while curr + 1 in nums:
                curr += 1
                length += 1

            maxlen = max(maxlen, length)
    return maxlen
a = list(map(int, input().split()))
print(longest_consecutive_sequence(a))


# 10. Hospital Appointment Scheduling
# Combine overlapping time intervals so that the final list contains no overlapping intervals.
def merge_intervals(intervals):
    intervals.sort()
    result = []
    for start, end in intervals:
        if not result or start > result[-1][1]:
            result.append([start, end])
        else:
            result[-1][1] = max(result[-1][1], end)

    return result
intervals = [[1, 3], [2, 5], [7, 9], [8, 10]]
print(merge_intervals(intervals))

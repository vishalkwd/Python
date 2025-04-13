nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m, n = 3, 3


if m>0 and n>0:
    a = nums1[:m]
    b = nums2[:n]
    a.extend(b)
    nums1 = sorted(a)
print(nums1)
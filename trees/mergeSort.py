
#haven't validated yet...
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        res = []
        counter1 = 0
        counter2 = 0
        while counter1 < m or counter2 < n:
            if nums1[counter1] < nums2[counter2]:
                res.append(nums1[counter1])
                counter1 += 1
            if nums2[counter2] < nums1[counter1]:
                res.append(nums2[counter2])
                
        if counter1 > counter2:
            res.append(nums2[counter2: n])
        if counter2 > counter1:
            res.append(nums1[counter1: m])
        return res
            
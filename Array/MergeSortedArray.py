class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        Newnums1 = nums1[0:m].copy()
        Newnums2 = nums2[0:n]
        for i in range(m + n):
            if len(Newnums1) == 0:
                nums1[i:m+n] = Newnums2
                break
            elif len(Newnums2) == 0:
                nums1[i:m+n] = Newnums1
                break
            else:
                if Newnums1[0] <= Newnums2[0]:
                    nums1[i] = Newnums1.pop(0)
                else:
                    nums1[i] = Newnums2.pop(0)
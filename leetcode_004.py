class Solution:
    def min(self, a, b):
        return a if a<b else b
    def max(self, a, b):
        return a if a>b else b
    def findMedian(self, nums):
        size = len(nums)
        if size%2 == 1:
            return nums[size//2]
        return (nums[size//2-1]+nums[size//2])/2
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        totalLen = len(nums1)+len(nums2)

        if nums1 == []:
            return self.findMedian(nums2)/1.0
        if nums1[-1] <= nums2[0]:
            return self.findMedian(nums1+nums2)/1.0
        if nums1[0] > nums2[-1]:
            return self.findMedian(nums2+nums1)/1.0

        left = 0
        right = len(nums1)-1

        pos = -1
        while left <= right:
            mid = (left+right)//2
            if mid != -1:
                maxL = self.max(nums1[mid], nums2[totalLen//2-(mid+1)-1])
            else:
                maxL = nums2[totalLen//2-(mid+1)-1]
            if mid+1 < len(nums1):
                minR = self.min(nums1[mid+1], nums2[totalLen//2-(mid+1)])
            else:
                minR = nums2[totalLen//2-(mid+1)]
            if maxL <= minR:
                pos = mid
                break
            if maxL == nums1[mid]:
                right = mid-1
                if right == -1: left = -1
            else:
                left = mid+1

        if totalLen%2 == 0:
            if pos == -1:
                maxL = nums2[totalLen//2-(pos+1)-1]
            else:
                maxL =self.max(nums1[pos], nums2[totalLen//2-(pos+1)-1])
            if pos+1 >= len(nums1):
                minR = nums2[totalLen//2-(pos+1)]
            else:
                # if pos == -1:
                #     minR = nums2[totalLen//2-(pos+1)]
                # else:
                minR = self.min(nums1[pos+1], nums2[totalLen//2-(pos+1)])
            return (maxL+minR)/2
        else:
            if pos+1 >= len(nums1):
                return nums2[totalLen//2-(pos+1)]/1.0
            else:
                return self.min(nums1[pos+1], nums2[totalLen//2-(pos+1)])/1.0


if __name__ == '__main__':
    test = Solution()
    nums1 = [3]
    nums2 = [1,2,4]
    print(test.findMedianSortedArrays(nums1, nums2))



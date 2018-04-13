class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2147483648 or x > 2147483647 or x == 0:
            return 0
        ans = ''
        if x < 0:
            s = str(-x)
            for ch in s:
                ans = ch+ans
            i = 0
            while i < len(ans) and ans[i]=='0': i += 1
            ans = '-'+ans[i:]
        else:
            s = str(x)
            for ch in s:
                ans = ch+ans
            i = 0
            while i < len(ans) and ans[i] == '0': i += 1
            ans = ans[i:]
        ans = int(ans)
        if ans < -2147483648 or ans > 2147483647: return 0
        return ans

if __name__ == '__main__':
    test = Solution()
    x = 1534236469
    print(test.reverse(x))
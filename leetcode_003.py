class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ''
        ans = ''
        for ch in s:
            if self.is_ok(sub, ch):
                sub += ch
            else:
                if len(sub)>len(ans):
                    ans = sub
                index = sub.find(ch)
                sub = sub[index+1:]+ch
        if len(sub) > len(ans):
            ans = sub
        return len(ans)

    def is_ok(self, s, ch):
        if s == '': return True
        if ch in s: return False
        else: return True

if __name__ == '__main__':
    s = 'abcabcbb'
    s = 'bbbbb'
    s = 'pwwkew'
    s = 'abcbbabcd'
    test = Solution()
    print('ANS:'+test.lengthOfLongestSubstring(s))


# s = 'abcdef'
# print(s.find('a'))
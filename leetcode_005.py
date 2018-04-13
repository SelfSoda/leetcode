class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        for i in range(0, len(s)):
            start = i
            end = i
            while s[start] == s[end]:
                if len(ans) < len(s[start:end+1]):
                    ans = s[start:end+1]
                if start-1 in range(0, len(s)) and end+1 in range(0, len(s)):
                    if s[start-1] == s[end+1]:
                        start -= 1
                        end += 1
                    else: break
                else: break

            start = i
            if i+1 >= len(s): continue
            end = i+1
            while s[start] == s[end]:
                if len(ans) < len(s[start:end+1]):
                    ans = s[start:end+1]
                if start-1 in range(0,len(s)) and end+1 in range(0,len(s)):
                    if s[start-1] == s[end+1]:
                        start -= 1
                        end += 1
                    else: break
                else: break
        return ans

    def manacher(self, s):
        ans = ''
        s = '$'+'$'.join(s)+'$'
        r = [0]*len(s)
        maxR , pos = 0, 0
        for i in range(len(s)):
            if i < maxR:
                r[i] = min(r[pos-(i-pos)], maxR-i)
            else:
                r[i] = 1
            while i-r[i]>=0 and i+r[i]<len(s) and s[i-r[i]]==s[i+r[i]]:
                r[i] += 1
            if r[i]+i-1>maxR:
                maxR = r[i]+i-1
                pos = i
            ans = s[i-r[i]+1:i+r[i]-1] if len(ans) < len(s[i-r[i]+1:i+r[i]-1]) else ans
        return ans.replace('$','')


if __name__ == '__main__':
    test = Solution()
    s = 'ababa'
    print(test.longestPalindrome(s))
    print(test.manacher(s))

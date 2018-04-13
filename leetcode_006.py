class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = [['$'] for i in range(numRows)]
        row, dir = 0, 'down'
        for ch in s:
            ans[row].append(ch)
            if dir == 'down':
                if row+1 > numRows-1:
                    row, dir = row-1, 'up'
                else:
                    row = row+1
            elif dir == 'up':
                if row-1 < 0:
                    row, dir= row+1, 'down'
                else:
                    row = row-1
        return ''.join([''.join(row[1:]) for row in ans])

if __name__ == '__main__':
    test = Solution()
    s = 'ABCDEFG'
    num = 1
    print(test.convert(s, num))
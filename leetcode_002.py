# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.convertToInt(l1)
        num2 = self.convertToInt(l2)
        s = self.convertToListNode(num1+num2)
        ans = []
        while s != None:
            ans.append(s.val)
            s = s.next
        return ans

    def convertToInt(self, l):
        now = l
        base = 1
        result = 0
        while now != None:
            result += base * now.val
            base = base * 10
            now = now.next
        return result

    def convertToListNode(self, num):
        if num == 0: return ListNode(0)
        base = 10
        pre = None
        head = None
        while num != 0:
            now = ListNode(num % base)
            if pre == None:
                head = now
            else:
                pre.next = now
            pre = now
            num = num // base
        return head

if __name__ == "__main__":
    test = Solution
    x = ListNode(2)
    y = ListNode(4)
    z = ListNode(0)
    x.next = y
    y.next = z
    x1 = ListNode(5)
    y1 = ListNode(6)
    z1 = ListNode(0)
    x1.next = y1
    y1.next = z1

    print(test.convertToInt(test, x))
    # ans = test.convertToListNode(test, 807)
    # print(ans)
    print(test.addTwoNumbers(test, z, z1))
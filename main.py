class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        #Create a dummy node
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            #Get the values from the current node if is available
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            #Let's calculate the sum
            total = val1 + val2 + carry
            carry = total // 10 
            digit = total % 10 # Store all the result digits 1 by 1

            #Create new node for the digit and move to the next digit
            current.next = ListNode(digit)
            current = current.next

            #Let's move to the next nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

solution = Solution()
l1 = create_linked_list([2,4,3])
l2 = create_linked_list([5,6,4])
result = solution.addTwoNumbers(l1, l2)

while result:
    print(result.val)
    result = result.next

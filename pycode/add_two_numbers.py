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
        l1_value = self.get_node_value(l1)
        l2_value = self.get_node_value(l2)
        result =  self.trans_value_to_node(l1_value + l2_value)
        print(result)
        return result

    def get_node_value(self, node, value = 0, count = 0):
        value += node.val * pow(10, count)
        if node.next != None:
            return self.get_node_value(node.next, value, count + 1)
        else:
            return value
    
    def trans_value_to_node(self, value):
        result_node = ListNode(value % 10)
        if value >= 10:
            result_node.next = self.trans_value_to_node(value // 10)
        return result_node
            

sol = Solution()
# (2 -> 4 -> 3) + (5 -> 6 -> 4)
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
result = sol.addTwoNumbers(l1, l2)
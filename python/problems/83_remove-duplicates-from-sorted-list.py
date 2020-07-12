"""
    83_remove-duplicates-from-sorted-list
    ~~~

    https://leetcode.com/problems/remove-duplicates-from-sorted-list/

    :author: dilless(Huangbo)
    :date: 2020/7/12
"""
import shutil
from copy import copy

from data_structures.list_node import ListNode
from utils.linked_list_util import LinkedListUtil


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur_node = head
        while cur_node and cur_node.next:
            if cur_node.val == cur_node.next.val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next

        return head


def main(values=(1, 1, 2, 3, 3)):
    origin = LinkedListUtil.create_linked_list(values)
    correct = LinkedListUtil.create_linked_list(list(set(values)))
    ans = Solution().deleteDuplicates(copy(origin))
    r = LinkedListUtil.is_equal(ans, correct)

    print('[Origin]: ', end='')
    LinkedListUtil.print_linked_list(origin)
    print('[Answer]: ', end='')
    LinkedListUtil.print_linked_list(ans)
    print()

    if r:
        print('Succeed!')
    else:
        print('Failed!')


if __name__ == '__main__':
    main([1, 1, 2, 3, 4, 4, 5, 7, 7])
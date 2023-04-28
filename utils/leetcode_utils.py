from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_input_list(input_arr: [], pos: int) -> Optional[ListNode]:
    head = None
    current_node = None
    for n in input_arr:
        if head is None:
            head = ListNode(n)
            current_node = head
            continue
        current_node.next = ListNode(n)
        current_node = current_node.next
    return add_list_cycle(head, pos)


def add_list_cycle(head: Optional[ListNode], pos: int) -> Optional[ListNode]:
    if pos == -1:
        return head
    next_node = head
    cycle_node = None
    i = 0
    while next_node.next is not None:
        if i == pos:
            cycle_node = next_node
        next_node = next_node.next
        i += 1
    tail = next_node
    tail.next = cycle_node
    return head


def get_linked_list_cycle_node(head: Optional[ListNode], pos: int) -> Optional[ListNode]:
    if pos == -1:
        return None
    next_node = head
    i = 0
    while next_node.next is not None:
        if i == pos:
            return next_node
        next_node = next_node.next
        i += 1
    return head

def compare_linked_list(head1, head2):
    arr1 = []
    arr2 = []
    while head1.next:
        arr1.append(head1.data)
        head1 = head1.next
    while head2.next:
        arr2.append(head2.data)
        head2 = head2.next

    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True
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

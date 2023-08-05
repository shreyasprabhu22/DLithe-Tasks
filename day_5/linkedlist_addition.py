class ListNode:
    def __init__(self, data=0):
        self.data = data
        self.next = None

def add_linked_lists(head1, head2):
    result = ListNode()
    current = result
    carry = 0

    while head1 or head2 or carry:
        sum_val = carry

        if head1:
            sum_val += head1.data
            head1 = head1.next
        if head2:
            sum_val += head2.data
            head2 = head2.next

        carry = sum_val // 10
        sum_val = sum_val % 10

        current.next = ListNode(sum_val)
        current = current.next

    return result.next

def print_linked_list(head):
    current = head
    while current:
        print(current.data, "-> ", end="")
        current = current.next
    print("None")

def main():
    # Helper function to create a linked list from a list of integers
    def create_linked_list(nums):
        head = ListNode()
        current = head
        for num in nums:
            current.next = ListNode(num)
            current = current.next
        return head.next

    # Test case 1
    nums1 = [2, 4, 3]  # Representing number 342
    nums2 = [5, 6, 4]  # Representing number 465
    head1 = create_linked_list(nums1)
    head2 = create_linked_list(nums2)

    result = add_linked_lists(head1, head2)

    # Printing the sum of linked lists
    print("Sum of Linked Lists:")
    print_linked_list(result)

if __name__ == "__main__":
    main()

"""
File: linked_list_prepend_append_in_between.py
Name: Shane Liu
-------------------------
This file shows 3 main operations on manipulating a linked list:
(1)Prepend
(2)Append
(3)In between
"""


class ListNode:
	def __init__(self, data, pointer):
		self.val = data
		self.next = pointer


def main():
	# Construct linked_list
	linked_list = None	
	linked_list = ListNode(('A', 3), None)
	linked_list.next = ListNode(('B', 5), None)
	linked_list.next.next = ListNode(('C', 7), None)
	print("Original linked_list: ")
	traversal(linked_list)

	# (1)Prepend
	new_node = ListNode(('Z', 0), None)
	print("After prepending ('Z', 0): ")
	new_node.next = linked_list
	linked_list = new_node
	traversal(linked_list)

	# (2)Append
	new_node = ListNode(('D', 9), None)
	print("After appending ('D', 9): ")
	cur = linked_list
	while cur.next is not None:
		cur = cur.next
	cur.next = new_node
	traversal(linked_list)

	# (3)In between 
	new_node = ListNode(('X', 5), None)
	print("After inserting ('X', 5): ")
	cur = linked_list
	while cur.next is not None:
		if cur.val[1] <= new_node.val[1] < cur.next.val[1]:
			new_node.next = cur.next
			cur.next = new_node
			break
		else:
			cur = cur.next
	traversal(linked_list)
	

def traversal(linked_list):
	"""
	:param linked_list: ListNode, holding the first ListNode object as the start of priority queue.		
	This function prints out each val of a linked list
	"""
	cur = linked_list
	while cur is not None:
		print(cur.val)
		cur = cur.next


if __name__ == '__main__':
	main()

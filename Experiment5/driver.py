from linkedlist_ops import LinkedList
from linkedlist_ops import SampleLinkedList
from stack_app import in_pre, post_eval
mylist = SampleLinkedList()

mylist.sort()
print(mylist.add_list())
mylist.print_ll()

print(in_pre("( A - B / C ) * ( A / K - L )"))
print(post_eval("1 2 3 + -"))
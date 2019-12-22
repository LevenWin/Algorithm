# -*- coding: UTF-8 -*-
import math
from tree import Tree

# ? 代表none， ！代表节点的结束
def encode(tree, s):
    if tree == None:
        return s + "?!"
    s += (str(tree.value) + "!")
    s = encode(tree.left, s)
    s = encode(tree.right, s)
    return s
def decode(s):
    real_s = s["s"]
    if len(real_s) == 0:
        return None
    s_list = real_s.split("!")
    head_value = s_list[0]
    s["s"] = "!".join(s_list[1:])
    if head_value == "?":
        return None
    else:
        head_node = Tree(int(head_value))
        head_node.left = decode(s)
        head_node.right = decode(s)
        return head_node
    
if __name__ == "__main__":
    tree = Tree(0).simpleTree()
    s = encode(tree, "") # 1!2!4!?!?!5!?!?!3!?!6!?!?!
    t = decode({"s":s})
    print(s,t)


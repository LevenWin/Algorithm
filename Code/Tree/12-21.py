# -*- coding: UTF-8 -*-
import math
from tree import Tree

class PrettyTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = 0
        self.offset_x = 0

def initPrettyTree(t, pt, level, offset_x):
    if t == None:
        return
    pt.value = t.value
    pt.level = level
    pt.offset_x = offset_x
    if t.left:
        pt.left = PrettyTreeNode(0)
        initPrettyTree(t.left, pt.left, level + 1, offset_x - 1)
    if t.right:
        pt.right = PrettyTreeNode(0)
        initPrettyTree(t.right, pt.right, level + 1, offset_x + 1)
def offsetPretteTree(pt):
    if pt == None:
        return
    offsetPretteTree(pt.left)
    offsetPretteTree(pt.right)
    result = {
        "left":{
            "left":{
                "node":None,
                "offset":0
            },
            "right":{
                "node":None,
                "offset":0
            }
        },
        "right":{
            "left":{
                "node":None,
                "offset":0
            },
            "right":{
                "node":None,
                "offset":0
            }
        }
    }
    tree_offset_attr(pt, 0, False, result, 0)
    space = (result['left']['right']['offset'] + result['right']['left']['offset']) * 5
    
    if pt.left != None and pt.right != None:
        update_sub(pt.left, -space/2)
        update_sub(pt.right, space/2)

def update_sub(pt, offset):
    if pt == None:
        return 
    pt.offset_x += offset
    update_sub(pt.left, offset)
    update_sub(pt.right, offset)

def tree_offset_attr(t, center_offset, is_left,result, level):
    if t == None:
        return
    if is_left:
        if result['left']['left']['offset'] <= center_offset:
            result['left']['left']['offset'] = center_offset
            result['left']['left']['node'] = t
        if result['left']['right']['offset'] >= center_offset:
            result['left']['right']['offset'] = center_offset
            result['left']['right']['node'] = t
    else:
        if result['right']['left']['offset'] <= center_offset:
            result['right']['left']['offset'] = center_offset
            result['right']['left']['node'] = t
        if result['right']['right']['offset'] >= center_offset:
            result['right']['right']['offset'] = center_offset
            result['right']['right']['node'] = t
    offset = 2
    if level == 0:
        tree_offset_attr(t.left, center_offset + offset, True, result, level + offset)
        tree_offset_attr(t.right, center_offset - offset, False, result, level + offset)
    else:
        tree_offset_attr(t.left, center_offset + offset, is_left, result, level + offset)
        tree_offset_attr(t.right, center_offset - offset, is_left, result, level + offset)

        
   

def tree_height(pt, config):
    if pt == None:
        return 
    if config['level'] < pt.level:
        config['level'] = pt.level
    if config["left"] > pt.offset_x:
        config["left"] = pt.offset_x
    if config["right"] < pt.offset_x:
        config["right"] = pt.offset_x
    tree_height(pt.left, config)
    tree_height(pt.right, config)

def tree_to_arr(t, list):
    if t == None:
        return list
    list.append(t)
    tree_to_arr(t.left, list)
    tree_to_arr(t.right, list)
    return list

def _printTree(trees, config):
    offset = config['offset']
    scale = config['scale']
    level = config['level']
    level_nodes = []
    cmp = lambda node: node.level
    for i in range(1, level+1):
        same_level = []
        for t in trees:
            if t.level == i:
                same_level.append(t)
        same_level.sort(key=cmp, reverse=True)
        level_nodes.append(same_level)
    total_ps = ""
    for level_node in level_nodes:
        ps = "\n"
        pre = 0
        for node in level_node:
            offset_x = offset + node.offset_x
            tmp =  offset_x
            offset_x -= pre
            pre = tmp
                
            while offset_x >= 0:
                ps += " "
                offset_x -= 1
            ps += str(node.value)
        print(ps)
        total_ps += ps
    # print(total_ps)


def printTree(pt):
    config = {"level":0,"left":0,"right":0}
    tree_height(pt, config)
    config['offset'] = 20
    config['scale'] = 1.5
    trees = tree_to_arr(pt, [])
    _printTree(trees, config)
    




if __name__ == "__main__":
    tree = Tree(0).defatulTree()
    pt = PrettyTreeNode(0)
    initPrettyTree(tree, pt, 1, 0)
    offsetPretteTree(pt)
    printTree(pt)




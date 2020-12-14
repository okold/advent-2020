# Advent of Code 2020 - Day 7
# December 14, 2020
# https://adventofcode.com/2020/day/7
import func

#################################################################
# CLASS DEFINITIONS
# BagNode
# Stores a bag by its name, along with its
# children and parents
class BagNode:
    def __init__(self, init_name):
        self.name = init_name   # string
        self.children = []      # [(BagNode, int)]
        self.parents = []       # [BagNode]
    
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

# A collection of BagNodes which can be traversed
# using strings for ease of use
class BagGraph:
    def __init__(self):
        self.list = []
    
    def insert(self, name):
        if not(self.contains(name)):
            self.list.append(BagNode(name))

    def insert_child(self, parent_name, child_name, child_num):
        if self.contains(parent_name):
            parent_node = self.get(parent_name)
            self.insert(child_name)
            child_node = graph.get(child_name)
            parent_node.children.append((child_node, child_num))
            child_node.parents.append(parent_node)

    def get(self, name):
        for node in self.list:
            if node.name == name:
                return node
        return None

    def contains(self, name):
        if self.get(name) is not None:
            return True
        return False

    # PART 1
    # takes a node name as a string and returns a list of strings
    # of every ancestor of that node
    def get_all_ancestors(self, name):
        node = self.get(name)
        return list(set(self.__get_all_ancestors_recursive(node)))

    # private, recursive portion of the above method
    def __get_all_ancestors_recursive(self, node):
        parent_list = []
        for parent in node.parents:
            parent_list.append(parent.name)
            parent_list = parent_list + self.__get_all_ancestors_recursive(parent)
        return parent_list
    
    # PART 2
    # recursively counts all the bags you'd need
    def count_all_children(self, name):
        node = self.get(name)
        return self.__count_all_children_recursive(node)

    def __count_all_children_recursive(self, node):
        num_children = 0
        if node is not None:
            for child in node.children:
                name = child[0]
                count = int(child[1])
                for i in range(0, count):
                    num_children += 1
                    num_children += self.__count_all_children_recursive(name)
        return num_children

#################################################################
# CREATES THE GRAPH
input = func.file_to_list("07/input")
graph = BagGraph()

for line in input:
    split = line.split(" bags contain ")
    parent_name = split[0]

    # inserts the parent bag, if it's not already in the graph
    graph.insert(parent_name)
    parent_node = graph.get(parent_name)

    if split[1] != "no other bags.":
        child_list = split[1].split(', ')
        for child in child_list:
            word_list = child.split(' ')
            child_num = int(word_list[0])
            child_name = word_list[1] + ' ' + word_list[2]
            graph.insert_child(parent_name, child_name, child_num)


print("PART 1:", len(graph.get_all_ancestors("shiny gold")))
print("PART 2:", graph.count_all_children("shiny gold"))

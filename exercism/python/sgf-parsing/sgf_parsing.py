import re

class SgfTree:
    def __init__(self, properties = None, children = None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if(not isinstance(other, SgfTree)):
            return False
        for k, v in self.properties.items():
            if(k not in other.properties):
                return False
            if(other.properties[k] != v):
                return False
        for k in other.properties.keys():
            if(k not in self.properties):
                return False
        if(len(self.children) != len(other.children)):
            return False
        for a, b in zip(self.children, other.children):
            if(a != b):
                return False
        return True

    def __ne__(self, other):
        return not self == other

def parse(inputstring):
    group_of_nodes_pattern = re.compile(r"\(;(?P<group_of_nodes>.*)\)", re.DOTALL)
    matches = group_of_nodes_pattern.match(inputstring)
    if(matches == None):
        raise ValueError("invalid input")
    group_of_nodes_string = matches.group("group_of_nodes")

    tree = SgfTree()
    if(len(group_of_nodes_string) == 0):
        return tree
    list_of_nodes = group_of_nodes_string.split(";")

    for n, node in enumerate(list_of_nodes):
        key_value_pattern = re.compile(r"(?P<key>[A-Za-z]+)(?P<values>(\[([\w\s]|\\])+\])+)", re.DOTALL)
        for node_info in key_value_pattern.finditer(node):
            key = node_info.group("key")
            value_string = node_info.group("values")
            value_string = value_string[1 : -1]
            value_list = value_string.replace("\\", "").replace("\t", " ").split("][")
            if(not key.isupper() or len(value_list) == 0):
                raise ValueError("Invalid key")
            if(n == 0):
                tree.properties[key] = value_list
            else:
                tree.children.append(SgfTree(properties = {key: value_list}))
                
    if(tree.properties == {}):
        raise ValueError("no properties")

    return tree
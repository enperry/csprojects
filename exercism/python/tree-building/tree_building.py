class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id

class Node:
    def __init__(self, node_id, children = []):
        self.node_id = node_id
        self.children = children

def BuildTree(records):
    if(not records):
        return None
    
    if(not [record.record_id for record in records if record.record_id == 0]):
        raise ValueError("no root record")
    if(not all([record.record_id > record.parent_id or record.record_id == 0 for record in records])):
        raise ValueError("records do not describe a tree")
    if(len(records) != max([record.record_id for record in records]) + 1):
        raise ValueError("missing records")
    if(len([1 for record in records if (record.record_id == 0) and (record.parent_id == 0)]) != 1):
        raise ValueError("root can't have parent")

    root = Node(0, [])
    tier = [root]
        
    while(tier):
        next_tier = []
        for node in tier:
            node.children = [Node(record.record_id, []) for record in records if record.parent_id == node.node_id and record.record_id != 0]
            node.children.sort(key = lambda x : x.node_id)
            next_tier = next_tier + node.children
        tier = next_tier

    return root
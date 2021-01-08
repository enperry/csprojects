def tree_from_traversals(preorder, inorder):
    if(len(preorder) != len(inorder)):
        raise ValueError("Traversals must have the same length.")
    if(len(set(preorder)) != len(preorder) or len(set(inorder)) != len(inorder)):
        raise ValueError("Traversals must be free of duplicates.")
    if(not preorder):
        return {}
    if(len(preorder) == 1):
        return {"v": preorder[0], "l": {}, "r": {}}
    left_inorder = inorder[:inorder.index(preorder[0])]
    right_inorder = inorder[inorder.index(preorder[0]) + 1 : ]
    left_preorder = [x for x in preorder if x in left_inorder]
    right_preorder = [x for x in preorder if x in right_inorder]
    return {"v": preorder[0], "l": tree_from_traversals(left_preorder, left_inorder),"r": tree_from_traversals(right_preorder, right_inorder)}
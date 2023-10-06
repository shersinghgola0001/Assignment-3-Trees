class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def count_subtrees_with_sum(node, target_sum, count):
    if not node:
        return 0
    left_count = count_subtrees_with_sum(node.left, target_sum, count)
    right_count = count_subtrees_with_sum(node.right, target_sum, count)
    subtree_sum = node.value + left_count + right_count
    if subtree_sum == target_sum:
        count[0] += 1
    return subtree_sum
def count_subtrees_with_given_sum(root, target_sum):
    count = [0]  # Using a list to store count so it can be modified within the recursive function
    count_subtrees_with_sum(root, target_sum, count)
    return count[0]
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)
root.right.left = TreeNode(2)
root.right.right = TreeNode(6)
target_sum = 10
result = count_subtrees_with_given_sum(root, target_sum)
print(f"Number of subtrees with sum {target_sum}: {result}")

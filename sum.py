class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_level_sum(root):
    if not root:
        return 0

    max_sum = float("-inf")
    queue = [root]

    while queue:
        level_sum = 0
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.pop(0)
            level_sum += node.value

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        max_sum = max(max_sum, level_sum)

    return max_sum
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(6)
root.right.right.right = TreeNode(7)

result = max_level_sum(root)
print("Maximum level sum:", result)

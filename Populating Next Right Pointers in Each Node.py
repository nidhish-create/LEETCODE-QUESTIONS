class Solution(object):
    def connect(self, root):
        def f(root):
            if root is None:
                return 
            if root.left:
                root.left.next = root.right
            if root.right:
                if root.next:
                    root.right.next = root.next.left
            f(root.left)
            f(root.right)
        f(root)
        return root
        """
        :type root: Node
        :rtype: Node
        """

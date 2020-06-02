# 验证二叉搜索树

# 中等

# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。

# 假设一个二叉搜索树具有如下特征：

# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/validate-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x=None, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.pre = -float('inf') # 标志，指针

        # 中序遍历，得到的为顺序序列
        def inorder(node):
            # 边界条件，如果为空肯定为二叉排序树
            if not node: 
                return True
            # 递归 直到左子树为空 或者 递归过程中
            if not (inorder(node.left) or str(self.pre) >= str(node.val)):
                return False
            self.pre = node.val
            return inorder(node.right)
        return inorder(root)


    def printFromTopToBottom(self, root):
        l = []
        if root is None:
            return l
        queue = []

        queue.append(root)

        while queue:
            node = queue.pop(0)
            l.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return l


def createTree(root, treeList, i):
    """
        :type root: TreeNode
        :type treeList: List[int]
        :type i: int
        :rtype: TreeNode
    """
    if i < len(treeList):
        if treeList[i] is None:
            return None
        else:
            root = TreeNode(treeList[i])
            root.left = createTree(root.left, treeList, i*2 + 1) # 遍历左子树，序号为二叉树规律
            root.right = createTree(root.right, treeList, i*2 + 2) # 遍历右子树
            return root
    return root

testList = [5,1,4,'null','null',3,6]#['12','5','18','2','9','15','19','null','null','null','null','null','17','null'] # [5,1,4,'null','null',3,6]

tree = TreeNode()
test = Solution()

tree = createTree(tree,testList,0)

print(test.printFromTopToBottom(tree))

print(test.isValidBST(tree))
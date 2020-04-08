# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}
# 和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution:
	# 返回构造的TreeNode根节点
	def reConstructBinaryTree(self, pre, tin):
		# write code here
		if len(pre) == 0:
			return None
		if len(pre) == 1:
			return TreeNode(pre[0])
		root = TreeNode(pre[0])  # 前序遍历的第一个为根节点
		pos = tin.index(pre[0])  # 在中序遍历中查找根位置（也就是左子树的元素个数），分为左右子树集合，左为左子树，右为右子树
		root.left = self.reConstructBinaryTree(pre[1:1 + pos], tin[:pos])  # 左子树，的前序遍历的第一个值，为根的左子树节点
		root.right = self.reConstructBinaryTree(pre[pos + 1:], tin[pos + 1:])  # 右子树的前序遍历的第一个值，为根的右子树的节点
		return root#返回的根即为每次层级递归调用的值，由底层构建

array = [1, 2, 3, 4, 5, 6, 7, 7]
print(array.index(3))

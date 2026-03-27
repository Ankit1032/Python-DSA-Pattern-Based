# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        # My solution worked but there is a more cleaner way to do ti
        #My intuition is : I am building all root-to-leaf numbers bottom-up by collecting child paths and prefixing the current node’s value to each path.
        # 1. Each node asks its children: “give me all numbers formed from you to leaves”
        # 2. Then you add your digit in front of each of those numbers
        # 3. If it's a leaf → you start a new number with just that digit

        # if not root:
        #     return 0
        
        # left_num = ""
        # right_num = ""

        # def dfs(root):
        #     if not root:
        #         return []

        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     #leaf node
        #     if left == [] and right == []:
        #         return [str(root.val)]

        #     res = []

        #     #This below code almost worked logical numerical wise but it gave nested lists so used another logic
        #     # Example:  [['1["2[\'48\']", "2[\'49\']"]', "1['25']"], ["1['36']", "1['37']"]]
        #     # if left != []:
        #     #     for i in range(len(left)):
        #     #         left[i] = str(root.val) + str(left[i])
            
        #     # if right != []:
        #     #     for i in range(len(right)):
        #     #         right[i] = str(root.val) + str(right[i])

        #     if left != []:
        #         for num in left:
        #             res.append(str(root.val) + num)
            
        #     if right != []:
        #         for num in right:
        #             res.append(str(root.val) + num)
            
        #     return res
        
        # arr = dfs(root)
        # #print(arr)
        # #root = [4,9,0,5,1]
        # #arr = ['495', '491', '40']

        # sum_arr = 0
        # for i in arr:
        #     sum_arr += int(i)
        
        # return sum_arr
        

        ####################### Solution 2 : Cleaner way #############
        def dfs(node, current):
            if not node:
                return 0

            current = current * 10 + node.val

            # leaf node
            if not node.left and not node.right:
                return current

            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)
            
            

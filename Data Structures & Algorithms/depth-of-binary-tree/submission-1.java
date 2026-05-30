/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxDepth(TreeNode root) {
        return maxDepth(root, 0);
        
    }
    public int maxDepth(TreeNode root, int currDepth){
        if (root == null){
            return currDepth;
        } else {
            currDepth++;
            int lDepth = maxDepth(root.left, currDepth);
            int rDepth = maxDepth(root.right, currDepth);
            return Math.max(lDepth, rDepth);
            // if (lDepth > rDepth){
            //     return lDepth;
            // } 
            // return rDepth;
            
        }
    }
}

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
    public TreeNode invertTree(TreeNode root) {
        
        if (root == null){
            return root;
        } else {
            TreeNode i = root;
            TreeNode left = root.left;
            TreeNode right = root.right;
            i.left = right;
            i.right = left;
            invertTree(left);
            invertTree(right);
            return root;
        }
        
    }
}

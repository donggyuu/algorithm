/**
 * Make basic tree using Linked List
 */

public class TreeNode {

        Object value;
        TreeNode left;
        TreeNode right;

        public TreeNode(Object value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }

        // =========================
        // make sub tree
        // =========================
        public void makeLeftSubTree(TreeNode sub) {
            // want to add values but if already exist
            // then initialize by null
            if (left != null) {
                this.left = null;
            }
            this.left = sub;
        }

        public void makeRightSubTree(TreeNode sub) {
            if (right != null) {
                this.right = null;
            }
            this.right = sub;
        }

        // =========================
        // return sub tree
        // =========================

        public Object getValue() {
            return value;
        }

        public TreeNode getLeftSubTree() {
            return this.left;
        }

        public TreeNode getRightSubTree() {
            return this.right;
        }
}
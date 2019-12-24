public class BasicTree {

    /**
     * Make basic tree by Linked List
     */

    public static void main(String[] args) {

        TreeNode bt1 = new TreeNode(1);
        TreeNode bt2 = new TreeNode(2);
        TreeNode bt3 = new TreeNode(3);
        TreeNode bt4 = new TreeNode("four");

        bt1.makeLeftSubTree(bt2);
        bt1.makeRightSubTree(bt3);
        bt2.makeRightSubTree(bt4);
        //     bt1
        //     / \
        //   bt2  bt3
        //      \
        //      bt4
    }

    static class TreeNode {

        Object data;
        TreeNode left;
        TreeNode right;

        public TreeNode(Object data) {
            this.data = data;
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

        public Object getData() {
            return data;
        }

        public TreeNode getLeftSubTree() {
            return this.left;
        }

        public TreeNode getRightSubTree() {
            return this.right;
        }

    }
}
public class CountingUnivalSubtrees {

    /**
     * ※※※※ Q ※※※※※※※※※※
     * Make method that return the number of unival trees
     * https://www.dailycodingproblem.com/blog/unival-trees/
     *
     * ※※※※ Details ※※※※
     * what is unival trees? (which stands for “universal value”)
     * A unival tree is a tree where all nodes have the same value.
     *
     *   a
     *  / \
     * a   a
     *     /\
     *    a  a
     *        \
     *         A
     * This tree has 3 unival subtrees: the two ‘a’ leaves and the one ‘A’ leaf.
     * The ‘A’ leaf causes all its parents to not be counted as a unival tree.
     *
     *   a
     *  / \
     * c   b
     *     /\
     *    b  b
     *        \
     *         b
     * This tree has 5 unival subtrees: the leaf at ‘c’, and every ‘b’.
     */

    public static void main(String[] args) {

        TreeRoot bt1 = new TreeRoot("a");
        TreeRoot bt2 = new TreeRoot("b");
        TreeRoot bt3 = new TreeRoot("c");
        TreeRoot bt4 = new TreeRoot("d");

        bt1.makeLeftSubTree(bt2);
        bt1.makeRightSubTree(bt3);
        bt2.makeRightSubTree(bt4);

        if (isUnival(bt1, bt1.getValue())) {
            System.out.println("has unival tree");
        } else {
            System.out.println("not unival tree");
        }
    }


    private static boolean isUnival(TreeRoot treeRoot, Object treeValue) {
        return univalHelper(treeRoot, treeValue);
    }

    private static boolean univalHelper(TreeRoot treeRoot, Object treeValue) {

        if (treeRoot == null) {
            return true;
        }

        if (treeRoot.value == treeValue) {
            return univalHelper(treeRoot.left, treeValue)
                    && univalHelper(treeRoot.right, treeValue);
        }

        return false;
    }


    /**
     * sample tree
     */
    static class TreeRoot {

        Object value;
        TreeRoot left;
        TreeRoot right;

        public TreeRoot(Object value) {
            this.value = value;
            this.left = null;
            this.right = null;
        }

        public void makeLeftSubTree(TreeRoot sub) {

            if (left != null) {
                this.left = null;
            }
            this.left = sub;
        }

        public void makeRightSubTree(TreeRoot sub) {
            if (right != null) {
                this.right = null;
            }
            this.right = sub;
        }

        public Object getValue() {
            return value;
        }
        public TreeRoot getLeftSubTree() {
            return this.left;
        }
        public TreeRoot getRightSubTree() {
            return this.right;
        }
    }

}
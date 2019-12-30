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

        TreeNode bt1 = new TreeNode("a");
        TreeNode bt2 = new TreeNode("a");
        TreeNode bt3 = new TreeNode("a");
        TreeNode bt4 = new TreeNode("a");

        bt1.makeLeftSubTree(bt2);
        bt1.makeRightSubTree(bt3);
        bt2.makeRightSubTree(bt4);

        if (isUnival(bt1, bt1.getValue())) {
            System.out.println("has unival tree");
        } else {
            System.out.println("not unival tree");
        }
    }


    private static boolean isUnival(TreeNode treeNode, Object treeValue) {
        return univalHelper(treeNode, treeValue);
    }

    private static boolean univalHelper(TreeNode treeNode, Object treeValue) {

        if (treeNode == null) {
            return true;
        }

        if (treeNode.value == treeValue) {
            return univalHelper(treeNode.left, treeValue)
                    && univalHelper(treeNode.right, treeValue);
        }

        return false;
    }

}
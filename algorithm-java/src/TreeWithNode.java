public class TreeWithNode {

    public static void main(String[] args) {

        Tree<Integer> t = new Tree<Integer>();
        Node n4 = t.createNode(null, 4, null);
        Node n5 = t.createNode(null, 5, null);
        Node n2 = t.createNode(n4, 2, n5);
        Node n3 = t.createNode(null, 3, null);
        Node n1 = t.createNode(n2, 1, n3);

        t.setRoot(n1);
        t.preOrder(t.getRoot());
    }

    /**
     * Node for Tree
     */
    static class Node<T> {

        private T data;
        private Node<T> left;
        private Node<T> right;

        public Node (T data) {
            this.data = data;
        }

    }

    /**
     * Tree 클래스 구현
     */
    static class Tree<T> {

        /**
         * root node 세팅
         */
        public Node<T> root;

        public void setRoot(Node<T> node) {
            this.root = node;
        }

        public Node<T> getRoot() {
            return root;
        }

        /**
         * Node 추가
         */
        public Node<T> createNode(Node<T> left, T data, Node<T> right) {

            Node<T> newNode = new Node<T>(data);
            newNode.left = left;
            newNode.right = right;
            // data는 constructor로 이미 설정

            return newNode;
        }

        /**
         * Tree 순회
         * ** 처음 집어넣을 node는 root Node, 이후 재귀적 순회
         * ** 전위 : root -> left -> right
         */
        public void preOrder(Node<T> node) {
            if (node != null) {
                System.out.println(node.data);
                preOrder(node.left);
                preOrder(node.right);
            }
        }

    }

}

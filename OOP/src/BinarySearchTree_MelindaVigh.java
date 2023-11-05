import java.io.FileWriter;
import java.io.IOException;

public class BinarySearchTree_MelindaVigh implements BSTInterface_MelindaVigh{
    private Node root;

    public BinarySearchTree_MelindaVigh() {
        root = null;
    }

    public void insert(Artwork_MelindaVigh art) {
        root = insertRecursive(root, art);
    }

    private Node insertRecursive(Node root, Artwork_MelindaVigh art) {
        if (root == null) {
            root = new Node(art);
            return root;
        }

        // Compare artworks based on a specific property (e.g., year)
        if (art.getYear() < root.artpiece.getYear())
            root.left = insertRecursive(root.left, art);
        else if (art.getYear() > root.artpiece.getYear())
            root.right = insertRecursive(root.right, art);

        return root;
    }

    public boolean search(Artwork_MelindaVigh art) {
        return searchRecursive(root, art);
    }

    private boolean searchRecursive(Node root, Artwork_MelindaVigh art) {
        if (root == null)
            return false;

        // Compare artworks based on a specific property (e.g., title and artist)
        if (art.getTitle().equals(root.artpiece.getTitle()) && art.getArtist().equals(root.artpiece.getArtist()) && art.getYear() == root.artpiece.getYear())
            return true;

        // Determine the direction to search based on the comparison of the years
        if (art.getYear() < root.artpiece.getYear())
            return searchRecursive(root.left, art);
        else
            return searchRecursive(root.right, art);
    }

    public void remove(Artwork_MelindaVigh art) {
        root = removeRecursive(root, art);
    }

    private Node removeRecursive(Node root, Artwork_MelindaVigh art) {
        if (root == null)
            return root;

        // Compare artworks based on a specific property (e.g., title and artist)
        if (art.getTitle().equals(root.artpiece.getTitle()) && art.getArtist().equals(root.artpiece.getArtist())) {
            // Case 1: Node has no child or only one child
            if (root.left == null)
                return root.right;
            else if (root.right == null)
                return root.left;

            // Case 2: Node has two children
            root.artpiece = findMin(root.right); // Replace with the minimum value from the right subtree
            root.right = removeRecursive(root.right, root.artpiece); // Remove the duplicate node from the right subtree
        } else if (art.getYear() < root.artpiece.getYear()) {
            root.left = removeRecursive(root.left, art);
        } else {
            root.right = removeRecursive(root.right, art);
        }

        return root;
    }

    private Artwork_MelindaVigh findMin(Node root) {
        while (root.left != null) {
            root = root.left;
        }
        return root.artpiece;
    }

    public void inorderTraversal(FileWriter writer) throws QueueUnderflowException, QueueOverflowException, IOException {
        Queue_MelindaVigh queue = new Queue_MelindaVigh(10);
        inorderTraversalRecursive(root, queue);

        while (!queue.isEmpty()) {
            Artwork_MelindaVigh artwork = queue.dequeue();
            String output = "'" + artwork.getTitle() + "' by " + artwork.getArtist() + " was completed in " + artwork.getYear()+"\n";
            writer.write(output);
        }
        // Now clear the writer using flush() method
        writer.flush();
    }

    private void inorderTraversalRecursive(Node root, Queue_MelindaVigh queue) throws QueueOverflowException {
        if (root != null) {
            inorderTraversalRecursive(root.left, queue);
            queue.enqueue(root.artpiece);
            inorderTraversalRecursive(root.right, queue);
        }
    }
}


// THIS IS GOOD FOR THE STACK!
//public class BinarySearchTree_MelindaVigh {
//    private Node root;
//
//    public BinarySearchTree_MelindaVigh() {
//        root = null;
//    }
//
//    public void insert(Artwork_MelindaVigh art) {
//        root = insertRecursive(root, art);
//    }
//
//    private Node insertRecursive(Node root, Artwork_MelindaVigh art) {
//        if (root == null) {
//            root = new Node(art);
//            return root;
//        }
//
//        // Compare artworks based on a specific property (e.g., year)
//        if (art.getYear() < root.artpiece.getYear())
//            root.left = insertRecursive(root.left, art);
//        else if (art.getYear() > root.artpiece.getYear())
//            root.right = insertRecursive(root.right, art);
//
//        return root;
//    }
//
//    public boolean search(Artwork_MelindaVigh art) {
//        return searchRecursive(root, art);
//    }
//
//    private boolean searchRecursive(Node root, Artwork_MelindaVigh art) {
//        if (root == null)
//            return false;
//
//        // Compare artworks based on a specific property (e.g., title and artist)
//        if (art.getTitle().equals(root.artpiece.getTitle()) && art.getArtist().equals(root.artpiece.getArtist()) && art.getYear() == root.artpiece.getYear())
//            return true;
//
//        // Determine the direction to search based on the comparison of the years
//        if (art.getYear() < root.artpiece.getYear())
//            return searchRecursive(root.left, art);
//        else
//            return searchRecursive(root.right, art);
//    }
//
//    public void remove(Artwork_MelindaVigh art) {
//        root = removeRecursive(root, art);
//    }
//
//    private Node removeRecursive(Node root, Artwork_MelindaVigh art) {
//        if (root == null)
//            return root;
//
//        // Compare artworks based on a specific property (e.g., title and artist)
//        if (art.getTitle().equals(root.artpiece.getTitle()) && art.getArtist().equals(root.artpiece.getArtist())) {
//            // Case 1: Node has no child or only one child
//            if (root.left == null)
//                return root.right;
//            else if (root.right == null)
//                return root.left;
//
//            // Case 2: Node has two children
//            root.artpiece = findMin(root.right); // Replace with the minimum value from the right subtree
//            root.right = removeRecursive(root.right, root.artpiece); // Remove the duplicate node from the right subtree
//        } else if (art.getYear() < root.artpiece.getYear()) {
//            root.left = removeRecursive(root.left, art);
//        } else {
//            root.right = removeRecursive(root.right, art);
//        }
//
//        return root;
//    }
//
//    private Artwork_MelindaVigh findMin(Node root) {
//        while (root.left != null) {
//            root = root.left;
//        }
//        return root.artpiece;
//    }
//
//    public void inorderTraversal() throws StackUnderflowException, StackOverflowException {
//        Stack_MelindaVigh stack = new Stack_MelindaVigh(10);
//        inorderTraversalRecursive(root, stack);
//
//        while (!stack.isEmpty()) {
//            Artwork_MelindaVigh artwork = stack.top();
//            stack.pop();
//            System.out.println("'" + artwork.getTitle() + "' by " + artwork.getArtist() + " was completed in " + artwork.getYear());
//        }
//    }
//
//    private void inorderTraversalRecursive(Node root, Stack_MelindaVigh stack) throws StackOverflowException {
//        if (root != null) {
//            inorderTraversalRecursive(root.left, stack);
//            stack.push(root.artpiece);
//            inorderTraversalRecursive(root.right, stack);
//        }
//    }
//}


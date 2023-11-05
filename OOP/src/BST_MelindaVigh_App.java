import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class BST_MelindaVigh_App {
    public static void main(String[] args) throws QueueUnderflowException, QueueOverflowException {
        System.out.println("Welcome! \nLet's sort your list or artworks in chronological order");
        System.out.println("You can 'add', 'remove', and 'search' for artworks in the list.");
        System.out.println("Write 'done' when you're finished");

        BinarySearchTree_MelindaVigh bst = new BinarySearchTree_MelindaVigh();

        try {
            File inputFile = new File("input.txt");
            Scanner sc = new Scanner(inputFile);

            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                String[] parts = line.split(",");
                int year = Integer.parseInt(parts[0].trim());
                String artist = parts[1].trim();
                String title = parts[2].trim();

                Artwork_MelindaVigh artwork = new Artwork_MelindaVigh(year, artist, title);
                bst.insert(artwork);
            }
            sc.close();

        }catch(FileNotFoundException e){
            System.out.println("File not found.");
        }

        try {
            File outputFile = new File("output.txt");
            FileWriter writer = new FileWriter(outputFile);

            writer.write("Inorder Traversal:\n");
            bst.inorderTraversal(writer);

            Scanner src = new Scanner(System.in);
            String choice ="";
            while (!"done".equalsIgnoreCase(choice)) {
                System.out.print("Please enter one of the options:");
                choice = src.next();

                if ("add".equals(choice)) {
                    System.out.println("Enter the year the artwork was created");
                    int year = src.nextInt();

                    System.out.println("What's the artist's name?");
                    src.nextLine(); // Consume the newline character, so it doesn't skip one of the prompts
                    String artist = src.nextLine();

                    System.out.println("What's the title of the artwork?");
                    //src.nextLine(); // Consume the newline character, so it doesn't skip one of the prompts
                    String title = src.nextLine();


                    Artwork_MelindaVigh artwork = new Artwork_MelindaVigh(year, artist, title);
                    bst.insert(artwork);
                    System.out.println("You've successfully added an artwork");
                }
                else if ("remove".equalsIgnoreCase(choice)){
                    System.out.println("Enter the year of the artwork you wish to remove");
                    int year = src.nextInt();

                    System.out.println("Enter the artist's name of the artwork you wish to remove");
                    src.nextLine(); // Consume the newline character, so it doesn't skip one of the prompts
                    String artist = src.nextLine();

                    System.out.println("Enter the title of the artwork you wish to remove");
                   // src.nextLine(); // Consume the newline character, so it doesn't skip one of the prompts
                    String title = src.nextLine();

                    Artwork_MelindaVigh removeArt = new Artwork_MelindaVigh(year, artist, title);
                    bst.remove(removeArt);
                    System.out.println("You've successfully removed an artwork");
                }
                else if("search".equalsIgnoreCase(choice)){
                    System.out.println("Enter the year of the artwork you're searching for");
                    int year = src.nextInt();

                    System.out.println("Enter the artist's name of the artwork you're searching for");
                    src.nextLine(); // Consume the newline character, so it doesn't skip one of the prompts
                    String artist = src.nextLine();

                    System.out.println("Enter the title of the artwork you're searching for");
                    //src.nextLine(); // Consume the newline character, so it doesn't skip one of the prompts
                    String title = src.nextLine();

                    Artwork_MelindaVigh searchArt = new Artwork_MelindaVigh(year, artist, title);
                    if (bst.search(searchArt))
                        writer.write("\n'" + searchArt.getTitle() + "' by " + searchArt.getArtist() + " from " + searchArt.getYear() + " was found in the tree.\n");
                    else
                        writer.write("\n'" + searchArt.getTitle() + "' " + searchArt.getArtist() + " from " + searchArt.getYear() + " was NOT found in the tree.\n");
                }
                else if ("done".equalsIgnoreCase(choice)) {
                    System.out.println("Thanks! Good bye!");
                }
            }
            writer.write("\nInorder Traversal after adding or removing an artwork:\n");
            bst.inorderTraversal(writer);

            writer.close();
            System.out.println("Results written to 'output.txt'.");
        } catch (IOException e) {
            System.out.println("Was not able to write to file.");
        }
    }
}
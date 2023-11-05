import java.io.FileWriter;
import java.io.IOException;

public interface BSTInterface_MelindaVigh {
    void insert(Artwork_MelindaVigh art);
    boolean search(Artwork_MelindaVigh art);
    void remove(Artwork_MelindaVigh art);
    void inorderTraversal(FileWriter writer) throws QueueUnderflowException, QueueOverflowException, IOException;
}

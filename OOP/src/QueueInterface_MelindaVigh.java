public interface QueueInterface_MelindaVigh {
    public void enqueue(Artwork_MelindaVigh piece) throws QueueOverflowException;
    public Artwork_MelindaVigh dequeue() throws QueueUnderflowException;
    public Artwork_MelindaVigh peek() throws QueueUnderflowException;
    public boolean isEmpty();
    public boolean isFull();
}

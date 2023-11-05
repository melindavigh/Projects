
public class Queue_MelindaVigh implements QueueInterface_MelindaVigh{
    private int maxSize;
    private Artwork_MelindaVigh[] queueArray;
    private int front;
    private int rear;
    private int currentSize;

    public Queue_MelindaVigh(int maxSize) {
        this.maxSize = maxSize;
        this.queueArray = new Artwork_MelindaVigh[maxSize];
        this.front = 0;
        this.rear = -1;
        this.currentSize = 0;
    }

    public boolean isEmpty() {
        return currentSize == 0;
    }

    public boolean isFull() {
        return currentSize == maxSize;
    }

    public int size() {
        return currentSize;
    }

    public void enqueue(Artwork_MelindaVigh piece) throws QueueOverflowException {
        if (isFull()) {
            throw new QueueOverflowException("Queue is full. Unable to enqueue.");
        }
        else {
            rear = (rear + 1) % maxSize;
            queueArray[rear] = piece;
            currentSize++;
        }
    }

    public Artwork_MelindaVigh dequeue() throws QueueUnderflowException {
        if (isEmpty()) {
            throw new QueueUnderflowException("Queue is empty. Unable to dequeue.");
        }
        else {
            Artwork_MelindaVigh dequeuedItem = queueArray[front];
            front = (front + 1) % maxSize;
            currentSize--;
            return dequeuedItem;
        }
    }

    public Artwork_MelindaVigh peek() throws QueueUnderflowException {
        if (isEmpty()) {
            throw new QueueUnderflowException("Queue is empty. Unable to peek.");
        }
        else {
            return queueArray[front];
        }
    }
}
public class Artwork_MelindaVigh {
    //private double length;
    //private double width;
    private int year;
    private String artist;
    private String title;

    Artwork_MelindaVigh(int year, String artist, String title){
        this.year = year;
        this.artist = artist;
        this.title = title;
    }

    // setters
    public void setArtist(String artist) {
        this.artist = artist;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setYear(int year) {
        this.year = year;
    }

    // getters
    public int getYear() {
        return year;
    }

    public String getArtist() {
        return artist;
    }

    public String getTitle() {
        return title;
    }

    //methods
//    public double getArea(){
//        return this.length * this.width;
//    }

    @Override
    public String toString(){
        return ("'" + this.getTitle() + "' artwork by " + this.getArtist() + " was completed in "
                + this.getYear());
    }
}

package models;

public class columns {
    Integer disk_number;
    Integer slide_number;
    String keywords;
    String location;
    String year;
    String photographer;
    String file_name;

    public columns(Integer disk_number, Integer slide_number, String keywords, String location, String year, String photographer, String file_name) {
        this.disk_number = disk_number;
        this.slide_number = slide_number;
        this.keywords = keywords;
        this.location = location;
        this.year = year;
        this.photographer = photographer;
        this.file_name = file_name;
    }

    public Integer getDisk_number() {
        return disk_number;
    }

    public void setDisk_number(Integer disk_number) {
        this.disk_number = disk_number;
    }

    public Integer getSlide_number() {
        return slide_number;
    }

    public void setSlide_number(Integer slide_number) {
        this.slide_number = slide_number;
    }

    public String getKeywords() {
        return keywords;
    }

    public void setKeywords(String keywords) {
        this.keywords = keywords;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }

    public String getPhotographer() {
        return photographer;
    }

    public void setPhotographer(String photographer) {
        this.photographer = photographer;
    }

    public String getFile_name() {
        return file_name;
    }

    public void setFile_name(String file_name) {
        this.file_name = file_name;
    }
}

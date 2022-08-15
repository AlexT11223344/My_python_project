package services;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class MySQLdb {
    String url = "jdbc:mysql://localhost:3306/photograph_index";
    String driver = "com.mysql.cj.jdbc.Driver";
    String user_name = "root";
    String password = "alex11223344";
    Connection connection = null;
    static MySQLdb instance = null;

    public MySQLdb() {
        try {
            Class.forName(driver);
            connection = DriverManager.getConnection(url, user_name, password);
        } catch (SQLException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static synchronized MySQLdb getInstance() {
        if (instance == null) {
            instance = new MySQLdb();
        }
        return instance;
    }

    public List<String> fetchKeywords() throws SQLException{
        List<String> Keywords_list = new ArrayList<>();
        String sql_GetKeywords = "SELECT * FROM martin_archive_printable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetKeywords);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String keywords = resultSet.getString("Keywords");
            Keywords_list.add(keywords);
        }
        return Keywords_list;
    }


    public List<String> fetchDiskNum() throws SQLException{
        List<String> diskNum_list = new ArrayList<>();
        String sql_GetKeywords = "SELECT * FROM martin_archive_printable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetKeywords);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String diskNumber = resultSet.getString("Disk_Number");
            diskNum_list.add(diskNumber);
        }
        return diskNum_list;
    }

    public List<String> fetchSlideNum() throws SQLException{
        List<String> slideNum_list = new ArrayList<>();
        String sql_GetKeywords = "SELECT * FROM martin_archive_printable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetKeywords);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String slideNumber = resultSet.getString("Slide_number");
            slideNum_list.add(slideNumber);
        }
        return slideNum_list;
    }

    public List<String> fetchLocation() throws SQLException{
        List<String> location_list = new ArrayList<>();
        String sql_GetKeywords = "SELECT * FROM martin_archive_printable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetKeywords);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String location = resultSet.getString("Location");
            location_list.add(location);
        }
        return location_list;
    }

    public List<String> fetchYear() throws SQLException{
        List<String> year_list = new ArrayList<>();
        String sql_GetKeywords = "SELECT * FROM martin_archive_printable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetKeywords);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String year = resultSet.getString("Year");
            year_list.add(year);
        }
        return year_list;
    }

    public List<String> fetchPhotographer() throws SQLException{
        List<String> photographer_list = new ArrayList<>();
        String sql_GetKeywords = "SELECT * FROM martin_archive_printable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetKeywords);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String photographer = resultSet.getString("Photographer");
            photographer_list.add(photographer);
        }
        return photographer_list;
    }

    public List<String> fetchFileName() throws SQLException{
        List<String> fileName_list = new ArrayList<>();
        String sql_GetKeywords = "SELECT * FROM martin_archive_printable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetKeywords);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String fileName = resultSet.getString("File_Name");
            fileName_list.add(fileName);
        }
        return fileName_list;
    }

}

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


    /* 1. Fetch keywords, extract data from Keywords column */
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


    /* 2. Fetch Disk Number, extract data from Disk Number column */
    public List<String> fetchDiskNum() throws SQLException{
        List<String> DiskNum_list = new ArrayList<>();
        String sql_GetDiskNum = "SELECT * FROM martin_archive_printable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetDiskNum);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String keywords = resultSet.getString("Disk_Number");
            DiskNum_list.add(keywords);
        }
        return DiskNum_list;
    }


    /* 3. Fetch slide Number, extract data from slide Number column */
    public List<String> fetchSlideNum() throws SQLException{
        List<String> SlideNum_list = new ArrayList<>();
        String sql_GetSlideNum = "SELECT * FROM martin_archive_printable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetSlideNum);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String keywords = resultSet.getString("slide_number");
            SlideNum_list.add(keywords);
        }
        return SlideNum_list;
    }


    /* 4. Fetch location, extract data from location column */
    public List<String> fetchLocation() throws SQLException{
        List<String> Location_list = new ArrayList<>();
        String sql_GetLocation = "SELECT * FROM martin_archive_printable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetLocation);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String keywords = resultSet.getString("Location");
            Location_list.add(keywords);
        }
        return Location_list;
    }


    /* 5. Fetch Year, extract data from Year column */
    public List<String> fetchYear() throws SQLException{
        List<String> Year_list = new ArrayList<>();
        String sql_GetYear = "SELECT * FROM martin_archive_printable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetYear);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String keywords = resultSet.getString("Year");
            Year_list.add(keywords);
        }
        return Year_list;
    }


    /* 6. Fetch Photographer, extract data from Photographer column */
    public List<String> fetchPhotographer() throws SQLException{
        List<String> Photographer_list = new ArrayList<>();
        String sql_GetPhotographer = "SELECT * FROM martin_archive_printable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetPhotographer);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String keywords = resultSet.getString("Photographer");
            Photographer_list.add(keywords);
        }
        return Photographer_list;
    }


    /* 2. Fetch File Name, extract data from File Name column */
    public List<String> fetchFileName() throws SQLException{
        List<String> FileName_list = new ArrayList<>();
        String sql_GetFileName = "SELECT * FROM martin_archive_printable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetFileName);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String keywords = resultSet.getString("File_Name");
            FileName_list.add(keywords);
        }
        return FileName_list;
    }

}

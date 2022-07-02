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
        String sql_GetKeywords = "SELECT * FROM martinarchiveprintable";
        PreparedStatement preparedStatement = connection.prepareStatement(sql_GetKeywords);
        ResultSet resultSet = preparedStatement.executeQuery();
        while (resultSet.next()){
            String keywords = resultSet.getString("Keywords");
            Keywords_list.add(keywords);
        }
        return Keywords_list;
    }

}

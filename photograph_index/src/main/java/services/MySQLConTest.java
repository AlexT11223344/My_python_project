package services;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class MySQLConTest {
    public void jdbcall() throws ClassNotFoundException, SQLException{

        Class.forName("com.mysql.jdbc.Driver");//加载驱动类
        String url="jdbc:mysql://localhost:3306/photograph_index";
        String username="root";
        String password="alex11223344";
        Connection conn=DriverManager.getConnection(url,username,password);//用参数得到连接对象
        System.out.println("Success！");
        System.out.println(conn);
    }
}

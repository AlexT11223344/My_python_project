package servlet;

import services.MySQLdb;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.sql.SQLException;
import java.util.List;

@WebServlet(name = "DbInfoServlet", value = "/DbInfoServlet")
public class DbInfoServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        MySQLdb mySQLdb = MySQLdb.getInstance();

        try{
            List<String> keywords = mySQLdb.fetchKeywords();
            request.getSession().setAttribute("Keywords", keywords);

            List<String> diskNum = mySQLdb.fetchDiskNum();
            request.getSession().setAttribute("DiskNum", diskNum);

            List<String> slideNum = mySQLdb.fetchSlideNum();
            request.getSession().setAttribute("SlideNum", slideNum);

            List<String> location = mySQLdb.fetchLocation();
            request.getSession().setAttribute("Location", location);

            List<String> year = mySQLdb.fetchYear();
            request.getSession().setAttribute("Year", year);

            List<String> photographer = mySQLdb.fetchPhotographer();
            request.getSession().setAttribute("Photographer", photographer);

            List<String> fileName = mySQLdb.fetchFileName();
            request.getSession().setAttribute("FileName", fileName);
        }
        catch (SQLException e){
            e.printStackTrace();
        }

        RequestDispatcher dispatcher = request.getRequestDispatcher("/test.jsp");
        dispatcher.forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}

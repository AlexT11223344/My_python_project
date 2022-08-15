package servlet;

import services.MySQLdb;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.annotation.*;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;
import java.util.regex.Pattern;

@WebServlet(name = "ServiceLogic", value = "/ServiceLogic")
public class ServiceLogic extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        MySQLdb mySQLdb = MySQLdb.getInstance();

        String keyword = request.getParameter("keyword");
        request.getSession().setAttribute("Keyword", keyword);

        String photographer_input = request.getParameter("photographer");
        request.getSession().setAttribute("Photographer_input", photographer_input);
        System.out.println(photographer_input);

        try {
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


//            System.out.println(keywords.getClass().toString());

            /* Transfer java.util.array(dynamic) to array(static) */
            String[] keywords_Array = new String[keywords.size()];
            String[] diskNum_Array = new String[diskNum.size()];
            String[] slideNum_Array = new String[slideNum.size()];
            String[] location_Array = new String[location.size()];
            String[] year_Array = new String[year.size()];
            String[] photographer_Array = new String[photographer.size()];
            String[] fileName_Array = new String[fileName.size()];

            keywords.toArray(keywords_Array);
            diskNum.toArray(diskNum_Array);
            slideNum.toArray(slideNum_Array);
            location.toArray(location_Array);
            year.toArray(year_Array);
            photographer.toArray(photographer_Array);
            fileName.toArray(fileName_Array);

            ArrayList results_disNum = new ArrayList();
            ArrayList results_slideNum = new ArrayList();
            ArrayList results_location = new ArrayList();
            ArrayList results_year = new ArrayList();
            ArrayList results_photographer = new ArrayList();
            ArrayList results_fileName = new ArrayList();
            ArrayList results_keywords = new ArrayList();



            for(int i =0; i < keywords_Array.length; i++){
//                System.out.println(keywords_Array[i]);
//                System.out.println(keywords_Array[i].getClass());
                if (photographer_Array[i].trim().equals(photographer_input) == true || photographer_input.equals("0") == true){
                    List<String> temp = Arrays.asList(keywords_Array[i].split(","));
                    String[] temp_arr = new String[temp.size()];
                    temp.toArray(temp_arr);

                    for(int j =0; j < temp_arr.length; j++){
                        temp_arr[j] = temp_arr[j].replaceAll("[\\pP‘’“”]" , "");
                        temp_arr[j] = temp_arr[j].trim();
                        String temp_arr_lowercase = temp_arr[j].toLowerCase();
//                    System.out.println(fileName_Array[i]);
//                    System.out.println(temp_arr_lowercase);
//                    String str_regex = "^(?i)" + temp_arr[j] + "$";
//                    Pattern p = Pattern.compile(str_regex, Pattern.CASE_INSENSITIVE);

                        if(temp_arr_lowercase.indexOf(keyword.toLowerCase()) != -1){
//                        System.out.println(temp_arr[j]);
//                        System.out.println("keyword is:" + keyword);
                            results_disNum.add(diskNum_Array[i]);
                            results_slideNum.add(slideNum_Array[i]);
                            results_location.add(location_Array[i]);
                            results_year.add(year_Array[i]);
                            results_photographer.add(photographer_Array[i]);
                            results_fileName.add(fileName_Array[i]);
                            results_keywords.add(keywords_Array[i]);
                        }
                        else{
                            continue;
                        }
                    }
                }
                else continue;
            }
//            for (String str : keywords){
//                System.out.println(str);
//            }
            request.getSession().setAttribute("results_DisNum", results_disNum);
            request.getSession().setAttribute("results_SlideNum", results_slideNum);
            request.getSession().setAttribute("results_Location", results_location);
            request.getSession().setAttribute("results_Year", results_year);
            request.getSession().setAttribute("results_Photographer", results_photographer);
            request.getSession().setAttribute("results_FileName", results_fileName);
            request.getSession().setAttribute("results_Keywords", results_keywords);



        } catch (SQLException e) {
            e.printStackTrace();
        }

        RequestDispatcher dispatcher = request.getRequestDispatcher("/Homepage.jsp");
        dispatcher.forward(request, response);
    }


    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }
}

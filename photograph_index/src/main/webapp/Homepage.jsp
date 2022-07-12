<%--
  Created by IntelliJ IDEA.
  User: Alex Tang
  Date: 2022/6/24
  Time: 15:33
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Home Page</title>
</head>
<body>


<form name="keyword" action="KeywordInfoServlet" method="get">
    <h2>Input keyword:</h2>
    <input type="text" name="keyword">
    <input type="submit" id="search" value="Search">

</form>

<form name="DBinfo" action="DbInfoServlet" method="get">
    <h2>Test connection to the DB and get infomation from it</h2>
    <input type="submit" value="Test">
</form>

<p id="keyword_print"></p>

</body>
</html>

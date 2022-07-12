<%--
  Created by IntelliJ IDEA.
  User: 23619
  Date: 2022/6/25
  Time: 15:32
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page import="java.util.List" %>
<html>
<head>
    <title>Test page</title>
</head>
<body>
    <c:forEach items="${Keywords}" var="keywords" varStatus="i">
        <li>${i.index + 1}. ${keywords}</li>
    </c:forEach>
</body>
</html>

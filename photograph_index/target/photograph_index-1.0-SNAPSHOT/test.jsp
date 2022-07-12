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

    <P>******************************************************</P>
    <c:forEach items="${DiskNum}" var="disknum" varStatus="i1">
        <li>${i1.index + 1}. ${disknum}</li>
    </c:forEach>

    <P>******************************************************</P>
    <c:forEach items="${SlideNum}" var="slidenum" varStatus="i2">
        <li>${i2.index + 1}. ${slidenum}</li>
    </c:forEach>

    <P>******************************************************</P>
    <c:forEach items="${Keywords}" var="keywords" varStatus="i3">
        <li>${i3.index + 1}. ${keywords}</li>
    </c:forEach>

    <c:forEach items="${Location}" var="location" varStatus="i4">
        <li>${i4.index + 1}.${location}</li>
    </c:forEach>

    <P>******************************************************</P>
    <c:forEach items="${Year}" var="year" varStatus="i5">
        <li>${i5.index + 1}. ${year}</li>
    </c:forEach>

    <P>******************************************************</P>
    <c:forEach items="${Photographer}" var="photographer" varStatus="i6">
        <li>${i6.index + 1}. ${photographer}</li>
    </c:forEach>

    <P>******************************************************</P>
    <c:forEach items="${FileName}" var="filename" varStatus="i7">
        <li>${i7.index + 1}. ${filename}</li>
    </c:forEach>

</body>
</html>

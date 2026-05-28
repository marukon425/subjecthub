<%@page import="java.util.Calendar"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>chap7/mondai15</title>
</head>
<body>
	<% String str = "問題15はこれにてクリア！お疲れ様でした。"; %>
	<%= str+"<br>" %>
	<% Calendar calendar = Calendar.getInstance();%>
	<% String[] daysOfWeek = {"日","月","火","水","木","金","土"}; %>
	<%= String.format("%d年%d月%d日(%s)　%d:%d:%d",calendar.get(Calendar.YEAR),calendar.get(Calendar.MONTH)+1
			,calendar.get(Calendar.DATE),daysOfWeek[calendar.get(Calendar.DAY_OF_WEEK) - 1],calendar.get(Calendar.HOUR_OF_DAY)
			,calendar.get(Calendar.MINUTE),calendar.get(Calendar.SECOND)) %>
</body>
</html>
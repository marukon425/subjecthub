package chap4;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Calendar;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;


@WebServlet("/chap4/mondai17")
public class Mondai17 extends HttpServlet {

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html; charset=UTF-8");
		PrintWriter out = response.getWriter();
//		Date date = new java.util.Date();
		Calendar calendar = Calendar.getInstance();
		int year = calendar.get(Calendar.YEAR);
		int month = calendar.get(Calendar.MONTH) + 1; // 月は 0 から始まるため、1 を加えて補正
		int day = calendar.get(Calendar.DATE);
		int dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK); // 曜日を取得する場合
		int hour = calendar.get(Calendar.HOUR_OF_DAY);
		int minute = calendar.get(Calendar.MINUTE);
		int second= calendar.get(Calendar.SECOND);
		

		String[] daysOfWeek = {"日", "月", "火", "水", "木", "金", "土"};
		String dayOfWeekStr = daysOfWeek[dayOfWeek - 1]; // 配列のインデックスに合わせるために -1

		out.println("問題１７はこれにてクリア！お疲れ様でした。<br>");
		out.printf("%d年%d月%d日(%s) %s:%s:%s", year, month, day, dayOfWeekStr,hour,minute,second);
	}

}

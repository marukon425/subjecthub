package chap21;

import java.io.IOException;
import java.util.List;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import bean.Course;
import dao.CourseDAO;

@WebServlet(urlPatterns={"/chap21/mondai13/input"})
public class Mondai13input extends HttpServlet {
	public void doGet (
		HttpServletRequest request, HttpServletResponse response
	) throws ServletException, IOException {

		try {
			CourseDAO dao = new CourseDAO();
			List<Course> list = dao.selectAll();

			request.setAttribute("list", list);

		} catch (Exception e) {
			e.printStackTrace();
		}

		request.getRequestDispatcher("/chap21/mondai13input.jsp").forward(request, response);
	}
}

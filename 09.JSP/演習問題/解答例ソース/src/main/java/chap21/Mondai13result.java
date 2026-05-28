package chap21;

import java.io.IOException;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import bean.Course;
import dao.CourseDAO;

@WebServlet(urlPatterns={"/chap21/mondai13/update"})
public class Mondai13result extends HttpServlet {
	public void doGet (
		HttpServletRequest request, HttpServletResponse response
	) throws ServletException, IOException {
		int id = Integer.parseInt(request.getParameter("id"));

		try {
			CourseDAO dao = new CourseDAO();
			Course cou = dao.selectById(id);

			request.setAttribute("course", cou);

		} catch (Exception e) {
			e.printStackTrace();
		}

		request.getRequestDispatcher("/chap21/mondai13update.jsp").forward(request, response);
	}
}

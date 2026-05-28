package chap20;

import java.io.IOException;
import java.util.List;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import bean.Course;
import bean.StudentExp;
import dao.CourseDAO;
import dao.StudentDAO;

@WebServlet(urlPatterns={"/chap20/mondai15/update"})
public class Mondai15result extends HttpServlet {
	public void doGet (
		HttpServletRequest request, HttpServletResponse response
	) throws ServletException, IOException {
		int id = Integer.parseInt(request.getParameter("id"));

		try {
			StudentDAO dao = new StudentDAO();
			StudentExp stu = dao.selectById(id);

			CourseDAO cDao = new CourseDAO();
			List<Course> cList = cDao.selectAll();

			request.setAttribute("student", stu);
			request.setAttribute("courseList", cList);

		} catch (Exception e) {
			e.printStackTrace();
		}

		request.getRequestDispatcher("/chap20/mondai15update.jsp").forward(request, response);
	}
}

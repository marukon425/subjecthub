package chap22;

import java.io.IOException;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import bean.StudentExp;
import dao.StudentDAO;

@WebServlet(urlPatterns={"/chap22/mondai11/disp"})
public class Mondai11disp extends HttpServlet {
	public void doGet (
		HttpServletRequest request, HttpServletResponse response
	) throws ServletException, IOException {
		int id = Integer.parseInt(request.getParameter("id"));

		try {
			StudentDAO dao = new StudentDAO();
			StudentExp stu = dao.selectById(id);

			request.setAttribute("student", stu);

		} catch (Exception e) {
			e.printStackTrace();
		}

		request.getRequestDispatcher("/chap22/mondai11disp.jsp").forward(request, response);
	}
}

package chap16;

import java.io.IOException;
import java.util.List;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import bean.StudentExp;
import dao.StudentDAO;

@WebServlet(urlPatterns={"/chap16/mondai14"})
public class Mondai14 extends HttpServlet {

	public void doGet (
		HttpServletRequest request, HttpServletResponse response
	) throws ServletException, IOException {

		request.setCharacterEncoding("UTF-8");
		String name = request.getParameter("name");

		try {
			if(name != null){
				StudentDAO dao = new StudentDAO();
				List<StudentExp> list = dao.partialMatchSearchByName(name);

				request.setAttribute("list", list);
			}

			request.getRequestDispatcher("mondai14.jsp").forward(request, response);

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}

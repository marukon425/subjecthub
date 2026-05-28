package chap20;

import java.io.IOException;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import bean.Student;
import dao.StudentDAO;

@WebServlet(urlPatterns={"/chap20/mondai15/result"})
public class Mondai15update extends HttpServlet {
	public void doGet (
		HttpServletRequest request, HttpServletResponse response
	) throws ServletException, IOException {

		int id = Integer.parseInt(request.getParameter("id"));
		String name = request.getParameter("name");
		int courseId = Integer.parseInt(request.getParameter("courseId"));
		Student stu = new Student();
		stu.setStudentId(id);
		stu.setStudentName(name);
		stu.setCourseId(courseId);

		try {
			StudentDAO dao = new StudentDAO();
			int line = dao.update(stu);

			if(line > 0){
				request.setAttribute("message", "更新が完了しました。");
			}else{
				request.setAttribute("message", "更新出来ませんでした。\n再度お試しください。");
			}

		} catch (Exception e) {
			e.printStackTrace();
		}

		request.getRequestDispatcher("/chap20/mondai15result.jsp").forward(request, response);
	}
}

package chap17;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import bean.StudentExp;
import dao.StudentDAO;

@WebServlet(urlPatterns={"/chap17/mondai15/add"})
public class Mondai15Add extends HttpServlet {
	public void doGet (
		HttpServletRequest request, HttpServletResponse response
	) throws ServletException, IOException {

		HttpSession session = request.getSession();
		request.setCharacterEncoding("UTF-8");
		String[] ids = request.getParameterValues("studentIds");

		if(ids == null){
			request.setAttribute("message", "一人以上を選択してください");
			session.removeAttribute("commendationList");
			session.setAttribute("commendationList", new ArrayList<StudentExp>());
		}else{
			try {
				StudentDAO dao = new StudentDAO();
				List<StudentExp> list = dao.selectByIds(ids);

				session.setAttribute("commendationList", list);
				request.setAttribute("message", "リストに追加しました。");

			} catch (Exception e) {
				e.printStackTrace();
			}
		}

		request.getRequestDispatcher("/chap17/mondai15list.jsp").forward(request, response);

	}
}

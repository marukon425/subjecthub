package chap17;

import java.io.IOException;
import java.util.List;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import bean.StudentExp;
import dao.StudentDAO;

@WebServlet(urlPatterns={"/chap17/mondai15/input"})
public class Mondai15Input extends HttpServlet {
	public void doGet (
		HttpServletRequest request, HttpServletResponse response
	) throws ServletException, IOException {

		HttpSession session = request.getSession();
		List<StudentExp> commendationList = (List<StudentExp>)session.getAttribute("commendationList");

		try {
			StudentDAO dao = new StudentDAO();
			List<StudentExp> list = dao.selectAllWithCourseName();

			if(commendationList != null){
				for(StudentExp stu:commendationList){
					for(int i=0;i<list.size();i++){
						if(stu.getStudentId() == list.get(i).getStudentId()){
							list.get(i).setCheck();
							break;
						}
					}
				}
			}

			request.setAttribute("list", list);
			request.getRequestDispatcher("/chap17/mondai15input.jsp").forward(request, response);

		} catch (Exception e) {
			e.printStackTrace();
		}

	}
}

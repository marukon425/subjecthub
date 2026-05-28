package chap17;

import java.io.IOException;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

@WebServlet(urlPatterns={"/chap17/mondai13/result"})
public class Mondai13Result extends HttpServlet {

	public void doGet (
		HttpServletRequest request, HttpServletResponse response
	) throws ServletException, IOException {

		HttpSession session = request.getSession();
		int price = (Integer)session.getAttribute("price");
		int quantity = (Integer)session.getAttribute("quantity");

		int total = price * quantity;

		request.setAttribute("total", total);

		request.getRequestDispatcher("/chap17/mondai13result.jsp").forward(request, response);

	}
}

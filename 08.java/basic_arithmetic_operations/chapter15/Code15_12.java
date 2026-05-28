package basic_arithmetic_operations.chapter15;
import java.util.*;

import javax.xml.crypto.Data;;

public class Code15_12 {
    public static void main(String[] args) {
        Calendar c = Calendar.getInstance();
        c.set(2023, 8, 18, 5, 53, 20);
        c.set(Calendar.MONTH, 9);
        Date d = c.getTime();
        System.out.println(d);
        Date now = new Date();
        c.setTime(now);
        int y = c.get(Calendar.YEAR);
        System.out.println("今年は" + y + "年です");
    }
}

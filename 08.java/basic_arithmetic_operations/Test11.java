package basic_arithmetic_operations;


// 繰り返し文
public class Test11 {
    public static void main(String[] args) {
        boolean doorClose = true;
        // 繰り返しの中にdoorCloseがfalseになる処理がないから永遠に繰り返す
        while (doorClose == true) {
            System.out.println("ノックする");
            System.out.println("1分待つ");
        }

    }
}



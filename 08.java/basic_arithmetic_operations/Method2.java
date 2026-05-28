package basic_arithmetic_operations;

public class Method2 {
    public static void main(String[] args) {
        // add(100, 20);
        // add(200, 50);
        System.out.println("数値を入力してください");
        int x = new java.util.Scanner(System.in).nextInt();
        System.out.println("数値を入力してください");
        int y = new java.util.Scanner(System.in).nextInt();
        add(x, y);
    }
    public static void add(int x, int y) {
        int ans = x + y;
        System.out.println(x + "+" + y + "=" + ans);
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.print("整数値xを入力してください");
        int x = new java.util.Scanner(System.in).nextInt();
        System.out.print("整数値yを入力してください");
        int y = new java.util.Scanner(System.in).nextInt();
        System.out.println(x + "から" +  y + "までの合計値は" + Calc.sum(x, y));

    }
}

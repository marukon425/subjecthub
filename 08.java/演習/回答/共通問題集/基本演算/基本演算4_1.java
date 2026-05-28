package 演習.回答.共通問題集.基本演算;

public class 基本演算4_1 {
    public static void main(String[] args) {
        System.out.println("0から100までの得点(整数値)を入力してください");
        int num1 = new java.util.Scanner(System.in).nextInt();
        if (num1 >= 80) {
            System.out.println("合格です");
        }else{
            System.out.println("不合格です");
        }
    }
}

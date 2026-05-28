package 演習.回答.共通問題集.基本演算;

public class 基本演算4_3 {
    public static void main(String[] args) {
        System.out.println("0～100までの得点(整数値)を2つ入力してください");
        int num1 = new java.util.Scanner(System.in).nextInt();
        int num2 = new java.util.Scanner(System.in).nextInt();
        if (num1 >= 80 && num2 >= 80) {
            System.out.println("２科目とも合格です");
        }
    }
}

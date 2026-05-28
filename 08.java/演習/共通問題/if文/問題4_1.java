package 共通問題.if文;

import java.util.Scanner;

public class 問題4_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("0～100 までの得点（整数値）を 2 つ入力してください");

        System.out.print("国語の点数");
        int japanese = sc.nextInt();

        System.out.print("英語の点数");
        int english = sc.nextInt();

        if (japanese == 100 && english == 100) {
            System.out.println("満点です");
        }
    }
}

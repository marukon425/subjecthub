package 共通問題.if文;

import java.util.Scanner;

public class 問題4_3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("0～100 までの得点（整数値）を 2 つ入力してください");

        System.out.print("国語の点数：");
        int japanese = sc.nextInt();

        System.out.print("英語の点数：");
        int english = sc.nextInt();

        if (japanese >= 80 && english >= 80) {
            System.out.println("２科目とも合格です。");
        }
    }
}

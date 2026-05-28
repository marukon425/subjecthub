package 共通問題.swich文;

import java.util.Scanner;

public class 問題5_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("ランクを入力してください");
        String lank = sc.nextLine();

        switch (lank) {
        case "A" :
            System.out.println("ランクAは評価「優」です");
        case "B" :
            System.out.println("ランクBは評価「良」です");
        case "C" :
            System.out.println("ランクCは評価「可」です");
        case "D" :
            System.out.println("ランクDは評価「不可」です");
        }
    }
}

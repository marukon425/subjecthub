package 演習.回答.共通問題集.基本演算;

public class 基本演算5_1 {
    public static void main(String[] args) {
        System.out.println("A～Dの値を入力してください：");
        String num = new java.util.Scanner(System.in).nextLine();
        
        switch (num) {
            case "A":
                System.out.println("ランク評価は「優」です");
            case "B":
                System.out.println("ランク評価は「良」です");
            case "C":
                System.out.println("ランク評価は「可」です");
            case "D":
                System.out.println("ランク評価は「不可」です");
        }
    }
    
}

package 演習.回答.共通問題集.基本演算;

public class 基本演算9_4 {
    public static int multiple(int num){
        return num*3;
    }

    public static void main(String[] args) {
        System.out.print("整数を入力してください");
        int num = new java.util.Scanner(System.in).nextInt();
        System.out.println(num + "の3倍は" + multiple(num) + "です。");
    }
}

package 演習.回答.共通問題集.基本演算;

public class 基本演算8_5 {
    public static void main(String[] args) {
    int[] lst = {1, 2, 3, 4, 5};
    int sum = 0;
    for (int value : lst){
        sum += value;
    }
    System.out.println("合計値は" + sum + "です。");
    System.out.println("平均値は" + sum/lst.length + "です。");
    }
}

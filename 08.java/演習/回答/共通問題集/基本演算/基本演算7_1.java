package 演習.回答.共通問題集.基本演算;

public class 基本演算7_1 {
    public static void main(String[] args) {
        int num = 0;
        int num1 = 0;
        while (num1<100){
            num1 += 1;
            num += num1;
            if (num1 == 100){
                break;
            }
        }
        System.out.println("合計："+num);
    }
}

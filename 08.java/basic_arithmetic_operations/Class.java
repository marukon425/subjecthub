package basic_arithmetic_operations;

// 二つのデータに分けてクラスを使う
public class Class {
    public static void main(String[] args) {
        int a = 10; int b = 2;
        //             ↓ 別ファイルで作ったクラスやメソッドが使える
        int total = CalcLogic.tasu(a,b);
        int delta = CalcLogic.hiku(a, b);
        System.out.println("足すと" + total + "、引くと" + delta);
    }
    // public static int tasu(int a, int b){
    //     return (a + b);
    // }

    // public static int hiku(int a, int b){
    //     return (a -b);
    // }
}



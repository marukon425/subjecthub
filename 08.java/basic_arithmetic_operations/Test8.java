package basic_arithmetic_operations;


// 乱数を発生させる
// pythonのときは
/*
import random

random randint(1, 10)
みたいな書き方するけど
*/
public class Test8 {
    public static void main(String[] args) {
        // 変数「r」に0～90のランダムな数字を代入
        // 　　　　　　↓    ↓    ↓     pythonでいうimport宣言 nexInt → 整数の値で
        int r = new java.util.Random().nextInt(90);
        System.out.println("あなたはたぶん、" + r + "歳ですね？");
    }
}

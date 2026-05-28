package basic_arithmetic_operations;

// 引数に配列を受け取るメソッド
public class Method5 {

    public static void printArray(int[] array){
        // 受け取った配列の引数を繰り返し表示する
        for (int element : array){
            System.out.println(element);
        }
    }
    public static void main(String[] args) {
        int[] array = {1, 2, 3};
        printArray(array);
    }
}
/*
配列(複数の数字)をメソッドに渡して1つずつ画面に表示するプログラム
mainメソッドで
int[] array = {1, 2, 3}; として数字を3つ持つ配列を作る
printArray(array);メソッドで
受け取った配列の中身を1つずつ取り出して表示する

*/
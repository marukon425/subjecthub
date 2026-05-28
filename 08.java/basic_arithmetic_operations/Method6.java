package basic_arithmetic_operations;


// 値私と参照渡し

// 同じ配列を参照しているが確認する
public class Method6 {
    // int型配列を受け取り、
    // 配列内の要素を全て1を加えるメソッド
    public static void incArray(int[] array) {
        for (int i = 0; i < array.length; i++){
            array[i]++; //要素に1を加える
        }
    }

    public static void main(String[] args) {
        int[] array = {1, 2, 3};  //int　型配列を定義
        incArray(array);  //配列を渡す
        for (int i : array){ //拡張for文で要素を順に取得
            System.out.println(i); //要素を表示
        }
    }
}
/*
配列をメソッドに渡して、配列の中の
「すべての用嘘に1を足す(中身を変える)」プログラム
mainで配列array = {1, 2, 3}を作る。
incArray(array)を呼ぶ → 配列の中身が{2, 3, 4}に書き換わる。
差後に for-eachで表示 → 出力は[2 3 4]
*/

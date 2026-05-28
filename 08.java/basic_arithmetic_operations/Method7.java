package basic_arithmetic_operations;


// 戻り値に配列を用いる
public class Method7 {
    // int型配列を受け取り
    // 配列内の要素全てに1を加えるメソッド
    public static void incArray(int[] array) {
        for (int i = 0; i < array.length; i++){
            array[i]++; //要素に1を加える
        }
    }
    public static void main(String[] args) {
        int[] array = {1, 2, 3}; // int 型配列を定義
        for (int i : array){ // 配列を渡す
            System.out.println(i); // 要素を表示
        }
    }
}


/*
配列をメソッドに渡して、配列の中の
全ての要素に1を足す (中身を書き換える) プログラム
main で配列 array = {1, 2, 3} を作る。
incArray(array)を呼ぶ → 配列の中身が {2, 3, 4}になる
最後にfor-eachで表示 → 出力は[2 3 4]
*/
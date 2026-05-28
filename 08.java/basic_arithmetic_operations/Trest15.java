package basic_arithmetic_operations;


// 配列
public class Trest15 {
    public static void main(String[] args) {
        // ---------------------------------------
        // int[] で整数型の配列を宣言
        int[] scores;
        // scoresに要素を5個作ることを定義
        scores = new int[5];
        // ---------------------------------------
        // ↑ を一行で書く ↓
        int[] scores1 = new int[5];



        // 配列の長さを調べる
        int num = scores.length;
        System.out.println("要素の数：" + num);
        // ↑ ５になる
        // ※いちいち変宣言しなくても一行で調べることもできる



        // 配列の利用(作った箱に要素を代入)
        // 配列の1番目に30を代入
        scores[1] = 30;
        System.out.println(scores[1]);
        // 30が表示される



        // 配列の初期化
        /*
        int x;
        System.out.println(x);
        ↑ "整数型x"ってだけの宣言だからコンパイルエラーになる
        */
        int[] scores3 = new int[5];
        System.out.println(scores[0]);
        // ↑ この時は0が出力される
        // 配列がString型のときは"null"が出力される



        // 省略技法
        int[] scores4 = new int[] {20, 30, 40, 50, 80};
        int[] scores5 = {20, 30, 40, 50, 80};


        // for文を使って配列を扱う
        int[] scores6 = {20, 30, 40, 50, 80};
        // scoeres6の要素数まで繰り返す
        for (int i = 0; i < scores6.length; i++) {
            // scores6のi番目の要素を出力
            System.out.println(scores6[i]);
        }



        // 拡張for文
        int[] scores7 = {20, 30, 40, 50, 80};
        // ↓ 従来のfor文
        for (int i = 0; i < scores7.length; i++){
            System.out.println(scores7[i]);
        }
        // 拡張for文
        // 「:」の打ち間違いに注意
        for (int value : scores7){
            System.out.println(value);
        }
        /*
        int i = 0; i < scores7.length; i++を書かなくても
        valueがデータの受け渡しができる
        
        python ↓
        scores = [20, 30, 40, 50, 80]
        for i in scores:
            print(i)
        みたいな感じの書き方
        */


    }
}

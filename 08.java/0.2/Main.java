public class Main{
    public static void main(String[] args){
        System.out.println("Hello World");
    }
}

/* 
public : どこからでも使える (公開) という意味
class : クラス定義の宣言
Main : クラスの名前 (自分が決めたクラスの名前)
static : インスタンスを作らなくても呼び出せるメソッド 「入口」　のイメージ
void : 戻り値がないことを示す
main : メソッド(関数)の名前
(string[]args) : コマンドラインから引数を受けるための変数
*/

/*
System.out.println(35 -10); → 25
System.out.println("尾田" + "亮太"); → 尾田亮太
*/



/*
【変数宣言】
public class Main{
    pubric static void main(string[] args){
        System.out.println("Hello World");
        int x; 変数(整数型)xを宣言 
        x = 3; xに3を代入
    }
}

型(int, str, float...) 変数名;
変数名は基本的に小文字
int num = 22; みたいなこともできる
*/


/*
コンパイルの仕方
ディレクトリをコンパイルしたファイルまで持ってくる
javac ○○.java　のコマンドを入力
コンパイルファイルができて完成
*/


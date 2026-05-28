package basic_arithmetic_operations;

/*
メソッドの定義
                            ↓この()は引数を受け渡すものだから必ず書かないといけない
public static void メソッド名()　{
    メソッドが呼び出された時の処理
}

javaは一番最初にmainメソッドを探しに行くからhelloメソッドをどこに書いてもmainの中にメソッドを呼び出したら実行できる
// つまり細かい処理はメソッドを作ってメソッドを動かすときはmainの中で動かしたらだいたい動く
*/


public class Method {
    public static void main(String[] args) {
        System.out.println("メソッドを呼び出します");
        hello();
        System.out.println("メソッドの呼び出しが終わりました");
    }

    // helloメソッド
    public static void hello(){
        System.out.println("奏さん、こんにちは");
    }
}

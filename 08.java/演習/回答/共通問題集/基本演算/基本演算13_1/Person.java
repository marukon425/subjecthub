package 演習.回答.共通問題集.基本演算.基本演算13_1;

//abstractを宣言して抽象クラス(Person)を作成
// 曖昧なクラス
abstract class Person {
    String name;
    String job;
    // コンストラクタ
    Person(String name, String job){
        // 初期化
        this.name = name;
        this.job = job;
    }

    // 抽象メソッド(introduct)を作成
    // 曖昧なメソッド
    // 自己紹介
    abstract void introduct();
}

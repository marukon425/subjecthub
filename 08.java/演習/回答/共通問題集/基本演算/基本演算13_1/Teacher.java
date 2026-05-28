package 演習.回答.共通問題集.基本演算.基本演算13_1;

// Personクラスを継承したクラス(Teacher)を作成
public class Teacher extends Person {
    String subject; //科目の初期化

    public Teacher(String name, String job, String subject){
        super(name, job);// 親クラスのコンストラクタを呼び出し
        this.subject = subject;
    }
    void introduct(){
        System.out.println("氏名：" + super.name);
        System.out.println("職種：" + super.job);
        System.out.println("担当教科：" + this.subject);
    }
}

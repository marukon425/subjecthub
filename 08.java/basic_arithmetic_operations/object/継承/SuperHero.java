
// Heroクラスを継承
// extendsで継承
public class SuperHero extends Hero {
    boolean flying;
    public SuperHero(){
        System.out.println("SuperHeroのコンストラクタが動作");
    }

    // 親クラスのattackを呼び出す
    public void attack(Matango m){
        super.attack(m);
        if (this.flying) {
            super.attack(m);
        }
    }

    public void fly(){
        this.flying = true;
        System.err.println("飛び上がった！");
    }

    public void land(){
        this.flying = false;
        System.out.println("着地した！");
    }

    // 親クラスから再定義(オーバーライド)
    // 親クラスに定義してるメソッドをもう一回子クラスで定義する
    // final 継承禁止を宣言する
    public  final void run(){
        System.out.println(this.name + "は撤退した");
    }

    // 親インスタンス部へのアクセス
    public void attack(Matango m){
        System.out.println(this.name + "の攻撃！");
        m.hp -= 5;
        System.out.println("5ポイントのダメージを与えた!");

        if (this.flying) {
            System.out.println(this.name + "の攻撃！");
            m.hp -= 5;
            System.out.println("5ポイントのダメージを与えた！");
        }
    }
}

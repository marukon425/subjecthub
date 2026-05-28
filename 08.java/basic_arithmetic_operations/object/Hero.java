public class Hero {
    String name; // 名前
    int hp; // 体力
    Sword sword;

    // 攻撃
    public void attack() {
        System.out.println(this.name + "は攻撃した！");
        System.out.println("敵に5ポイントのダメージを与えた!");
    }

    // 眠る  引数なし
    // this : pythonのselfみたいな感じのやつ
    public void sleep() {
        this.hp = 100;
        System.out.println(this.name + "は、眠って回復した！");
    }

    // 座る
    public void sit(int sec) {
        this.hp = sec;
        System.out.println(
            this.name + "は、" + sec + "秒座った！"
        );
        System.out.println(
        "HPが" + sec + "ポイント回復した"
        );


    }
    // 転ぶ
    public void slip() {
        this.hp -= 5;
        System.out.println(this.name + "は、転んだ！");
        System.out.println("5のダメージ");
    }
    // 逃げる
    public void run() {
        System.out.println(this.name + "は、逃げ出した！");
        System.out.println("GMEOVER");
        System.out.println("最終HPは" + this.hp + "でした");
    }
    public Hero(String name){
        this.hp =100;
        this.name = name;
    }

    public Hero(){
        this("ダミー");
    }
}

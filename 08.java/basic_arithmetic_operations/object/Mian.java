public class Mian {
    public static void main(String[] args) {
        // (以下の内容をjavaで記述していく)

        Sword s = new Sword();
        s.name = "炎の剣";
        s.damage = 10;
        // 勇者よ、この仮想世界に生まれよ！


        // 変数hにHeroクラスを代入してインスタンス化する
        // フィールドに初期値をセット
        Hero h = new Hero("ミナト");
        System.out.println(h.hp);
        System.out.println(h.name);
        // Hero h = new Hero();
        // h.name = "ミナト";
        // h.hp = 100;s
        //h.sword = s; swordフィールドに剣インスタンスを代入
        System.out.println("現在の武器は" + h.sword.name); //剣の名前を表示
        System.out.println("勇者" + h.name + "を生み出しました");
        // 勇者のメソッドを呼び出していく
        h.sit(5); // 5秒座る
        h.slip(); // 転ぶ
        h.sit(25); // 25秒座る
        h.run(); // 逃げる

        // もう一人ヒーローを生成する
        Hero h2 = new Hero();
        h2.name = "アカサ";
        h2.hp = 100;

        // 魔法使いを生成する
        Wizerd w = new Wizerd();
        w.name = "スガワラ";
        w.ph = 50;


        w.heal(h); //ミナトを回復させる


        // お化けキノコよ、この仮想世界に生まれよ！
        // キノコAを生成
        Matango m1 = new Matango();
        m1.hp = 50;
        m1.suffix = 'A';
        // キノコBを生成
        Matango m2 = new Matango();
        m1.hp = 48;
        m1.suffix = 'B';


        // 勇者よ、戦え！
        // お化けキノコよ、逃げろ！
        h.slip(); // 勇者が転ぶ
        m1.run(); // お化けキノコ「A」が逃げる
        m2.run(); //お化けキノコ「B」が逃げる
        h.run(); // 勇者が逃げる
        
    }
}

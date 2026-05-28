public class Mian {
    public static void main(String[] args) {

        Character[] c = new Character[5];
        c[0] = new Hero();
        c[1] = new Hero();
        c[1] = new Thief();
        c[1] = new Wizard();
        c[1] = new Wizard();
        // 部屋に泊まる
        for ( Character ch : c){
            ch.hp += 50;
        }

        /*        
        SuperHero sh = new SuperHero(); //スーパーヒーローのコンストラクタ動作がコンソールに表示される
        // Heroクラス
        Hero h = new Hero();
        h.run(); //「ミナトは逃げ出した！」が表示される

        // SuperHeroクラス
        SuperHero sh = new SuperHero();
        sh.run(); // 「ミナトは撤退した」が表示される

        Wizerd w = new Wizerd();
        Matango m = new Matango();
        w.name = "アサカ";
        w.attack(m);
        w.fireball(m);

        Slime s = new Slime();
        Monster mo = new Monster();
        s.run(); mo.run();
        */

        
    }
}

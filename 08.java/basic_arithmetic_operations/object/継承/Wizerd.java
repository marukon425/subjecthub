package inheritance;
// 魔法使いクラス
public class Wizerd extends Character {
    int np;
    public void attack(Matango m){
        System.out.println(this.name + "の攻撃！");
        System.out.println("敵に３ポイントのダメージ！");
        m.hp -= 3;
    }

    public void fireball(Matango m){
        System.out.println(this.name + "は火の玉を放った！");
        System.err.println("敵に20ポイントのダメージ");
        m.hp -= 20;
        this.mp -= 5;
    }

    // public void heal(Hero h){
    //     h.hp += 10;
    //     System.out.println(h.name + "のHPを10回復した！");
    // }
}

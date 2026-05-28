// 魔法使いクラス
public class Wizerd {
    String name;
    int ph;
    public void heal(Hero h){
        h.hp += 10;
        System.out.println(h.name + "のHPを10回復した！");
    }
}

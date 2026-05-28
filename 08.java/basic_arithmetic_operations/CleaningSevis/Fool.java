package basic_arithmetic_operations.CleaningSevis;

import inheritance.Matango;

public class Fool extends Character implements Human {
    // キャラクターからhpやnemなどのフィールドを継承している
    // キャラクターから継承した抽象メソッドattack()を実装
    public void attack(Matango m){
        System.out.println(this.name + "は戦わずに遊んでいる");
    }

    void talk();
    void watch();
    void hear();
    void run();
}

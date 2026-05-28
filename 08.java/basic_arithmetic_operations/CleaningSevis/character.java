package basic_arithmetic_operations.CleaningSevis;

import inheritance.Matango;

public class character {
    String name;
    int hp;
    public void run(){
        System.out.println(this.name + "は逃げ出した");
    }
    public abstract void attack(Matango m){}
}

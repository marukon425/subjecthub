package 演習.回答.共通問題集.基本演算.基本演算13_1;

// Personクラスを継承
public class Cook extends Person{
    String specialties;
    void Cook(String name, String job, String specialties){
        super(name, job);
        this.specialties = specialties;
    }
    void introduct(){
        System.out.println("氏名：" + super.name);
        System.out.println("職種：" + super.job);
        System.out.println("得意料理：" + this.specialties);    
    }
}

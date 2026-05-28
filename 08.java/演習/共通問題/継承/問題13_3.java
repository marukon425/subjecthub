package 共通問題.継承;



// Teachr ,Cook → personの子クラス

public class 問題13_3 {
    public static void main(String[] args) {
        Teacher T1 = new Teacher("竹井一馬", "教員", "情報処理");
        T1.introduct();
        Cook C1 = new Cook("大原太郎", "シェフ", "オムライス");
        C1.introduct();

    }
}

interface Person {
    void introduct();
}

class Teacher implements Person{
    String name;
    String job;
    String subject;

    Teacher(String name, String job, String subject){
        this.name = name;
        this.job = job;
        this.subject = subject;
    }



    @Override 
    public void introduct() {
        // TODO Auto-generated method stub
        System.out.println("氏名：" + this.name);
        System.out.println("職種：" + this.job);
        System.out.println("担当教科：" + this.subject);
    }
}

class Cook implements Person{
    String name;
    String job;
    String specialites;

    Cook(String name, String job, String specialites){
        this.name = name;
        this.job = job;
        this.specialites = specialites;
    }



    @Override 
    public void introduct() {
        // TODO Auto-generated method stub
        System.out.println("氏名：" + this.name);
        System.out.println("職種：" + this.job);
        System.out.println("得意料理：" + this.specialites);
    }}
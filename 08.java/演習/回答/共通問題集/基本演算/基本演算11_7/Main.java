package 演習.回答.共通問題集.基本演算.基本演算11_7;

public class Main {
    Student stu_A = new Student("A", "001", 89, 65, 88);
    Student stu_B = new Student("B", "002", 80, 95, 64);
    Student stu_C = new Student("C", "003", 70, 80, 98);
    ll
    stu_A.output_info();

}

// publicを除けば一個のファイルに何個もクラスが作れる
class Student {
    String name;
    String stunum;
    double japan;
    double math;
    double english;


    Student(String name, String stunum, double japan, double math, double english){
        this.name = name;
        this.stunum = stunum;
        this.japan = japan;
        this.math = math;
        this.english = english;
    }

    // 平均点算出のメソッド
    public double get_avg(){
        return (this.japan + this.english + this.math)/3;
    }

    // 出力
    public void output_info(){
        System.out.println(this.stunum+"番"+" "+this.name+"さん"+"    "+this.japan+"点"+"  "+this.math+"点"+"  "+this.english+"点");
    }
    
}

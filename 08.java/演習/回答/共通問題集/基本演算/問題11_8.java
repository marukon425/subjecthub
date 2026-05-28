package 演習.回答.共通問題集.基本演算;

public class 問題11_8 {    
    public static void main(String[] args) {
        Person a = new Person("A", 18, "千代田区神田保町1-1", "aaa@mail.com");
        Person b = new Person("C", -3, "横浜市西区桜木町2-2-2", "bbb@mail.com");
        Person c = new Person("C", 20, "さいたま市北区大原3-3", "@mail.com");
        

        System.out.println(a.j_age());
        System.out.println(a.j_mail());
        System.out.println(a.output_info());
        System.out.println(b.output_info());
        System.out.println(c.output_info());
    }    
}

class Person {
    String name;
    int age;
    String adress;
    String mail;

    public Person(String name, int age, String adress, String mail){
        this.name = name;
        this.age = age;
        this.adress = adress;
        this.mail = mail;
    }

    boolean j_age(){
        if (this.age >= 0 && this.age < 100) {
            // System.out.println("正常");
            return true;
        }else{
            // System.out.println("異常");
            return false;
        }
    }

    boolean j_mail(){
        boolean j = false;
        for (int i = 0; i < this.mail.length(); i++){
            if (this.mail.charAt(i) == '@' && i > 0) {
                j = true;
            }
        }
        return j;
    }


    String output_info(){
        String judge;
        if (j_age() && j_mail()) {
            judge = "正常";
        }else{
            judge = "異常";
        }
        return this.name+"さん　"+this.age+"歳　"+this.adress+"　"+this.mail+" "+judge;
    }
    
}
/*
Person

氏名、年齢、性別、身長、体重を引数として受け取るコンストラクタ
コンストラクタ：引数なし・クラス名と同じ名前・newで呼び出す・インスタンスの初期化

個人情報を表示するメソッド

BMIを表示するメソッド

適正体重を表示するメソッド


*/
public class Person {
    String name;
    int age;
    String gender;
    double height;
    double weight;
    
    public Person(String name, int age, String gender, double height, double weight){
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.height = height;
        this.weight = weight;
    }

    // 個人情報を表示するメソッド
    public void disp_info(){
        System.out.print("名前：" + name );
        System.out.print("年齢：" + age );
        System.out.print("性別：" + gender );
        System.out.print("身長(cm)：" + height );
        System.out.print("体重(kg)：" + weight );
    }

    // BMI値を表示するクラス
    public double get_bmi(){
        double h = height / 100; // 身長をm単位にする
        double bmi = weight / (h * h);
        System.out.println("BMI 値 = " + bmi);

        return bmi;
    }

    // 肥満度判定を表示するクラス
    public void get_obestity(double bmi){
        String decision = "";
        if (bmi < 18.5) {
            decision = "低体重(やせ型)";
        }else if (bmi >= 18.5 && bmi < 25.0) {
            decision = "普通体重";
        }else if (bmi >= 25.0 && bmi < 30.0) {
            decision = "肥満 (1度)";
        }else if (bmi >= 30.0 && bmi < 35.0) {
            decision = "肥満 (2度)";
        }else if (bmi >= 35.0 && bmi < 40.0) {
            decision = "肥満 (3度)";
        }else if (bmi >= 40.0) {
            decision = "肥満 (4度)";
        }

        System.out.println("肥満度の判定 = " + decision);
    }

    // 適正体重を表示するクラス
    public void get_suitable_weight(){
        double h = height / 100; 
        double desirable_weight = (h * h) * 22;
        System.out.println("適正体重 = " + desirable_weight); 
    }
}

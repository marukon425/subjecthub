public class Main {
    public static void main(String[] args) {
        // インスタンス化
        Person p = new Person("鈴木太郎", 42, "男性", 179.3, 72.7);
        p.disp_info();
        double bmi = p.get_bmi();
        p.get_obestity(bmi);
        p.get_obestity(bmi);
    }
}

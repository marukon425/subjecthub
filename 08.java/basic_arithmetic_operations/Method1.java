package basic_arithmetic_operations;

public class Method1 {
    public static void main(String[] args) {
        System.out.println("メソッドを呼び出します");
        System.out.println("奏");
        System.out.println("朝香");
        System.out.println("菅原");
        System.out.println("メソッドの呼び出しが終わりました");
    }

    //                             ↓ 引数に「文字型」のname変数を設定   
    public static void hello(String name) {
        System.out.println(name + "さん、こんにちは");
    }
}

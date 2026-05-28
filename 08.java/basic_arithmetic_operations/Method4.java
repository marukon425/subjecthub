package basic_arithmetic_operations;

// オーバーロード(引数が異なる場合)
/*
基本的にメソッドの名前は1つしか使用できないが、この場合は複数使用できる「便利機能」
*/
public class Method4 {
    // 1つ目のメソッド
    public static int add(int x, int y) {
        return x + y;
    }

    // 2つ目のメソッド
    public static double add(double x, double y) {
        return x + y;
    }

    // 3つ目のメソッド
    public static String add(String x, String y) {
        return x + y;
    }

    public static void main(String[] args) {
        // ↓ 1つ目のメソッドが呼び出される
        System.out.println(add(10, 20));

        // ↓ 2つ目のメソッドが呼び出される
        System.err.println(add(3.5, 2.7));
        
        // ↓ 3つ目のメソッドが呼び出される
        System.out.println(add("hello", "world"));
    }


    /*
    3つのaddメソッドがあるけど引数の数、引数,戻り値の型、が違ったら同じメソッドが何個でも作れる
    */
}

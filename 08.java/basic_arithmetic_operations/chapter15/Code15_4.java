package basic_arithmetic_operations.chapter15;


// テスト出る
public class Code15_4 {
    public static void main(String[] args) {
        // StringBuilder:文字列を結合するクラスメソッド
        StringBuilder sb = new StringBuilder();
        // StringBuilderに1万回文字列結合
        for (int i = 0; i < 10000; i++){
            sb.append("java");
        }
        String s = sb.toString();
        // 一万のjavaを改行なしで出力
        System.out.println(s);
    }
}

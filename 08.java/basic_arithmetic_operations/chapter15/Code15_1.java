package basic_arithmetic_operations.chapter15;

public class Code15_1 {
    public static void main(String[] args) {
        String s1 = "スッキリ";
        String s2 = "java";
        String s3 = "java";
        if (s2.equals(s3)) {
            System.out.println("s2とs3は等しい");
        }
        if (s2.equalsIgnoreCase(s3)) {
            System.out.println("s2とs3はケースを区別しなければ等しい");
        }
        System.out.println("s1の長さは" + s1.length() + "です");
    }
}

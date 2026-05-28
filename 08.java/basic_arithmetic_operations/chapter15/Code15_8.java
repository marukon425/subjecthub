package basic_arithmetic_operations.chapter15;

public class Code15_8 {
    public static void main(String[] args) {
        String s = "abc,def:ghi";
        String words = s.replaceAll("[beh]","X");
        System.out.println(words);

    }
}

package 演習.回答.共通問題集.基本演算;

public class 基本演算9_3 {
    public static void repeat(String word, int repeat){
        for (int i = 0; i < repeat; i++){
            System.out.println(word);
        }
    }

    public static void main(String[] args) {
        repeat("Hwllo", 3);
        repeat("Good morning",6);
    }
}

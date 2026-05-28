package basic_arithmetic_operations;


// 条件分岐
public class Test10 {
    public static void main(String[] args) {
        boolean tenki = true;
        if (tenki == true) {
            System.out.println("洗濯をします");
            System.out.println("散歩に行きます");
        }else{
            System.out.println("映画を見ます");
        }


        // 文字列を比較するときの条件分岐
        String text = "これは文字列";
        if (text.equals("これは文字列")) {
            System.out.println("これは文字列です");
        }


        // snd orの書き方
        String name = "丸山";
        String name1 = "円山";
        // and
        if (name.equals("丸山") && name1.equals("円山")) {
            System.out.println("どっちもまるやまです");
        // or
        }else if (name.equals("丸山") || name1.equals("円山")) {
            System.out.println("どちらかが「丸山です」");
        }
    }
}

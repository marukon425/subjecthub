package inheritance;
public class Matango {
    int hp; // 体力

    // final : 今後この変数の値は変えられなくできる機能(定数フィールド)
    // 変数名を大文字にすることで使える
    final int LEVEL = 10;
    char suffix;
    public void run(){
        System.out.println("お化けキノコ" + this.suffix + "は逃げ出した！");
    }

    
}

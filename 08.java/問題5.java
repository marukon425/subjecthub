import java.util.Scanner;

public class 問題5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("現在のパスワードを入力してください：");
        StringBuilder sb = new StringBuilder(sc.nextLine());
        System.out.println("セキュリティ上の問題を発見しました。");
        System.out.println("セキュリティを強化したパスワードを作成しました。");

        for (int i = 0; i < sb.length(); i++) {
            System.out.print(sb.charAt(sb.length() - 1 - i));
        }
    }
}

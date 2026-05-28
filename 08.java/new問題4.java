import java.util.Scanner;

public class new問題4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] lst = new int[5];

        for(int i = 0; i < 5; i++){
            System.out.print((i + 1) + "教科目の点数を入力してください");
            int num = sc.nextInt();
            if (num < 0 || num > 100) {
                System.out.println("不正な点数を検知しました。０点とします。");
                num = 0;
                lst[i] = num;
            }else
                lst[i] = num;
        }

        int num1 = sum(lst);

        System.out.println();
    }

    public static double sum(int[] lst){
        int num = 0;
        for (int i = 0; i < 5; i++){
            num += lst[i];
        }
        return num;
    }
    public static int avg(int[] lst){
        int num = 0;
        for (int i = 0; i < 5; i++){
            num += lst[i];
        }
        double avg = num / 5;
        return avg;
    }
}

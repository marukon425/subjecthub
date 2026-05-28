import java.util.Scanner;

public class 問題4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("1教科目の点数を入力してください");
        int num1 = sc.nextInt();
        if (num1 < 0 || num1 > 100) {
            System.out.println("不正な値を検知しました。０点とします。");
            num1 = 0;
        }

        System.out.println("2教科目の点数を入力してください");
        int num2 = sc.nextInt();
        if (num2 < 0 || num2 > 100) {
            System.out.println("不正な値を検知しました。０点とします。");
            num2 = 0;
        }        
        
        System.out.println("3教科目の点数を入力してください");
        int num3 = sc.nextInt();
        if (num3 < 0 || num3 > 100) {
            System.out.println("不正な値を検知しました。０点とします。");
            num3 = 0;
        }        System.out.println("4教科目の点数を入力してください");
        int num4 = sc.nextInt();
        if (num4 < 0 || num4 > 100) {
            System.out.println("不正な値を検知しました。０点とします。");
            num4 = 0;
        }        System.out.println("5教科目の点数を入力してください");
        int num5 = sc.nextInt();
        if (num5 < 0 || num5 > 100) {
            System.out.println("不正な値を検知しました。０点とします。");
            num5 = 0;
        }

            sum(num1, num2, num3, num4, num5);
            avg(num1, num2, num3, num4, num5);
    }

    public static void sum(int num1,int num2,int num3,int num4,int num5){
        System.out.println("合計点：" + (num1+num2+num3+num4+num5));
    }

    public static void avg(int num1,int num2,int num3,int num4,int num5){
        System.out.println("平均点：" + ((num1+num2+num3+num4+num5)/5));
    }
    }






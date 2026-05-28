package 共通問題.継承;

import java.util.Scanner;

public class 問題11_7 {
    
}

// CalcExcuter → CalcAddSubのインスタンス、CalcMultiDivのインスタンスを多重継承

class CalcAddSub{
    int num1;
    int num2;

    public CalcAddSub(int num1, int num2){
        this.num1 = num1;
        this.num2 = num2;
    }

    public void CalcAdd(int num1, int num2){
        System.out.println("足し算の結果：" + (num1 + num2));
    }

    public void CalcSub(int num1, int num2){
        System.out.println("引き算の結果：" + (num1 - num2));
    }
}


class CalcMultiDiv {
    int num1;
    int num2;

    public CalcMultiDiv(int num1, int num2){
        this.num1 = num1;
        this.num2 = num2;
    }    

    
}


class Cra {
    double num3, num4, num5;
    
}

package basic_arithmetic_operations.コレクションフレームワーク;

import java.util.*;

public class Practice3 {
    
    public static void doit(List <String> lst) {
        System.out.println("クラス名は: " + lst.getClass());
        System.out.println("変数名は: "  + lst);
    }
    public static void main(String[] args) {
        List<String> List = new ArrayList<>();
    
        String[] stLst = {"えい", "えい", "おー"};
    
        List<String> stLst2 = new ArrayList<>(); 
        stLst2.add("右");
        stLst2.add("左");
        stLst2.add("右");

        System.out.println(doit(stLst));
    }

}

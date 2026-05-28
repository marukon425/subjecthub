package basic_arithmetic_operations.コレクションフレームワーク;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Sample1_4 {
    public static void main(String[] args) {
        // リストを作成
        List<Integer> lst = new ArrayList<>();

        lst.add(1); lst.add(2);
        System.out.println("list 変数のクラス" + lst.getClass());
        System.out.println("list の中身" + lst);

        // リストを配列に変換
        Integer[] lst2Ary = lst.toArray(new Integer[lst.size()]);
        System.out.println("lst2 変数クラス: " + lst2Ary.getClass());
        System.out.println("lst2 変数の中身" + Arrays.toString(lst2Ary));

        // 配列をリストに変換
        List<Integer> ary2Lst = Arrays.asList(lst2Ary);
        System.out.println("ary2lst 変数のクラス: " + ary2Lst.getClass());
        System.out.println("ary2Lst 変数の中身: " + ary2Lst);
    }
}

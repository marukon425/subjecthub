package basic_arithmetic_operations.コレクションフレームワーク;
import java.util.*;
public class Sample1_5 {
    public static void main(String[] args) {
        // 配列を作成
        Integer[] ary = {1, 2};
        System.out.println("クラス名: " + ary.getClass());
        System.out.println("中身: " + Arrays.toString(ary));

        // 配列をリストに変換
        List<Integer> list = new ArrayList<>(Arrays.asList(ary));
        System.out.println("クラス名: " + list.getClass());

        // 要素を追加
        list.add(3);
        // 中身を表示
        System.out.println("中身: " + list);
    }
}

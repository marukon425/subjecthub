package basic_arithmetic_operations.コレクションフレームワーク;
import java.util.Random;
public class Practice1 {
    public static void main(String[] args) {

        // 1.
        int num = new Random().nextInt(5) + 6;
        int[] list = new int[num];
        for (int i = 0; i < list.length; i++){
            list[i] = i;
        }

        for (int i : list){
            System.out.print(i);
        }
    }   
}

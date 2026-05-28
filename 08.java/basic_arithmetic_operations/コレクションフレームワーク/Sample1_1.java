import java.util.ArrayList;


public class Sample1_1 {
    public static void main(String[] args){
        ArrayList<Integer> a1 = new ArrayList<Integer>();

        a1.add(10);
        a1.add(20);

        int a = a1.get(0);

        System.out.println(a);
    }
    
}
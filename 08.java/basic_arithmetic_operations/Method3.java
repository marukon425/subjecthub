package basic_arithmetic_operations;


// 戻り値の利用
public class Method3 {

    // 戻り値を設定するときは「void」じゃなくて戻り値の「型」を書く
    public static int add(int x, int y){
        int ans = x + y;
        return ans;
    }
    public static void main(String[] args) {
        int ans = add(100, 10);
        System.out.println("100 + 10 = "+ans);
    }
}

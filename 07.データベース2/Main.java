import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;



import java.util.Scanner;



public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] num_lst = new int[n];
        String[] play_lst = new String[n];

        // 代入
        for(int i = 0; i < n; i++){
            String[] p = sc.nextLine().split(" ");
            num_lst[i] = Integer.parseInt(p[0]);
            play_lst[i] = p[1];
        }

        // ソート(バブル)
        int temp =0;
        for(int i = 0; i < n; i++){
            for(int j = 0; i < n-i ; j++){
                if (num_lst[i] > ) {
                    
                }
            }
        }

    }
}





// String[] lst = sc.nextLine().split(" ");
// // 池の1週の距離(Nメートル)
// int N = Integer.parseInt(lst[0]);
// // 1ターンでKメートル歩く
// int K = Integer.parseInt(lst[1]);
// // Tターン歩く
// int T = Integer.parseInt(lst[2]);

// int N_N = N;
// for (int i = 0; i < T; i++){
//     if (N_N - K < 0) {
//         int minus = N_N - K;
//         N_N = N - minus;
//     }else{
//         N_N -= K;
        
//     }
// }
// String j;
// if (N_N == 0) {
//     j = "YES";
// }else{
//     j = "NO";
// }
// System.out.println(j);
package basic_arithmetic_operations.chapter18;
import java.io.FileReader;
import java.util.*;;

public class Code18_1 {
    public static void main(String[] args) throws Exception {
        FileReader fr = new FileReader("data.txt");

        int input = fr.read();
        while (input != -1) {
            System.out.println((char)input);
            input = fr.read();
        }
        fr.close();
    }
}

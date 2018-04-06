import java.io.File;
import java.util.Scanner;

public class SnakesAndLadders {

    static int quickestWayUp(int[][] ladders, int[][] snakes) {
        // Complete this function
        return 0;
    }

    public static void main(String[] args) throws Exception{
        File file = new File("tests/SnakesAndLadders.txt");
        Scanner scanner = new Scanner(file);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            int n = in.nextInt();
            int[][] ladders = new int[n][2];
            for(int ladders_i = 0; ladders_i < n; ladders_i++){
                for(int ladders_j = 0; ladders_j < 2; ladders_j++){
                    ladders[ladders_i][ladders_j] = in.nextInt();
                }
            }
            int m = in.nextInt();
            int[][] snakes = new int[m][2];
            for(int snakes_i = 0; snakes_i < m; snakes_i++){
                for(int snakes_j = 0; snakes_j < 2; snakes_j++){
                    snakes[snakes_i][snakes_j] = in.nextInt();
                }
            }
            int result = quickestWayUp(ladders, snakes);
            System.out.println(result);
        }
        in.close();
    }
}

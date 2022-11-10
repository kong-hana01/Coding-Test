import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = Integer.parseInt(in.nextLine());
        int[][] board = new int[101][101];
        for (int i = 0; i < n; i++) {
            String[] location = in.nextLine().split(" ");
            int x = Integer.parseInt(location[0]), y = Integer.parseInt(location[1]);
            for (int j = 0; j < 10; j++) {
                for (int k = 0; k < 10; k++) {
                    board[j+x][k+y] = 1;
                }
            }
        }
        int result = 0;
        for (int i = 1; i < 101; i++) {
            result += Arrays.stream(board[i]).sum();
        }
        System.out.println(result);
    }
}
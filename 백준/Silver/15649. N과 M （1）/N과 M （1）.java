import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
//        int n = Integer.parseInt(in.nextLine());
        String[] input = in.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);
        backtracking(new ArrayList<>(), n, m);
    }

    private static void backtracking(List<Integer> sequence, int n, int maxLength) {
        if (sequence.size() == maxLength) {
            sequence.stream().forEach((x) -> System.out.printf(x + " "));
            System.out.println();
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (sequence.contains(i)) {
                continue;
            }
            sequence.add(i);
            backtracking(sequence, n, maxLength);
            sequence.remove(sequence.size()-1);
        }
    }
}
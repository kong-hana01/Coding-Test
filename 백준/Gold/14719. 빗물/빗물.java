import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        List<Integer> collect = Arrays.stream(s.split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());
        Integer H = collect.get(0);
        Integer W = collect.get(1);
        s = sc.nextLine();
        List<Integer> blockBoard = Arrays.stream(s.split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());

        int result = 0;
        for (int i = 0 ; i < H; i++) {
            boolean isFill = false;
            int num = 0;
            for (int j = 0; j < W; j++) {
                if (blockBoard.get(j) > i && !isFill) {
                    isFill = true;
                    num = 0;
                    continue;
                }
                if (blockBoard.get(j) > i) {
                    result += num;
                    num = 0;
                    continue;
                }
                num += 1;
            }
        }
        System.out.println(result);
    }
}
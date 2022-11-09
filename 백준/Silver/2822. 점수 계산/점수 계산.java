import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        List<List<Integer>> score = new ArrayList<>();
        for (int i = 1; i <= 8; i++) {
            List<Integer> temp = new ArrayList<>();
            temp.add(i);
            temp.add(Integer.valueOf(in.nextInt()));
            score.add(temp);
        }
        score = score.stream()
                .sorted(Comparator.comparingInt(l -> -l.get(1)))
                .collect(Collectors.toList());

        List<Integer> resultOrder = new ArrayList<>();
        Integer resultScore = 0;
        for (int i = 0; i <= 4; i++) {
            resultScore += score.get(i).get(1);
            resultOrder.add(score.get(i).get(0));
        }
        System.out.println(resultScore);
        resultOrder.stream()
                .sorted(Comparator.naturalOrder())
                .forEach(num -> System.out.print(num + " "));
    }
}
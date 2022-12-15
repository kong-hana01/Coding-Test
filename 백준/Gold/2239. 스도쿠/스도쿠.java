import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        // backtracking
        Scanner scanner = new Scanner(System.in);
        List<List<Integer>> board = new ArrayList<>();
        int countOfZero = 0;
        for (int i = 0; i < 9; i++) {
            List<Integer> row = Arrays.stream(scanner.nextLine()
                            .split(""))
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());
            board.add(row);
            countOfZero += row.stream().filter(x -> x.equals(0)).count();
        }
        boolean[][] checkBox = initBox(board);
        boolean result = backtracking(board, checkBox, 0, 0, countOfZero);
        board.stream().forEach(x -> {
            x.stream().forEach(System.out::print);
            System.out.println();
        });
    }
    
    
    public static boolean backtracking(List<List<Integer>> board, boolean[][] checkBox, int row, int col, int countOfZero) {

        if (countOfZero == 0) {
            return true;
        }

        int nextRow = row;
        int nextCol = getNextStep(col);
        if (nextCol == 0) {
            nextRow = row + 1;
        }

        if (!board.get(row).get(col).equals(0)) {
            if (backtracking(board, checkBox, nextRow, nextCol, countOfZero)) {
                return true;
            }
            return false;
        }

        for (int num = 1; num <= 9; num++) {
            if (promising(board, checkBox, row, col, num)) {
                board.get(row).set(col, num);
                int boxNum = getBoxNum(row, col);
                checkBox[boxNum][num] = true;
                if (backtracking(board, checkBox, nextRow, nextCol, countOfZero - 1)) {
                    return true;
                }
                board.get(row).set(col, 0);
                checkBox[boxNum][num] = false;
            }
        }
        return false;
    }

    public static boolean promising(List<List<Integer>> board, boolean[][] checkBox, int row, int col, int num) {

        // 가로 세로에 대해 중복값이 있는지 확인
        for (int i = 0; i < 9; i++) {
            if (board.get(row).get(i).equals(num)) {
                return false;
            }
            if (board.get(i).get(col).equals(num)) {
                return false;
            }
        }
        // checkBox에 없다면 True
        int boxNum = getBoxNum(row, col);
        return !checkBox[boxNum][num];
    }

    public static boolean[][] initBox(List<List<Integer>> board) {
        boolean[][] box = new boolean[9][10];
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                int num = board.get(row).get(col);
                int boxNum = getBoxNum(row, col);
                box[boxNum][num] = true;
            }
        }
        return box;
    }

    public static int getBoxNum(int row, int col) {
        return (row / 3) * 3 + (col / 3);
    }

    public static int getNextStep(int step) {
        if (step == 8) {
            return 0;
        }
        return step + 1;
    }
}
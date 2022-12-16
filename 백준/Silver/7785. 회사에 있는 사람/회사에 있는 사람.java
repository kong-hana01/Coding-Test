import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Integer.min;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        HashMap<String, Boolean> log = new HashMap<>();
        for (int i = 0; i < n; i++) {
            String[] s = sc.nextLine().split(" ");
            if (s[1].equals("enter")) {
                log.put(s[0], true);
            } else {
                log.remove(s[0]);
            }
        }
        for (String name: log.keySet().stream().sorted(Collections.reverseOrder()).collect(Collectors.toList())) {
            System.out.println(name);
        }
    }
}
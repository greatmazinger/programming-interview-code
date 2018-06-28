import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

class looplist {  
    public static void main(String args[]) {
        List<Integer> list = new ArrayList<>();
        // Method 1: classic for loop
        for (int i = 0; i < 10; i++) {
            list.add(i);
        }
        for (int i = 0; i < 10; i++) {
            System.out.println("for: " + list.get(i));
        }
        // Method 2: while loop
        list.clear();
        int j = 0;
        while (j < 10) {
            list.add(j);
            j++;
        }
        j = 0;
        while (j < 10) {
            System.out.println("which: " + list.get(j));
            j++;
        }
        // Method 3: Java 8 streams
        IntStream.range(0, 10).forEach(
            n -> {
                list.add(n);
            }
        );
        IntStream.range(0, 10).forEach(
            n -> {
                System.out.println("stream: " + list.get(n));
            }
        );
    }
}

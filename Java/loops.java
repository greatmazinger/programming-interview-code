import java.util.stream.IntStream;

class loops {  
    public static void main(String args[]) {
        // Method 1: classic for loop
        for (int i = 0; i < 10; i++) {
            System.out.println("for: " + i );
        }
        // Method 2: while loop
        int j = 0;
        while (j < 10) {
            System.out.println("which: " + j);
            j++;
        }
        // Method 3: Java 8 streams
        IntStream.range(0, 10).forEach(
            n -> {
                System.out.println("stream: " + n);
            }
        );
    }
}

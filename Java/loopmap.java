import java.util.HashMap;
import java.util.Map;
import java.util.stream.IntStream;

class loopmap {  
    public static void main(String args[]) {
        Map<Integer, String> map = new HashMap<>();
        // Method 1: classic loop over map
        for (int i = 0; i < 10; i++) {
            map.put(i, Integer.toString(i*i));
        }
        for (Map.Entry<Integer, String> entry : map.entrySet()) {
            System.out.println("for entrySet: " + entry.getKey() + " -> " + entry.getValue());
        }
        // Method 2: Java 8 stream + forEach
        map.entrySet().stream()
            .forEach(
                entry -> {
                    System.out.println("stream: " + entry.getKey() + " -> " + entry.getValue());
                }
            );
    }
}

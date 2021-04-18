package net.veroy.prototype;

import java.io.IOException;
import java.lang.Process;
import java.lang.ProcessBuilder;

/**
 * INPUT:
 *    - java path
 *    - jar path
 *    - CSV path
 */
/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        try {
            Process process = new ProcessBuilder( "/usr/lib/jvm/java-11-openjdk/bin/java",
                                                  "-jar", "/mnt/NVM/src/00-BLACKROCK/MINE/helloworld/target/helloworld-1.0-SNAPSHOT.jar",
                                                  "App" ).start();
            String result = new String(process.getInputStream().readAllBytes());
            String resultErr = new String(process.getErrorStream().readAllBytes());
            int exitCode = process.waitFor();
            System.out.println("RESULT: " + result);
            System.out.println("RESULT ERR: " + resultErr);
        } catch (IOException ioexc) {
            System.out.println("IOException: " + ioexc.getMessage());
        } catch (InterruptedException intexc) {
            System.out.println("InterruptedException: " + intexc.getMessage());
        }
    }
}

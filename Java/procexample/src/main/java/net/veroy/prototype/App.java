package net.veroy.prototype;

import java.io.IOException;
import java.lang.Process;
import java.lang.ProcessBuilder;
import java.util.ArrayList;
import java.util.List;

/**
 * Tester for JavaProc class:
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        String cmd = "/mnt/NVM/src/programming-interview-code/Java/procexample/lua/runPkg";
        List<String> helloworldArgs = new ArrayList<>();
        helloworldArgs.add("TODO");
        JavaProc process = new JavaProc(cmd, helloworldArgs);
        int exitCode = process.runCmd();
        // TODO String result = new String(process.getInputStream().readAllBytes());
        // TODO String resultErr = new String(process.getErrorStream().readAllBytes());
        // System.out.println("RESULT: " + result);
        // System.out.println("RESULT ERR: " + resultErr);
    }
}

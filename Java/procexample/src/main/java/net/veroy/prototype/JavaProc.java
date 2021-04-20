package net.veroy.prototype;

import java.io.IOException;
import java.lang.Process;
import java.lang.ProcessBuilder;
import java.util.ArrayList;
import java.util.List;

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
public class JavaProc 
{
    private final String cmd;
    private final List<String> opts;

    public JavaProc(String cmd, List<String> opts) {
        this.cmd = cmd;
        this.opts = opts;
    }

    public int runCmd() {
        try {
            ArrayList<String> procList = new ArrayList(this.opts);
            procList.add(0, this.cmd);
            Process process = new ProcessBuilder(procList).start();
            String result = new String(process.getInputStream().readAllBytes());
            String resultErr = new String(process.getErrorStream().readAllBytes());
            int exitCode = process.waitFor();
            System.out.println("RESULT: " + result);
            System.out.println("RESULT ERR: " + resultErr);
        } catch (IOException ioexc) {
            System.out.println("IOException: " + ioexc.getMessage());
            return -1;
        } catch (InterruptedException intexc) {
            System.out.println("InterruptedException: " + intexc.getMessage());
            return -2;
        }
        return 0; // TODO
    }
}

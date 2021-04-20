package net.veroy.prototype;

import java.io.File;
import java.io.IOException;
import java.lang.Process;
import java.lang.ProcessBuilder;
import java.util.ArrayList;
import java.util.List;

import lombok.Getter;

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

    @Getter
    private String result;

    @Getter
    private String resultErr;

    public JavaProc(String cmd, List<String> opts) {
        this.cmd = cmd;
        this.opts = opts;
    }

    public int runCmd() {
        try {
            File cmdFile = new File(this.cmd);
            if (!cmdFile.exists()) {
                throw new IllegalStateException("File doesn't exist: " + this.cmd);
            }
            String workingDir = cmdFile.getParent();

            ArrayList<String> procList = new ArrayList(this.opts);
            procList.add(0, this.cmd);

            Process process = new ProcessBuilder(procList).directory(new File(workingDir))
                                                          .start();
            this.result = new String(process.getInputStream().readAllBytes());
            this.resultErr = new String(process.getErrorStream().readAllBytes());
            return process.waitFor();
        } catch (IOException ioexc) {
            System.out.println("IOException: " + ioexc.getMessage());
            return -1;
        } catch (InterruptedException intexc) {
            System.out.println("InterruptedException: " + intexc.getMessage());
            return -2;
        }
    }
}

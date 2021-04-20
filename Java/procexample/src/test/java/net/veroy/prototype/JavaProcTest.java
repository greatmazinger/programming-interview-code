package net.veroy.prototype;

import static org.junit.Assert.assertTrue;

import java.io.File;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

import org.junit.Before;
import org.junit.Test;

/**
 * Unit test for JavaProc.
 */
public class JavaProcTest 
{
    private JavaProc javaProc;

    @Before
    public void setup() {
    }

    
    @Test
    public void shouldRunCmdTest() {
        String cmdFilename = "runPkg";
        ClassLoader classLoader = getClass().getClassLoader();
        File file = new File(classLoader.getResource(cmdFilename).getFile());
        String cmdPath = file.getPath();

        List<String> helloworldArgs = new ArrayList<>();
        helloworldArgs.add("TODO");
        JavaProc process = new JavaProc(cmdPath, helloworldArgs);
        int exitCode = process.runCmd();
        String result = process.getResult();
        String resultErr = process.getResultErr();
        System.err.println("RESULT:" + result);
        System.err.println("RESULT-ERR:" + resultErr);
        // Check that the first script ran:
        assertTrue(result.contains("MOCK: runPkg-LUA"));
        // Check that the second script ran:
        assertTrue(result.contains("MOCK: authNShell-LUA"));
        // Check that the Java program ran:
        assertTrue(result.contains("Hello World!"));
    }
}

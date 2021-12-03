import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class HardSolution {
    public static void main(String[] argv) throws IOException {
        int x = 0, y = 0, aim = 0;
        for(String line : Files.readAllLines(Path.of("input"))) {
            String[] parsed = line.split(" ");
            switch(parsed[0]){
                case "up":
                aim -= Integer.parseInt(parsed[1]);
                break;
                case "down":
                aim += Integer.parseInt(parsed[1]);
                break;
                case "forward":
                Integer dist = Integer.parseInt(parsed[1]);
                x += dist;
                y += dist*aim;
            }
        }
        System.out.println(x * y);
                

    }
}

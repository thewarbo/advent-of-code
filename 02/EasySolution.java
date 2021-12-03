import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;
import java.util.stream.Collectors;

public class EasySolution {
    public static void main(String[] argv) throws IOException {
        Map<String, Integer> result = Files.lines(Path.of("input")).map(t -> t.split(" "))
                .collect(Collectors.groupingBy(t -> t[0], Collectors.summingInt(t -> Integer.parseInt(t[1]))));
        System.out.println(result);
        System.out.println(Math.abs(result.get("up") - result.get("down")) * result.get("forward"));
    }

}
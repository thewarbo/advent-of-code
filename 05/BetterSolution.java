import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class BetterSolution {
    static Pattern pattern = Pattern.compile("(\\d+),(\\d+) -> (\\d+),(\\d+)");

    public static int[] segmentFromText(String line){
        int[] value = new int[4];
        Matcher m = pattern.matcher(line);
        m.find();
        for(int i = 0; i<4; i++){
            value[i] = Integer.valueOf(m.group(i+1));
        }
        return value;
    }

    static List<int[]> listFromSegment(int[] segment){
        List<int[]> value = new ArrayList<>();
        int deltaX = Integer.signum(segment[2] - segment[0]);
        int deltaY = Integer.signum(segment[3] - segment[1]);
        for(int x = segment[0], y = segment[1]; x != segment[2] || y != segment[3]; x+= deltaX, y+= deltaY){
            value.add(new int[]{x, y});
        }
        value.add(new int[]{segment[2], segment[3]});
        return value;
    }
    public static void main(String[] args) throws IOException {
        Long result = 
        Files.lines(Path.of("05/input"))
           .map(BetterSolution::segmentFromText)
           .map(BetterSolution::listFromSegment)
           .flatMap(List::stream)
           .collect(Collectors.groupingBy(x ->( x[0] + "," + x[1]), Collectors.counting()))
           .entrySet().stream()
           .filter(x -> (x.getValue() > 1))
           .collect(Collectors.counting());
           System.out.println(result);

    }
}

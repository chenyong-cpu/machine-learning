import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class regrex {
    
    public static void main(String[] args) {
        String str = "(中文问号？123???英文)问号?我是华丽[的制表符\t]我是华丽{的空格符 我是华丽}的换行符\n";
        String rex = "\\b";

        Pattern pattern = Pattern.compile(rex);
        Matcher matcher = pattern.matcher(str);

        String[] result = pattern.split(str);

        for (String string: result) {
            System.out.println("分割的字符串：" + "[" + string + "]");
        }
    }

}

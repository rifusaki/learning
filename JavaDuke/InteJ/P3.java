public class P3 {
    public static Boolean twoOccurrences(String search, String source) {
        int Pos1 = source.indexOf(search);
        if (Pos1 != -1) {
            int Pos2 = source.indexOf(search, Pos1+1);
            return Pos2 != -1;
        }
        else return false;
    }

    public static String lastPart(String search, String source) {
        int Pos1 = source.indexOf(search);
        if (Pos1 != -1) return source.substring(Pos1);
        else return source;
    }

    public static void main(String[] args) {
        System.out.println(twoOccurrences("by", "A story by Abby Long"));
        System.out.println(twoOccurrences("a", "banana"));
        System.out.println(twoOccurrences("atg", "ctgtatgta") + "\n");

        System.out.println(lastPart("an","banana"));
        System.out.println(lastPart("zoo","forest"));
    }
}

public class P1 {
    public static String findSimpleGene(String ADN) {
        String adn = ADN.toLowerCase();
        int StI = adn.indexOf("atg");
        if (StI == -1) {
            return "";
        }
        int StE = adn.indexOf("taa", StI + 3);
        if ((StE - StI) % 3 == 0) {
            return adn.substring(StI, StE + 3);
        } else {
            return "";
        }
    }

    public static void main(String[] args) {
        String a = "cccatggggtttaaataataataggagagagagagagagttt";
        String b = "gggtttaaataataatag";
        String c = "atgcctag";
        String d = "ATGCCCTAA";
        String e = "AGGTAATGCCCASDAATAA";
        String vac = "";

        String[] genes = {a, b, c, d, e};

        for (String x : genes) {
            String res = findSimpleGene(x);
            if (res.equals(vac)) {
                System.out.println("Mal, mal");
            } else {
                System.out.println("Resultado: " + res);
            }
        }
    }
}
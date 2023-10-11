public class P2 {
    public static String findSimpleGene(String ADN, String Sta, String Sto) {
        String adn = ADN.toLowerCase();
        int StI = adn.indexOf(Sta);
        if (StI == -1) {
            return "";
        }
        int EnI = adn.indexOf(Sto, StI + 3);
        if ((EnI - StI) % 3 == 0) {
            return ADN.substring(StI, EnI + 3);
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
        String f = b.toUpperCase();
        String vac = "";
        String cod1 = "ggg";
        String cod2 = "aaa";

        String[] genes = {a, b, c, d, e, f};

        for (String x : genes) {
            String res = findSimpleGene(x, cod1, cod2);
            if (res.equals(vac)) {
                System.out.println("Mal, mal");
            } else {
                System.out.println("Resultado: " + res);
            }
        }
    }
}
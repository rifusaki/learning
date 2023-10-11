/**
 * Finds a protein within a strand of DNA represented as a string of c,g,t,a letters.
 * A protein is a part of the DNA strand marked by start and stop codons (DNA triples)
 * that is a multiple of 3 letters long.
 *
 * @author Duke Software Team 
 */
import edu.duke.*;
import java.io.*;

public class Part1 {
    public String findSimpleGene(String ADN) {
        String adn = ADN.toLowerCase();
        int StI = adn.indexOf("atg");
        if (StI == -1) {
            return "";
        }
        int StE = adn.indexOf("taa", StI + 3);
        if (StE - StI % 3 == 0) {
            return adn.substring(StI, StE + 3);
        } else {
            return "";
        }
    }

    public void testSimpleGene() {
        String a = "cccatggggtttaaataataataggagagagagagagagttt";
        String b = "gggtttaaataataatag";
        String c = "atgcctag";
        String d = "ATGCCCTAA";
        String e = "ATGCCCASDAATAA";
        String vac = "";

        String[] genes = {a, b, c, d, e};
        
        System.out.println(genes);
        
        for (String x : genes) {
            System.out.println(x);
            System.out.println(x.equals(vac));
            String res = findSimpleGene(x);
            if (x.equals(vac)) {
                System.out.println("Mal, mal");
            }
            else {
                System.out.println("Resultado: " + res);
            }
        }
    }

}

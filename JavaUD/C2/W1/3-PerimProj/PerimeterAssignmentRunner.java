import edu.duke.*;
import java.io.File;

public class PerimeterAssignmentRunner {
    public double getPerimeter (Shape s) {
        // Start with totalPerim = 0
        double totalPerim = 0.0;
        // Start wth prevPt = the last point 
        Point prevPt = s.getLastPoint();
        // For each point currPt in the shape,
        for (Point currPt : s.getPoints()) {
            // Find distance from prevPt point to currPt 
            double currDist = prevPt.distance(currPt);
            // Update totalPerim by currDist
            totalPerim = totalPerim + currDist;
            // Update prevPt to be currPt
            prevPt = currPt;
        }
        // totalPerim is the answer
        return totalPerim;
    }

    public int getNumPoints (Shape s) {
        // Put code here
        int count = 0;
        for (Point i : s.getPoints()) {
            count = count + 1;
        }    
        return count;
    }

    public double getAverageLength(Shape s) {
        // Put code here
        return getPerimeter(s) / getNumPoints(s);
    }

    public double getLargestSide(Shape s) {
        // Put code here
        Point prev = s.getLastPoint();
        double lsf = 0;
        for (Point e : s.getPoints()) {
            if (lsf < prev.distance(e)) {
                lsf = prev.distance(e);
            }
            prev = e;
        }
        return lsf;
    }

    public double getLargestX(Shape s) {
        // Put code here
        double xsf = 0;
        for (Point a : s.getPoints()) {
            if (xsf < a.getX()) {
                xsf = a.getX();
            }
        }
        double xto = xsf;
        return xto;
    }

    public double getLargestPerimeterMultipleFiles() {
        DirectoryResource arch = new DirectoryResource();
        double psf = 0.0;
        for (File fi : arch.selectedFiles()) {
            FileResource fis = new FileResource(fi);
            Shape s = new Shape(fis);
            if (psf < getPerimeter(s)) {
                psf = getPerimeter(s);
            }
        }
        return psf;
    }

    public File getFileWithLargestPerimeter() {
        DirectoryResource arch = new DirectoryResource();
        File fidef = null;
        double psf = 0.0;
        for (File fi : arch.selectedFiles()) {
            FileResource fis = new FileResource(fi);
            Shape s = new Shape(fis);
            if (psf < getPerimeter(s)) {
                fidef = fi;
                psf = getPerimeter(s);
            }
        }
        return fidef;
    }


    public void testPerimeter () {
        FileResource fr = new FileResource();
        Shape s = new Shape(fr);
        double length = getPerimeter(s);
        System.out.println("perímetro: " + length);
        System.out.println("número de puntos: " + getNumPoints(s));
        System.out.println("longitud promedio: " + getAverageLength(s));
        System.out.println("lado más largo: " + getLargestSide(s));
        System.out.println("x mayor: " + getLargestX(s));
    }
    
    public void testPerimeterMultipleFiles() {
        System.out.println("Mayor perímetro: " + getLargestPerimeterMultipleFiles());
        
    }

    public void testFileWithLargestPerimeter() {
        System.out.println("Archivo con mayor perímetro: " + getFileWithLargestPerimeter());
    }

    // This method creates a triangle that you can use to test your other methods
    public void triangle(){
        Shape triangle = new Shape();
        triangle.addPoint(new Point(0,0));
        triangle.addPoint(new Point(6,0));
        triangle.addPoint(new Point(3,6));
        for (Point p : triangle.getPoints()){
            System.out.println(p);
        }
        double peri = getPerimeter(triangle);
        System.out.println("perimeter = "+peri);
    }

    // This method prints names of all files in a chosen folder that you can use to test your other methods
    public void printFileNames() {
        DirectoryResource dr = new DirectoryResource();
        for (File f : dr.selectedFiles()) {
            System.out.println(f);
        }
    }

    public static void main (String[] args) {
        PerimeterAssignmentRunner pr = new PerimeterAssignmentRunner();
        //pr.testPerimeter();
        pr.testPerimeterMultipleFiles();
        pr.testFileWithLargestPerimeter();
    }
}

public class Led
{
    private double r;
    private double b;
    private double g;

    public Led(double r, double b, double g)
    {
        this.r = r;
        this.b = b;
        this.g = g;
    }
    
    public void setR(double r) {
        this.r = r;
    }
    
    public double getR() {
        return this.r;
    }
    
    public void setB(double b) {
        this.b = b;
    }
    
    public double getB() {
        return this.b;
    }
    
    public void setG(double g) {
        this.g = g;
    }
    
    public double getG() {
        return this.g;
    }
}

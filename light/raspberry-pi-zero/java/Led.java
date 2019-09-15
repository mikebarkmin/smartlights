import com.pi4j.wiringpi.Gpio;
import com.pi4j.wiringpi.SoftPwm;

public class Led
{
    private static int PIN_R = 3;
    private static int PIN_G = 5;
    private static int PIN_B = 7;
    
    private double r;
    private double b;
    private double g;

    public Led(double r, double b, double g)
    {
        Gpio.wiringPiSetup();
        SoftPwm.softPwmCreate(PIN_R, 0, 255);
        SoftPwm.softPwmCreate(PIN_G, 0, 255);
        SoftPwm.softPwmCreate(PIN_B, 0, 255);
        this.r = r;
        this.b = b;
        this.g = g;
    }
    
    public void setR(double r) {
        SoftPwm.softPwmWrite(PIN_R, r);
        this.r = r;
    }
    
    public double getR() {
        return this.r;
    }
    
    public void setB(double b) {
        SoftPwm.softPwmWrite(PIN_B, b);
        this.b = b;
    }
    
    public double getB() {
        return this.b;
    }
    
    public void setG(double g) {
        SoftPwm.softPwmWrite(PIN_G, g);
        this.g = g;
    }
    
    public double getG() {
        return this.g;
    }
}

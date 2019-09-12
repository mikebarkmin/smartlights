import java.util.*;
import sas.*;
import sasio.*;

public class App
{
    private static View view;
    private static Screen activeScreen;
    private static boolean running;
    public static final int HEIGHT = 800;
    public static final int WIDTH = 400;

    public App()
    {
        view = new View(WIDTH, HEIGHT, "Smartlights");      
        activeScreen = new LightsScreen();
        activeScreen.start();
        run();
    }

    public static void stop() {
        running = false;
    }
    
    public static View getView() {
        return view;
    }

    public static void changeScreen(Screen screen) {
        if (screen != null) {
            activeScreen.stop();
            activeScreen = screen;
            activeScreen.start();
        }
    }

    public void run() {
        running = true;
        while(running) {
            activeScreen.update();
            view.wait(10);
        }
    }
}

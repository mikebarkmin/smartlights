import org.json.JSONObject;
import sasio.*;

public class LightScreen implements Screen
{ 
    private JSONObject light;
    
    public LightScreen(JSONObject pLight) {
        light = pLight;
    }
    
    public void update() {}
  
    public void start() {
        new Textfield(0, 80, App.WIDTH, 20, light.getString("name"), App.getView());
    }
    
    public void stop() {}
}
import sas.*;
import sasio.*;
import java.awt.Color;
import java.util.*;
import org.json.*;
import com.github.kevinsawick.HttpRequest;

public class LightsScreen implements Screen
{   
    private List<JSONObject> lights;
    private Label lblLights;
    private List<Button> btnLights;
    
    public void update() {
        for (int i = 0; i < btnLights.size(); i++) {
            Button btnLight = btnLights.get(i);
            if (btnLight.clicked()) {
                System.out.println("clicked");
                JSONObject light = lights.get(i);
                App.changeScreen(new LightScreen(light));
            }
        }
    }
        
    public void start() {
        lights = new ArrayList<>();
        btnLights = new ArrayList<>();
        
        String body = HttpRequest.get("http://127.0.0.1:1880/lights").body();
        JSONArray a = new JSONArray(body);
        for (int i = 0; i < a.length(); i++) {
            JSONObject light = a.getJSONObject(i);
            lights.add(light);
            
            Button btnLight = new Button(20, i * 30 + 20, App.WIDTH - 40, 20, light.getString("name"), Color.YELLOW);
            btnLights.add(btnLight);
        }
    }
    
    public void stop() {
        for (Button btnLight : btnLights) {
            btnLight.setHidden(true);
        }
    }
}
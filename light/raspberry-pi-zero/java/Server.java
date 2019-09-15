import static spark.Spark.*;
import spark.ModelAndView;
import spark.Request;
import java.util.Map;
import java.util.HashMap;
import com.google.gson.Gson;
import java.net.InetAddress;

class Server {

    private Led led;

    public Server() {
        port(8080);
        staticFiles.location("/public");

        led = new Led(0, 0, 0);

        Gson gson = new Gson();
        get("/", (req, res) -> renderLed());
        get("/leds", (req, res) -> getLeds(), gson::toJson);
        post("/leds", (req, res) -> postLeds(req), gson::toJson);
    }

    public void close() {
        stop();
    }

    public Led getLeds() {
        return this.led;
    }

    public Led postLeds(Request req) {

        Gson gson = new Gson();

        Map<String, Double> params = gson.fromJson(req.body(), Map.class);

        double newR = params.getOrDefault("r", this.led.getR());
        double newG = params.getOrDefault("g", this.led.getG());
        double newB = params.getOrDefault("b", this.led.getB());

        this.led.setR(newR);
        this.led.setG(newG);
        this.led.setB(newB);

        return this.led;
    }
}


import java.util.List;
import java.util.ArrayList;
import java.net.InetAddress;

public class NetworkDevice {
    
    private String ipAddress;
    private String macAddress;
    
    public boolean isOnline() {
        try {
            InetAddress address = InetAddress.getByName(ipAddress);
            return address.isReachable(2000);
        } catch(Exception e) {
            return false;
        }
    }
    
    public static List<NetworkDevice> all() {
        return null;
    }
    
    public static String ipFromMac(String mac) {
        return null;
    }
}
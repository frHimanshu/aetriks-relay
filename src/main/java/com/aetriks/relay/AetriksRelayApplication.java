package com.aetriks.relay;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class AetriksRelayApplication {

    public static void main(String[] args) {
        SpringApplication app = new SpringApplication(AetriksRelayApplication.class);

        // Ensure app binds to your host's actual IP instead of localhost
        System.setProperty("server.address", getHostIp());

        app.run(args);
    }

    // Helper method to get host machine's IP address
    private static String getHostIp() {
        try {
            return java.net.InetAddress.getLocalHost().getHostAddress();
        } catch (Exception e) {
            System.err.println("Unable to determine host IP. Falling back to localhost.");
            return "127.0.0.1";
        }
    }
}

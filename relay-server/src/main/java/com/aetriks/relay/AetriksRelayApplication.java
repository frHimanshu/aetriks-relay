package com.aetriks.relay;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.net.InetAddress;

@SpringBootApplication
public class AetriksRelayApplication {

    public static void main(String[] args) {
        // Set server to bind to the host machine's actual IP address
        String hostIp = getHostIp();
        System.setProperty("server.address", hostIp);

        SpringApplication app = new SpringApplication(AetriksRelayApplication.class);
        app.run(args);

        System.out.println("Server is running on host IP: " + hostIp);
    }

    // Get the local machine's IP address
    private static String getHostIp() {
        try {
            return InetAddress.getLocalHost().getHostAddress();
        } catch (Exception e) {
            System.err.println("[Error] Unable to resolve host IP. Defaulting to localhost.");
            return "127.0.0.1";
        }
    }
}

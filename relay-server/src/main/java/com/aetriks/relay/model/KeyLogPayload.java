package com.aetriks.relay.model;

public class KeyLogPayload {

    private String keyboardData;

    // Default constructor (required for Spring to bind JSON)
    public KeyLogPayload() {
    }

    // Parameterized constructor
    public KeyLogPayload(String keyboardData) {
        this.keyboardData = keyboardData;
    }

    // Getter
    public String getKeyboardData() {
        return keyboardData;
    }

    // Setter
    public void setKeyboardData(String keyboardData) {
        this.keyboardData = keyboardData;
    }

    @Override
    public String toString() {
        return "KeyLogPayload{" +
                "keyboardData='" + keyboardData + '\'' +
                '}';
    }
}
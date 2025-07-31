package com.aetriks.relay.model;

public class KeylogPayload {

    private String keyboardData;

    // Default constructor
    public KeylogPayload() {}

    // Constructor with parameter
    public KeylogPayload(String keyboardData) {
        this.keyboardData = keyboardData;
    }

    public String getKeyboardData() {
        return keyboardData;
    }

    public void setKeyboardData(String keyboardData) {
        this.keyboardData = keyboardData;
    }

    @Override
    public String toString() {
        return "KeylogPayload{" +
                "keyboardData='" + keyboardData + '\'' +
                '}';
    }
}

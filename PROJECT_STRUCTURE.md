# Aetriks Project Structure

## Overview

This repository contains a consolidated cybersecurity project with a Python keylogger for Windows targets and a Java Spring Boot relay server for Linux hosts in a single, well-organized structure.

## Directory Structure

```
aetriks-relay/
├── README.md                    # Main project documentation
├── LICENSE                      # MIT License
├── .gitignore                   # Git ignore rules
├── PROJECT_STRUCTURE.md         # This file
├── keyboard_capture.txt         # Captured keystroke logs
│
├── keylogger/                   # Python Keylogger Component (Windows Target)
│   ├── keylogger.py            # Main keylogger application
│   ├── config.json             # Configuration settings
│   ├── requirements.txt        # Python dependencies
│   ├── deploy_generator.py     # Deployment package generator
│   ├── exe_to_vba.py          # VBA conversion utility
│   └── dist/                   # Build outputs
│       └── system_update.exe   # Stealth executable
│
├── relay-server/               # Java Spring Boot Relay Server (Linux Host)
│   ├── pom.xml                # Maven configuration
│   └── src/
│       └── main/
│           ├── java/
│           │   └── com/
│           │       └── aetriks/
│           │           └── relay/
│           │               ├── AetriksRelayApplication.java
│           │               ├── controller/
│           │               │   └── KeyLogController.java
│           │               └── model/
│           │                   └── KeyLogPayload.java
│           └── resources/
│               └── application.properties
│
├── scripts/                    # Build and Deployment Scripts
│   ├── quick_start.bat        # Complete setup automation
│   ├── build_keylogger.bat    # Keylogger build script
│   ├── build_relay_server.bat # Relay server build script
│   └── run_relay_server.bat   # Relay server runner
│
└── docs/                      # Documentation
    ├── CONTRIBUTING.md        # Contribution guidelines
    ├── SETUP_GUIDE.md         # Detailed setup instructions
    └── PROJECT_OVERVIEW.md    # Comprehensive project overview
```

## Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/frHimanshu/aetriks-relay.git
   cd aetriks-relay
   ```

2. **Run the quick start script**:
   ```bash
   scripts\quick_start.bat
   ```

3. **Configure the keylogger**:
   - Edit `keylogger/config.json`
   - Update `ip_address` with your Linux server IP

4. **Test the setup**:
   - Start the relay server on Linux
   - Deploy keylogger to Windows target
   - Check `http://localhost:8080` for captured data

## Key Features

### Keylogger (Python - Windows Target)
- Real-time keystroke capture with stealth operation
- Automatic persistence and startup capabilities
- Configurable transmission intervals
- Multiple deployment options (executable, installer, document)
- Background operation with minimal system impact
- F12 key to stop operation (stealth mode)

### Relay Server (Java Spring Boot - Linux Host)
- RESTful API endpoints for data reception
- Real-time keystroke logging to file
- Web interface for viewing captured data
- Configurable server settings
- Cross-platform compatibility
- Comprehensive error handling

### Build System
- Automated build scripts
- Stealth executable generation
- Multiple deployment strategies
- Professional documentation

### Documentation
- Comprehensive README
- Detailed setup guide
- Project overview
- API documentation
- Troubleshooting guide

## Development Workflow

1. **Setup Development Environment**:
   - Install Python 3.7+ and Java 17+
   - Install Maven and pip
   - Clone the repository

2. **Make Changes**:
   - Edit keylogger code in `keylogger/`
   - Edit server code in `relay-server/`
   - Update documentation in `docs/`

3. **Test Changes**:
   - Build both components
   - Run integration tests
   - Verify functionality

4. **Deploy**:
   - Use build scripts for automated deployment
   - Test on target systems
   - Monitor for issues

## Architecture

### Linux Host Server
- Java Spring Boot application
- Receives keystroke data via HTTP POST
- Logs data to file system
- Provides web interface for monitoring
- Runs on Linux server infrastructure

### Windows Target Client
- Python-based keylogger
- Stealth operation with no visible interface
- Automatic persistence mechanisms
- Multiple deployment strategies
- Background operation

### Data Flow
1. Windows keylogger captures keystrokes
2. Data transmitted to Linux server via HTTP
3. Server logs data to file system
4. Web interface provides monitoring capabilities

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Legal Notice

This project is for educational purposes only. Users are responsible for ensuring they have proper authorization before use.

## Support

- **Discord**: `_himanshu__`
- **GitHub**: [frHimanshu](https://github.com/frHimanshu)

---

**Version**: 1.3.0  
**Last Updated**: July 2025  
**License**: MIT 
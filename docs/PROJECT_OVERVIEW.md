# Aetriks Project Overview

## Project Description

Aetriks is a comprehensive cybersecurity research project that demonstrates keylogger functionality through a client-server architecture. The project consists of two main components:

1. **Python Keylogger (Client)** - Captures keystrokes on Windows systems
2. **Java Spring Boot Relay Server** - Receives and logs captured data

## Architecture Overview

```
┌─────────────────┐    HTTP POST    ┌──────────────────┐
│   Windows PC    │ ──────────────► │   Linux Server   │
│                 │                 │                  │
│ Python Keylogger│                 │ Spring Boot API  │
│ (Client)        │                 │ (Server)         │
└─────────────────┘                 └──────────────────┘
                                              │
                                              ▼
                                    ┌──────────────────┐
                                    │   Log Files      │
                                    │ keyboard_capture │
                                    │ .txt             │
                                    └──────────────────┘
```

## Component Details

### 1. Python Keylogger (Client)

**Location**: `keylogger/`

**Key Features**:
- Real-time keystroke capture using `pynput`
- Configurable data transmission intervals
- Automatic reconnection on network failures
- Stealth operation with minimal system impact
- VBA conversion capability for document-based deployment

**Files**:
- `keylogger.py` - Main keylogger application
- `config.json` - Configuration settings
- `requirements.txt` - Python dependencies
- `exe_to_vba.py` - VBA conversion utility

**Configuration Options**:
```json
{
    "ip_address": "127.0.0.1",    // Server IP address
    "port_number": 8080,          // Server port
    "time_interval": 10           // Transmission interval (seconds)
}
```

### 2. Java Spring Boot Relay Server

**Location**: `relay-server/`

**Key Features**:
- RESTful API endpoints for data reception
- Real-time keystroke logging to file
- Web interface for viewing captured data
- Configurable server settings
- Cross-platform compatibility

**API Endpoints**:
- `GET /` - View captured keystrokes in browser
- `POST /api/keystrokes` - Receive keystroke data
- `POST /` - Alternative endpoint for data reception

**Response Format**:
```json
{
    "message": "Successfully logged the data.",
    "stop": false
}
```

## Data Flow

1. **Keylogger Initialization**:
   - Load configuration from `config.json`
   - Initialize keyboard listener
   - Start data transmission thread

2. **Keystroke Capture**:
   - Monitor keyboard events using `pynput`
   - Buffer keystrokes in memory
   - Handle special keys (space, enter, backspace, etc.)

3. **Data Transmission**:
   - Send buffered data to server at configured intervals
   - Use HTTP POST with JSON payload
   - Handle connection errors and timeouts

4. **Server Processing**:
   - Receive HTTP POST requests
   - Parse JSON payload
   - Append data to log file
   - Return success/error response

5. **Data Storage**:
   - Log file: `keyboard_capture.txt`
   - Format: One keystroke entry per line
   - Persistent storage on server

## Security Features

### Client-Side Security
- Minimal system footprint
- Configurable transmission intervals
- Error handling and recovery
- Graceful shutdown on ESC key

### Server-Side Security
- Input validation
- Error handling
- Logging and monitoring
- Configurable server settings

### Network Security
- HTTP communication (upgrade to HTTPS for production)
- JSON payload validation
- Timeout handling
- Connection error recovery

## Deployment Options

### 1. Executable Deployment
- Build standalone executable with PyInstaller
- Distribute `.exe` file
- Requires network access to server

### 2. VBA Document Deployment
- Convert executable to VBA code
- Embed in Word document (`.docm`)
- Auto-execution on document open
- Stealth deployment option

### 3. Source Code Deployment
- Direct Python execution
- Requires Python environment
- Most flexible but visible

## Development Guidelines

### Code Structure
- Modular design with clear separation of concerns
- Comprehensive error handling
- Detailed logging for debugging
- Configuration-driven behavior

### Testing
- Unit tests for individual components
- Integration tests for client-server communication
- Manual testing with real keystrokes
- Network failure simulation

### Documentation
- Inline code comments
- API documentation
- Setup and deployment guides
- Troubleshooting documentation

## Legal and Ethical Considerations

### Educational Purpose
- Designed for cybersecurity education
- Demonstrates keylogger concepts
- Shows client-server architecture
- Illustrates data exfiltration techniques

### Responsible Use
- Use only on systems you own
- Obtain explicit permission before testing
- Follow local laws and regulations
- Document usage and authorization

### Security Implications
- Demonstrates potential security vulnerabilities
- Shows importance of endpoint protection
- Illustrates network monitoring needs
- Highlights data protection requirements

## Future Enhancements

### Planned Features
1. **Encryption**: End-to-end data encryption
2. **Authentication**: Server-side authentication
3. **Compression**: Data compression for efficiency
4. **Persistence**: Automatic startup and persistence
5. **GUI**: Graphical user interface for server
6. **Database**: Database storage instead of file logging
7. **Real-time Monitoring**: Live keystroke viewing
8. **Multi-platform**: Support for macOS and Linux

### Technical Improvements
1. **Performance**: Optimize data transmission
2. **Reliability**: Enhanced error recovery
3. **Scalability**: Support for multiple clients
4. **Monitoring**: Advanced logging and analytics
5. **Security**: Enhanced security features

## Contributing

### Development Setup
1. Clone the repository
2. Set up development environment
3. Install dependencies
4. Run tests
5. Make changes
6. Submit pull request

### Code Standards
- Follow existing code style
- Add comprehensive comments
- Include error handling
- Write unit tests
- Update documentation

### Review Process
- Code review for all changes
- Testing on multiple platforms
- Documentation updates
- Security review for new features

## Support and Maintenance

### Issue Reporting
- Use GitHub issues for bug reports
- Provide detailed reproduction steps
- Include system information
- Attach relevant logs

### Documentation Updates
- Keep documentation current
- Update setup instructions
- Maintain troubleshooting guides
- Add new feature documentation

### Version Management
- Semantic versioning
- Changelog maintenance
- Release notes
- Backward compatibility

This project serves as a comprehensive example of cybersecurity research tools while maintaining educational value and promoting responsible use. 
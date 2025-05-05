import subprocess

# We load the newline-separated commands from the commands file.
with open("commands.txt", "r") as fh:
    cmds = fh.readlines()
    for item in cmds:
        try:
            # Strip newline characters and skip comments or empty lines.
            command = item.strip()
            if not command or command.startswith("#"):  # Skip empty lines and comments
                continue
            print(f"Running: {command}")
            subprocess.run(command.split(" "), check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {command}\nError: {e}")

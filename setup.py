import subprocess

def run_commands_from_file(filename="commands.txt"):
    try:
        with open(filename, "r") as fh:
            commands = fh.readlines()
            for cmd in commands:
                cmd = cmd.strip()
                if cmd:
                    print(f"Running: {cmd}")
                    subprocess.run(cmd.split(), check=True)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")

if __name__ == "__main__":
    run_commands_from_file()

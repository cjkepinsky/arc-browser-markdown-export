import os
import sys
import subprocess

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_markdown_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)

    try:
        if os.name == 'posix':  # macOS, Linux
            subprocess.run(['open', file_path])
        elif os.name == 'nt':  # Windows
            os.startfile(file_path)
        else:
            print(f"Unsupported operating system: {os.name}")
            sys.exit(1)
    except Exception as e:
        print(f"Error opening file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


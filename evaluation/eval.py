import subprocess

def main():
    # Define the command to be executed
    command = "python.exe ..\commandToJson.py"  # Replace "your_command_here" with your actual terminal command

    # Open the text file containing the list of inputs
    with open("samples.txt", "r", encoding="utf-8") as file:
        # Iterate over each line in the file
        for line in file:
            print("Input: "+line)

            # Remove any trailing whitespace characters such as newline
            line = line.strip()
            
            # Construct the full command with the current line as an argument
            full_command = f"{command} \"ok glasses {line}\""
            
            # Execute the command in the terminal
            subprocess.run(full_command, shell=True)

if __name__ == "__main__":
    main()
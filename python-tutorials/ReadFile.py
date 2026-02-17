if __name__ == "__main__":
    try:
        file = open("example.txt", "r");
        content = file.read();
        print("File Name: ", file.name, "\n");
        print("File content:\n", content);
        file.close();
        print("File closed successfully.");
    except IOError:
        print("Error opening the file.");
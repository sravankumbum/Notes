if __name__ == "__main__":
    try:
        file = open("example.txt", "w");
        file.write("Hello, this is a sample text file.\n");
        file.write("This file is created using Python.\n");
        print("File written successfully.");
        file.close();
        print("File closed successfully.");
    except IOError:
        print("Error opening the file.");

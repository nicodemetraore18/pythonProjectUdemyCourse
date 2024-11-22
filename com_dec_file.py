import subprocess

def compress_file(file_path):
    try:
        subprocess.run(["tar","-czvf","compressed,tar.gz",file_path], check=True)
        print(f"compression succesfull . compressed file: compressed.tar.gz")

    except  subprocess.CalledProcessError as e:
        print(f"compression failed .An error occured :{e.stderr}")

def decompress_file(archive_path):
    try:
        subprocess.run(["tar","-xzvf", archive_path],check=True)
        print(f"Decompression successful .Files extracted from {archive_path}")

    except subprocess.CalledProcessError as e:
        print (f"Decompression failed .an error occured: {e.stderr}")

def main():
    print("options:")
    print("1. Compress a file ")
    print("2. Decompress an archive")

    choice=input("Enter your choice (1/2)")

    if choice=="1":
        file_to_compress = input("Enter the path of file to compress: ")
        compress_file(file_to_compress)
    elif choice=="2":
        archive_to_decompress =input("enter the path of the archive to decompress: ")
        decompress_file(archive_to_decompress)
    else:
        print("Invalid choice .please enter 1 or 2.")

if __name__=="__main__":
    main()
    

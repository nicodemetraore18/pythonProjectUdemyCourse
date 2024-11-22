import os
import subprocess


def search_keyword(keyword,folder_path):
    try:
        files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        if not files:
            print("No text files found in the specified folder .")
            return
        for file in files:
            file_path=os.path.join(folder_path,file)
            result =subprocess.run(["findstr", '/i', keyword, file_path], capture_output=True, text=True )
            occurrences =result.stdout.strip().split('\n')
            print (f"Occurrence of '{keyword}' in {file} :")
            for occurrence in occurrences :
                print(f"-{occurrence}")
    except FileNotFoundError:
        print("folder not found , please provide a valide folder path")


def main():
    keyword=input("Enter the keyword to search:")
    folder_path=input("enter the folder path to search in : ")

    search_keyword(keyword,folder_path)


if __name__ =="__main__":
    main()


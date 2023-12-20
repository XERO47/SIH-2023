import os
from collections import defaultdict
from pygments.lexers import guess_lexer_for_filename
from pygments.util import ClassNotFound


def detect_languages(files_array):
    file_counts = defaultdict(int)
    total_files = 0
    percentages={}
    # Collect file extensions and count files
    for file in files_array:
        
            _, extension = os.path.splitext(file)
            total_files += 1

            try:
                # Guess the lexer for the file
                lexer = guess_lexer_for_filename("file" + extension, "")
                language_name = lexer.name
                file_counts[language_name] += 1
            except ClassNotFound:
                # If the lexer is not found, count it as "Unknown"
                file_counts["Unknown"] += 1

    # Calculate and print the percentage for each language
    if total_files > 0:
        print(f"Total files: {total_files}")
        for language, count in file_counts.items():
            percentage = (count / total_files) * 100
            if(language=="Unknown"):
                pass
            else:
                print(f"{language}: {count} files ({percentage:.2f}%)")
                percentages[language] = round(percentage, 2)
    else:
        print("No files found in the specified directory.")
    return percentages

def detect_framework(os_file_list):
    framework="Not detected"
    manifest_file=""
    if("pom.xml" in os_file_list):
        framework="Maven"
        manifest_file="pom.xml"
    elif("package.json" in os_file_list):
        framework="Node"
        manifest_file="package.json"
    elif("package-lock.json" in os_file_list):
        framework="Node"
        manifest_file="package-lock.json"
    elif("requirements.txt" in os_file_list ):
        framework="Python"
        manifest_file="requirements.txt"
    elif("Pipfile.lock" in os_file_list):
        framework="Python"
        manifest_file="Pipfile.lock"
    elif("Pipfile" in os_file_list):
        framework="Python"
        manifest_file="Pipfile"
    return framework,manifest_file
def get_file_names(directory_path):
    file_names = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_names.append(file)
    return file_names




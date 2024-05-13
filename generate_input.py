import random
import os

def generate_requests(filename, num_requests=1000, max_cylinder=4999):
    # Ensure the directory exists and create it if it does not
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(filename, 'w') as file:
        for _ in range(num_requests):
            file.write(f"{random.randint(0, max_cylinder)}\n")

if __name__ == "__main__":
    # Change 'your_directory_path' to the path where you want to save the file
    file_path = "/Users/andrewsebastian/Desktop/untitled folder 3/disk_requests.txt"
    generate_requests(file_path)

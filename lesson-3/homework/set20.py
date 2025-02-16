import os

# Define the directory path
directory = "c:/Users/ids/Desktop/PythonHomework/lesson-3/homework"

# Ensure the directory exists
os.makedirs(directory, exist_ok=True)

# Create 25 empty Python files
for i in range(1, 26):
    file_path = os.path.join(directory, f"dictionary{i}.py")
    with open(file_path, 'w') as file:
        pass  # Create an empty file

print("25 empty Python files created successfully.")
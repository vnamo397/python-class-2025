filename = input("Enter the filename to read: ")
try:
	with open(filename, 'r') as f:
		content = f.read()
		print("File contents:")
		print(content)
except FileNotFoundError:
	print(f"Error: The file '{filename}' does not exist.")

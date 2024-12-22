import hashlib
import random
import string

# Function to generate a complex password
def generate_complex_password(nickname):
    # Salt to increase password security
    salt = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=8))
    password = nickname + salt  # Combine nickname and salt to form the password
    return password

# Function to generate the SHA-256 hash of the password
def generate_sha256_hash(password):
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()

# Function to write the hash to a file with a .sha256 extension
def write_hash_to_file(hash_value):
    # Create a .sha256 file in the same folder where the script is located
    with open('password_hash.sha256', 'w', encoding='utf-8') as file:
        file.write(f"SHA-256 Hash: {hash_value}\n")

# Main program
def main():
    nickname = input("Enter your nickname or name: ")
    
    # Generate password
    password = generate_complex_password(nickname)
    print(f"Generated password: {password}")

    # Ask if the user wants to convert the password to a SHA-256 hash
    hash_choice = input("Do you want to convert the password to a SHA-256 hash? (yes/no): ").strip().lower()
    
    if hash_choice == 'yes':
        # Generate the hash
        hash_value = generate_sha256_hash(password)
        print(f"SHA-256 password hash: {hash_value}")
        
        # Write the hash to a .sha256 file
        write_hash_to_file(hash_value)
        print("The password hash has been saved to the file 'password_hash.sha256'")
    else:
        print("The password was not converted to a hash.")

if __name__ == "__main__":
    main()

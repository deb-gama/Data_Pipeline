import os
from cryptography.fernet import Fernet

# Path to the .env file
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# Ensure the .env file exists
if not os.path.exists(env_path):
    open(env_path, 'w').close()

# Read .env file to check if FERNET_KEY is already set
with open(env_path, 'r') as env_file:
    lines = env_file.readlines()

fernet_key_exists = any(line.startswith("AIRFLOW__CORE__FERNET_KEY=") for line in lines)

if not fernet_key_exists:
    # Generate a new Fernet key
    fernet_key = Fernet.generate_key()
    fernet_key_str = fernet_key.decode()

    # Append the key to the .env file
    with open(env_path, 'a') as env_file:
        env_file.write(f"\nAIRFLOW__CORE__FERNET_KEY={fernet_key_str}\n")
    
    print(f"Generated and added Fernet Key {fernet_key_str} to .env file.")
else:
    print("Fernet key already exists in .env file.")

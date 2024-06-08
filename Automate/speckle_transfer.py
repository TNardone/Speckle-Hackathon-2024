import os
import subprocess
from dotenv import load_dotenv
from specklepy.api.client import SpeckleClient


# Get Speckle token
try:
    repo_root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], stderr=subprocess.DEVNULL, text=True).strip()
    env_path = os.path.join(repo_root, '.env')
    load_dotenv(env_path)
except subprocess.CalledProcessError:
    print('Could not load .env.')

TOKEN = os.getenv('SPECKLE_TOKEN')
URL = os.getenv('SPECKLE_URL')
STREAM_ID = os.getenv('SPECKLE_STREAM_ID')

client = SpeckleClient(host=URL)

try:
    client.authenticate_with_token(token=TOKEN)
    print("Authenticated successfully.")
except Exception as e:
    print(f"Authentication failed: {e}")

"""
try:
    # Fetch stream details
    stream = client.stream.get(id=STREAM_ID)
    print(f"Stream ID: {stream.id}")
    print(f"Stream Name: {stream.name}")
    print(f"User Role: {stream.role}")
    print(f"Collaborators: {stream.collaborators}")

    # Verify if the user has write access
    if stream.role in ["owner", "contributor"]:
        print("You have write access to this stream.")
    else:
        print("You do not have write access to this stream.")
except Exception as e:
    print(f"Failed to retrieve stream details: {e}")
    """
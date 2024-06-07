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

print(TOKEN)
print(URL)
'''
client = SpeckleClient(host=URL)

client.authenticate(token=TOKEN)

stream_info = client.stream.list()

for stream in stream_info:
    print(stream)
'''
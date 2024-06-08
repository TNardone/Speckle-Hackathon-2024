import os
import subprocess
from dotenv import load_dotenv
from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_account_from_token
from specklepy.objects.base import Base
from specklepy.api import operations
from specklepy.api.wrapper import StreamWrapper


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
PROJECT_ID = os.getenv('SPECKLE_PROJECT_ID')

# Initialize StreamWrapper
stream_wrapper = StreamWrapper(URL)


client = SpeckleClient()


try:
    account = get_account_from_token(TOKEN, stream_wrapper.server_url)
    client.authenticate_with_account(account)
    print("Authenticated successfully.")
except Exception as e:
    print(f"Authentication failed: {e}")


try:
    commits = client.commit.list(STREAM_ID)
    """
    commit_metadata = []
    for commit in commits:
        commit_dict = {
            'commit_id': commit.id,
            'author': commit.authorName,
            'object_id': commit.referencedObject,
            'branch_name': commit.branchName,
            'date': commit.createdAt,
            'commit_message': commit.message
        }
        commit_metadata.append(commit_dict)
    print(commit_metadata)
    """
    print("Successfully proccessed commits.")
except Exception as e:
    print(f"Could not process commits: {e}")

try:
    streams = client.stream.list()  # Assuming this method lists streams; confirm name from docs
    project_streams = [stream for stream in streams if stream.project_id == PROJECT_ID]
    if not project_streams:
        print("No streams found for the specified project.")
    else:
        for stream in project_streams:
            print(f"Stream ID: {stream.id}, Stream Name: {stream.name}")
except Exception as e:
    print(f"Could not retrieve streams: {e}")

"""
try:
    # List streams associated with the account
    streams = stream_wrapper.list_streams()

    # Filter streams by project ID
    project_streams = [stream for stream in streams if stream.project_id == PROJECT_ID]

    if not project_streams:
        print("No streams found for the specified project.")
        exit()

    # Print all relevant streams
    for stream in project_streams:
        print(f"Stream ID: {stream.stream_id}, Stream Name: {stream.name}")

    # Select the desired stream
    stream_id = project_streams[0].stream_id  # or manually set the specific stream ID

    # Retrieve data from the stream
    data = stream_wrapper.get_stream_data(stream_id)
    print("Stream data retrieved successfully.")
    print(data)

except Exception as e:
    print(f"Failed to retrieve streams or stream data: {e}")
    """
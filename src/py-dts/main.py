import json
from pathlib import Path
BASE_DIR = BASE_DIR = Path(__file__).resolve().parent
def sendLocal(message, password=None, compress=False, distributedResources=True, verbose=False, secondaryKey=None):
    def verb(msg):
        if verbose:
            print(msg)
    verb("PyDTS ()")
    verb("Sending message locally...")
    verb(f"Message: {message}")
    verb(f"Compress: {compress}")
    verb(f"Distributed Resources: {distributedResources}")
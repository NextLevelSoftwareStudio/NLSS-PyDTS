import json, sys
from pathlib import Path
BASE_DIR = BASE_DIR = Path(__file__).resolve().parent
specs_json = Path(BASE_DIR / "dependencies" / "specs.json")
registry_folder = Path.home() / "System" / "Registry" / "PyDTS"
with open(specs_json, "r") as f:
    specs = json.load(f)
PYDTS_VERSION = specs["Version"]
def sendLocal(message, password=None, compress=False, distributedResources=True, verbose=False, secondaryKey=None):
    def verb(msg):
        if verbose:
            print(msg)
    verb(f"PyDTS ({PYDTS_VERSION})")
    verb("Sending message locally...")
    verb(f"Message: {message}")
    verb(f"Compress: {compress}")
    verb(f"Distributed Resources: {distributedResources}")
def sendNetwork(message, password=None, compress=False, distributedResources=True, verbose=False, clientPassword=None):
    def verb(msg):
        if verbose:
            print(msg)
    verb(f"PyDTS ({PYDTS_VERSION})")
    verb("Sending message over network...")
    verb(f"Message: {message}")
    verb(f"Compress: {compress}")
    verb(f"Distributed Resources: {distributedResources}")
def install(verbose=False):
    def verb(msg):
        if verbose:
            print(msg)
    verb(f"Installing PyDTS ({PYDTS_VERSION})...")
def shutdown(verbose=False):
    if verbose:
        print(f"Shutting down PyDTS ({PYDTS_VERSION})...")
    sys.exit(0)
import json
from pathlib import Path
from .dependencies import lib_A
BASE_DIR = BASE_DIR = Path(__file__).resolve().parent
specs_json = Path(BASE_DIR / "dependencies" / "specs.json")
registry_folder = Path.home() / "Next Level Software Studio" / "Registry" / "PyDTS"
with open(specs_json, "r") as f:
    specs = json.load(f)
PYDTS_VERSION = specs["Version"]
def sendLocal(message, password=None, compress=False, distributedResources=True, verbose=False, secondaryKey=None):
    lib_A.verb(f"PyDTS ({PYDTS_VERSION})", verbose)
    lib_A.verb("Sending message locally...", verbose)
    lib_A.verb(f"Message: {message}", verbose)
    lib_A.verb(f"Compress: {compress}", verbose)
    lib_A.verb(f"Distributed Resources: {distributedResources}", verbose)
def sendNetwork(message, password=None, compress=False, distributedResources=True, verbose=False, clientPassword=None):
    lib_A.verb(f"PyDTS ({PYDTS_VERSION})", verbose)
    lib_A.verb("Sending message over network...", verbose)
    lib_A.verb(f"Message: {message}", verbose)
    lib_A.verb(f"Compress: {compress}", verbose)
    lib_A.verb(f"Distributed Resources: {distributedResources}", verbose)
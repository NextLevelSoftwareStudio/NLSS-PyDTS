import json
from pathlib import Path
from pytools import textIO
BASE_DIR = BASE_DIR = Path(__file__).resolve().parent
specs_json = Path(BASE_DIR / "dependencies" / "specs.json")
registry_folder = Path.home() / "Next Level Software Studio" / "Registry" / "PyDTS"
with open(specs_json, "r") as f:
    specs = json.load(f)
PYDTS_VERSION = specs["Version"]
def sendLocal(message, password=None, compress=False, distributedResources=True, verbose=False, key=None):
    textIO.print2(f"PyDTS ({PYDTS_VERSION})", verbose)
    textIO.print2("Sending message locally...", verbose)
    textIO.print2(f"Message: {message}", verbose)
    textIO.print2(f"Compress: {compress}", verbose)
    textIO.print2(f"Distributed Resources: {distributedResources}", verbose)

def sendNetwork(message, password=None, compress=False, distributedResources=True, verbose=False, clientPassword=None, key=None):
    textIO.print2(f"PyDTS ({PYDTS_VERSION})", verbose)
    textIO.print2("Sending message over network...", verbose)
    textIO.print2(f"Message: {message}", verbose)
    textIO.print2(f"Compress: {compress}", verbose)
    textIO.print2(f"Distributed Resources: {distributedResources}", verbose)
    textIO.print2(f"Key: {key}", verbose)
from pytools import textIO
from pathlib import Path
import json
BASE_DIR = BASE_DIR = Path(__file__).resolve().parent
specs_json = Path(BASE_DIR / "dependencies" / "specs.json")
with open(specs_json, "r") as f:
    specs = json.load(f)
PYDTS_VERSION = specs["Version"]

def receivingLocal(password, key, memoryblockname, verbose=False):
    textIO.print2(f"PyDTS ({PYDTS_VERSION})", verbose)
    textIO.print2("Receiving message locally...", verbose)
    textIO.print2(f"Memory block name: {memoryblockname}", verbose)
    textIO.print2(f"Password: {password}", verbose)
    textIO.print2(f"Key: {key}", verbose)

def receivingNetwork(password, clientPassword, key, verbose=False):
    textIO.print2(f"PyDTS ({PYDTS_VERSION})", verbose)
    textIO.print2("Receiving message over network...", verbose)
    textIO.print2(f"Password: {password}", verbose)
    textIO.print2(f"Client Password: {clientPassword}", verbose)
    textIO.print2(f"Key: {key}", verbose)
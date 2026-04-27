from pytools import textIO
import signal, sys, json, os, time
from multiprocessing import shared_memory
from pathlib import Path

BASE_DIR = BASE_DIR = Path(__file__).resolve().parent
specs_json = Path(BASE_DIR / "dependencies" / "specs.json")
registry_folder_pydts = Path.home() / "Next Level Software Studio" / "Registry" / "PyDTS"
with open(specs_json, "r") as f:
    specs = json.load(f)
PYDTS_VERSION = specs["Version"]

def starting(memoryblockName, memoryblockSize=1024, verbose=False):
    # 1024 bytes = 1 KiB
    try:
        shm = shared_memory.SharedMemory(name=memoryblockName, create=True, size=memoryblockSize)
        def encerrar(signum, frame):
            print(f"\n[SINAL {signum}] Recebido. Desalocando '{memoryblockName}'...")
            shm.close()
            shm.unlink()
            textIO.print2("Memória liberada com sucesso. Encerrando processo.", verbose)
            sys.exit(0)
        signal.signal(signal.SIGTERM, encerrar)
        signal.signal(signal.SIGINT, encerrar)
        textIO.print2(f"Alocator process active (PID: {sys.modules['os'].getpid()})", verbose)
        textIO.print2(f'Block name: "{memoryblockName}"\nBlock size: "{memoryblockSize}" bytes', verbose)
        textIO.print2(f"Waiting for termination signal from the OS...", verbose)
        pid = registry_folder_pydts / f"{memoryblockName} PID.txt"
        with open(pid, "w") as f:
            f.write(str(sys.modules['os'].getpid()))
            f.flush()
            os.fsync(f.fileno())
            time.sleep(5)
        while True:
            signal.pause()
    except FileExistsError:
        print(f"Erro: A memória '{memoryblockName}' já está alocada no sistema.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


def connecting(clientName, verbose=False, clientPassword=None):
    textIO.print2(f"Setting up PyDTS ({PYDTS_VERSION})", verbose)
    





def shutdown(memoryblockName, verbose=False):
    textIO.print2(f"Shutting down PyDTS ({PYDTS_VERSION})...", verbose)
    pidFile = registry_folder_pydts / f"{memoryblockName} PID.txt"
    try:
        with open(pidFile, "r") as f:
            pid = int(f.read())
    except FileNotFoundError:
        textIO.print2(f"PID file for '{memoryblockName}' not found. It may have already been terminated.", verbose)
        sys.exit(0)
    except PermissionError:
        textIO.print2(f"Permission denied when trying to read PID file for '{memoryblockName}'.", verbose)
        sys.exit(1)
    try:
        os.kill(pid, signal.SIGTERM)
    except ProcessLookupError as e:
        textIO.print2("Processo não encontrado.", verbose)
    except PermissionError as e:
        textIO.print2("Permissão negada para encerrar o processo.", verbose)
    sys.exit(0)
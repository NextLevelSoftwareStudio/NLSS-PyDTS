from tabnanny import verbose
import signal, sys, json, os, time
from multiprocessing import shared_memory
from pathlib import Path
from .dependencies import lib_A
from pathlib import Path

BASE_DIR = BASE_DIR = Path(__file__).resolve().parent
specs_json = Path(BASE_DIR / "dependencies" / "specs.json")
registry_folder = Path.home() / "Next Level Software Studio" / "Registry" / "PyDTS"
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
            lib_A.verb("Memória liberada com sucesso. Encerrando processo.", verbose)
            sys.exit(0)
        signal.signal(signal.SIGTERM, encerrar)
        signal.signal(signal.SIGINT, encerrar)
        lib_A.verb(f"Alocator process active (PID: {sys.modules['os'].getpid()})", verbose)
        lib_A.verb(f'Block name: "{memoryblockName}"\nBlock size: "{memoryblockSize}" bytes', verbose)
        lib_A.verb(f"Waiting for termination signal from the OS...", verbose)
        pid = registry_folder / f"{memoryblockName} PID.txt"
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


def connecting(deviceNameverbose=False):
    lib_A.verb(f"Setting up PyDTS ({PYDTS_VERSION})", verbose)


def shutdown(memoryblockName, verbose=False):
    lib_A.verb(f"Shutting down PyDTS ({PYDTS_VERSION})...", verbose)
    pidFile = registry_folder / f"{memoryblockName} PID.txt"
    try:
        with open(pidFile, "r") as f:
            pid = int(f.read())
    except FileNotFoundError:
        lib_A.verb(f"PID file for '{memoryblockName}' not found. It may have already been terminated.", verbose)
        sys.exit(0)
    except PermissionError:
        lib_A.verb(f"Permission denied when trying to read PID file for '{memoryblockName}'.", verbose)
        sys.exit(1)
    try:
        os.kill(pid, signal.SIGTERM)
    except ProcessLookupError as e:
        lib_A.verb("Processo não encontrado.", verbose)
    except PermissionError as e:
        lib_A.verb("Permissão negada para encerrar o processo.", verbose)
    sys.exit(0)
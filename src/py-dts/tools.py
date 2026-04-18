import signal, sys, os
from multiprocessing import shared_memory
from pathlib import Path
from .dependencies import lib_A
def starting(memoryblockName, memoryblockSize=1024, verbose=False):
    # 1024 bytes = 1 KiB
    def verb(msg):
        if verbose:
            print(msg)
    try:
        shm = shared_memory.SharedMemory(name=memoryblockName, create=True, size=memoryblockSize)
        def encerrar(signum, frame):
            print(f"\n[SINAL {signum}] Recebido. Desalocando '{memoryblockName}'...")
            shm.close()
            shm.unlink()
            verb("Memória liberada com sucesso. Encerrando processo.")
            sys.exit(0)
        signal.signal(signal.SIGTERM, encerrar)
        signal.signal(signal.SIGINT, encerrar)
        verb(f"Alocator process active (PID: {sys.modules['os'].getpid()})")
        verb(f'Block name: "{memoryblockName}"\nBlock size: "{memoryblockSize}" bytes')
        verb(f"Waiting for termination signal from the OS...")
        while True:
            signal.pause()
    except FileExistsError:
        print(f"Erro: A memória '{memoryblockName}' já está alocada no sistema.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
def installing(verbose=True):
    def verb(msg):
        if verbose:
            print(msg)
    verb("Installing...")
    if str(lib_A.sistema(complete=True)).startswith("Windows"):
        startup = Path(os.environ["APPDATA"]) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
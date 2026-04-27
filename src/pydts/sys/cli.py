import argparse, sys, subprocess, os
current_dir = os.path.dirname(os.path.abspath(__file__))
dependencies_path = os.path.join(current_dir, '..', 'dependencies')
sys.path.append(os.path.abspath(dependencies_path))
def main():
    parser = argparse.ArgumentParser(prog="pydts", description="Ferramenta CLI pydts")
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis")
    setup_parser = subparsers.add_parser("deviceSetup", help="Configura o dispositivo")
    setup_parser.add_argument("--publicKey", required=True, help="Chave pública")
    setup_parser.add_argument("--serverIP", required=True, help="IP do servidor")
    setup_parser.add_argument("--user", required=True, help="Usuário")
    reg_parser = subparsers.add_parser("deviceRegistration", help="Regista o dispositivo")
    reg_parser.add_argument("--publicKey", required=True, help="Chave pública")
    reg_parser.add_argument("--serverIP", required=True, help="IP do servidor")
    reg_parser.add_argument("--user", required=True, help="Usuário")
    args = parser.parse_args()
    if args.command == "deviceSetup":
        deviceSetup(args.publicKey, args.serverIP, args.user)
    elif args.command == "deviceRegistration":
        deviceRegistration(args.publicKey, args.serverIP, args.user)
    else:
        parser.print_help()
def deviceSetup(public_key, server_ip, user):
    print('Initating device setup for:')
    print(f'User: {user}.')
    print(f'Device IP: {server_ip}.')
    print(f'Public Key: {public_key}.')
    print('Make sure both devices are connected using an Ethernet cable.')
    question = input('Are they connected? (yes/no): ')
    if question == "yes":
        try:
            subprocess.run(["ping", server_ip, "-c", "4"])
            subprocess.run([])
        except subprocess.CalledProcessError:
            print("Failed to ping the server.")
    elif question == "no":
        sys.exit(0)
def deviceRegistration(public_key, server_ip, user):
    print('Initating device registration for:')
    print(f'User: {user}.')
    print(f'Server IP: {server_ip}.')
    print(f'Public Key: {public_key}.')
    print('Make sure both devices are connected using an Ethernet cable.')
    question = input('Are they connected? (yes/no): ')
    if question == "yes":
        try:
            subprocess.run(["ping", server_ip, "-c", "4"])
            subprocess.run([sudo apt update])
        except subprocess.CalledProcessError:
            print("Failed to ping the server.")
    elif question == "no":
        sys.exit(0)
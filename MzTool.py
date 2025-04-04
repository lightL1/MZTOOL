import nmap
import socket
import pyfiglet

# Função para exibir o banner personalizado
def exibir_banner():
    banner = pyfiglet.figlet_format("Mz Tools")
    print(banner)

# Função para escanear dispositivos na sub-rede usando nmap com /24
def escanear_subrede(subrede="192.168.0.0/24"):
    dispositivos = []
    try:
        scanner = nmap.PortScanner()
        print(f"Iniciando varredura na sub-rede {subrede}...")
        scanner.scan(hosts=subrede, arguments="-p 554")  # Varredura na porta RTSP
        for host in scanner.all_hosts():
            print(f"Host ativo encontrado: {host}")
            if 'tcp' in scanner[host]:
                for porta, info in scanner[host]['tcp'].items():
                    if info['state'] == "open":  # Verifica se a porta RTSP está aberta
                        print(f"  Porta {porta} aberta - Serviço: {info.get('name', 'Desconhecido')}")
                        dispositivos.append((host, porta))
        return dispositivos
    except Exception as e:
        print(f"Erro ao escanear a sub-rede: {e}")
        return dispositivos

# Função para acessar o fluxo RTSP usando payloads comuns
def acessar_rtsp_stream(ip, porta=554):
    try:
        rtsp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rtsp_socket.settimeout(5)
        rtsp_socket.connect((ip, porta))
        print(f"Conexão estabelecida com {ip}:{porta}")

        # Enviar o comando OPTIONS
        rtsp_socket.send(f"OPTIONS rtsp://{ip}:{porta}/ RTSP/1.0\r\nCSeq: 1\r\n\r\n".encode())
        resposta = rtsp_socket.recv(4096).decode()
        print("Resposta OPTIONS:")
        print(resposta)

        # Enviar o comando DESCRIBE
        rtsp_socket.send(f"DESCRIBE rtsp://{ip}:{porta}/ RTSP/1.0\r\nCSeq: 2\r\n\r\n".encode())
        resposta = rtsp_socket.recv(4096).decode()
        print("Resposta DESCRIBE:")
        print(resposta)

        # Nota: Para SETUP e PLAY, URLs específicas de stream (como /video) seriam necessárias.
        # Encerrar a conexão
        rtsp_socket.close()
    except Exception as e:
        print(f"Erro ao acessar RTSP stream em {ip}:{porta}: {e}")

# Exemplo de uso das funções
if __name__ == "__main__":
    exibir_banner()

    subrede = input("Digite a sub-rede no formato CIDR (ex: 192.168.0.0/24): ")
    dispositivos = escanear_subrede(subrede)

    if dispositivos:
        print("\nTentando acessar streams RTSP nos dispositivos encontrados...\n")
        for ip, porta in dispositivos:
            acessar_rtsp_stream(ip, porta)
    else:
        print("Nenhum dispositivo RTSP encontrado.")
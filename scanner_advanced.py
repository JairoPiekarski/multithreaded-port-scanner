import socket
import threading
import json
from datetime import datetime

def get_banner(sock):
    try:
        return sock.recv(1024).decode().strip()
    except:
        return "Serviço desconhecido"
    
def scan_port(target, port, open_ports):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                banner = get_banner(sock)
                open_ports.append((port, banner))
    except Exception as e:
        pass

def main():
    target = input("Enter target IP address or hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    
    print(f"Scanning ports {start_port} to {end_port} on {target}...")
    start_time = datetime.now()
    
    open_ports = []
    threads = []
    
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port, open_ports))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    end_time = datetime.now()
    duration = end_time - start_time

    # if open_ports:
    #     print(f"\nOpen ports on {target}:")

    #     with open("scan_report.txt", "w") as f:
    #         f.write(f"RELATORIO DE SEGURANCA\nTarget: {target}\n")
    #         f.write(f"Duração: {duration}\n\n")

    #         for port, banner in sorted(open_ports):
    #             linha = f"Porta {port}: {banner}\n"
    #             print(linha)
    #             f.write(linha + "\n")

    #     print("Relatório salvo em 'scan_report.txt'")
    # else:
    #     print(f"\nNo open ports found on {target} in the specified range.")

    report_data = {
        "target": target,
        "duration": str(duration),
        "scan_date": str(datetime.now()),
        "open_ports": []
    }

    for port, banner in sorted(open_ports):
        report_data["open_ports"].append({
            "port": port,
            "service": banner
        })

    with open("scan_report.json", "w") as f:
        json.dump(report_data, f, indent=4)

    print("Relatório salvo em 'scan_report.json'")
    
    if open_ports:
        print(f"\nOpen ports on {target}:")
        for port, banner in sorted(open_ports):
            print(f"Port {port}: {banner}")
    else:
        print(f"\nNo open ports found on {target} in the specified range.")
    
    print(f"\nScan completed in {duration}")

if __name__ == "__main__":
    main()
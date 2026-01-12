# Scanner de Portas e Identificador de Serviços Multithreaded 🛡️

Este projeto é um scanner de rede desenvolvido em Python para identificação de portas abertas e serviços (Banner). Ele foi projetado com foco em performance e organização de dados para auditorias de segurança.

## 🚀 Funcionalidades
- **Alta Performance:** Utiliza a biblioteca `threading` para realizar varreduras simultâneas, reduzindo drasticamente o tempo de execução.
- **Identificação de Serviços:** Implementa captura de banners para identificar softwares rodando em portas abertas.
- **Relatórios Estruturados:** Exporta automaticamente os resultados para `scan_report.json`, facilitando o consumo por outras ferramentas ou análise posterior.
- **Interface Intuitiva:** Execução simples via CLI com inputs dinâmicos para alvo e intervalo de portas.

## 🛠️ Detalhes Técnicos
- **Socket Programming:** Uso do protocolo TCP (`SOCK_STREAM`) para verificar conectividade.
- **Multithreading:** Gerenciamento de múltiplas threads para otimização de I/O de rede.
- **Data Serialization:** Manipulação de arquivos JSON para persistência de dados.

## 📋 Como usar
1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/NOME_DO_REPO.git

   Execute o scanner:

## 📁 Exemplo de Saída (JSON)

O arquivo gerado (`scan_report.json`) segue o padrão abaixo, ideal para análise automatizada:

```json
{
    "target": "scanme.nmap.org",
    "duration": "0:00:01.520272",
    "scan_date": "2026-01-12 19:10:46.499469",
    "open_ports": [
        {
            "port": 22,
            "service": "SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.13"
        },
        {
            "port": 80,
            "service": "Servi\u00e7o desconhecido"
        }
    ]
}
```

## ⚠️ Aviso Legal (Disclaimer)

Este software foi desenvolvido exclusivamente para fins educacionais e testes de segurança autorizados. O uso desta ferramenta contra alvos sem permissão explícita é ilegal e pode acarretar em sanções criminais. O desenvolvedor não se responsabiliza pelo uso indevido deste código.

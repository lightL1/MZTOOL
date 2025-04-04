# MZTOOL
Descobre câmeras com falha rtsp 1.0 na rede local

Aqui está um guia rápido sobre como usar o código:

1. **Instale as dependências necessárias**:
   Antes de executar o código, certifique-se de instalar as bibliotecas necessárias:
   ```bash
   pip install python-nmap pyfiglet
   ```

2. **Execute o programa**:
   Salve o código em um arquivo, por exemplo, `mz_tools.py`, e execute-o no terminal:
   ```bash
   python mz_tools.py
   ```

3. **Escolha o que deseja fazer**:
   Ao rodar o programa, você verá as opções disponíveis:
   - **Sub-rede (S)**: Informe uma sub-rede no formato CIDR (ex.: `192.168.0.0/24`) para escanear todos os dispositivos RTSP na rede.
   - **IP manual (M)**: Insira o IP de um dispositivo específico para tentar acessar as informações RTSP.

4. **Resultados esperados**:
   - Na opção **Sub-rede (S)**, ele fará uma varredura e listará todos os dispositivos com a porta RTSP (554) aberta.
   - Na opção **IP manual (M)**, ele enviará comandos básicos RTSP (`OPTIONS` e `DESCRIBE`) para o dispositivo e exibirá as respostas recebidas, incluindo informações detalhadas sobre os fluxos RTSP.

5. **Exemplo de uso (caso você conheça o IP de uma câmera)**:
   - Execute o código e escolha "M" para inserir o IP.
   - Por exemplo, insira o IP `192.168.0.101`.
   - Se o dispositivo responder, o programa exibirá informações básicas e as opções disponíveis no servidor RTSP.

### Dicas:
- Certifique-se de que o dispositivo com a câmera RTSP está acessível na rede e que a porta 554 está aberta.
- Use o formato correto de sub-rede ou IP para evitar erros.
- Caso precise de autenticação no RTSP, você pode ajustar o código para incluir `username` e `password` nos comandos.

Se precisar de ajuda com configurações específicas ou ajustes no código, é só pedir! 🚀✨

from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ModbusException, ConnectionException
import time
# Cria um cliente Modbus TCP
client1 = ModbusTcpClient("192.168.2.10", port=502)

try:
    # Tentativa de conectar ao CLP
    if client1.connect():
        print("Conexão estabelecida com sucesso.")
        
        # Lê 1 coil começando no endereço 0
        client1.write_coils(0,[False])
        time.sleep(0.5)
        response = client1.read_input_registers(0, 1)
        print(type(response))
        if not response.isError():
            # Verifica se a resposta não contém erros
            print("Valor do Coil:", response.registers[0])
        else:
            print("Erro ao ler o coil:", response)
    else:
        print("Não foi possível estabelecer conexão com o CLP.")
except (ModbusException, ConnectionException) as e:
    print("Erro de Modbus ou problema de conexão:", str(e))
finally:
    # Sempre fecha a conexão
    client1.close()
    print("Conexão fechada.")

from pymodbus.client.sync import ModbusTcpClient

#LEMBRANDO - ESSE SCRIPT SERÁ O MODBUS MASTER

############### Instancia um cliente (slave) ###############
#nome   = classe          ip slave       porta (padrão)
client1 = ModbusTcpClient('192.168.2.10',port=502) #estação 1

############### Escrever no slave ###############
#obj    metodo      bit   valor
client1.write_coils(0   ,[True] *1)  #Seta BIT True
client1.write_coils(0   ,[False]*1)  #Seta BIT True

############### Ler o slave ###############
#variavel     obj    método                bit inicial   Quantidade a ser lida
valores    =  client1.read_discrete_inputs(0            ,10) 

############### Printa a quantidade de valores ###############
print(valores)
#A saída será uma lista, de 1o posições, com os resultados da leitura a partir do bit 0
#Exemplo de possível saída
#[0,1,0,1,0,1,0,1,0,1]

import serial
import time

# ⚠️ Ajuste a porta conforme seu PC
PORTA = "COM3"  # Windows exemplo
# Linux/Mac seria algo como "/dev/ttyACM0"

BAUD_RATE = 9600

def iniciar_servidor():
    try:
        print("Iniciando servidor...")
        ser = serial.Serial(PORTA, BAUD_RATE, timeout=1)
        time.sleep(2)  # Aguarda inicialização Arduino
        print("Servidor conectado. Aguardando dados...\n")

        while True:
            if ser.in_waiting > 0:
                linha = ser.readline().decode("utf-8").strip()
                if linha:
                    processar_log(linha)

    except Exception as e:
        print("Erro:", e)

def processar_log(dado):
    print("LOG RECEBIDO ->", dado)

if __name__ == "__main__":
    iniciar_servidor()
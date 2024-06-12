import serial
import datetime # Possivelmente nao necessaria por uso da biblioteca time
import socket
import time

#arduino = serial.Serial(port='', baudrate=, timeout=)

# Considerando que eh feito o tratamento dos dados anterior a adicao no banco, eh possivel guardar as ultimas tres leituras em lista
# Utilizando as ultimas tres leituras, eh possivel calcular a previsao de quando o tanque vai esvaziar ou quando vai terminar de encher
# Dessa forma, nao eh necessario leitura do banco de dados pelo servidor

def getArduinoData(x):
    data = arduino.readline()
    return data

def treatData(x):
    data = getArduinoData()
    # Obtem os dados via serial do arduino
    # Necessário transformar bytes em long


    # Obtem a data e hora em que foi recebida a leitura

    # Apos tratamento dos dados, criar tupla com tempo e dado tratado
    # Adicionar tupla ao banco de dados

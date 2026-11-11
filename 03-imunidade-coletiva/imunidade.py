P = int(input())
C0 = int(input())
TxC = float(input())
Imu = int(input())

PorcImu = P * (Imu / 100)
Dia = 0
CA = 0

while True:
    C0 = (C0 * TxC)
    Dia = Dia + 1
    CA = CA + C0
    if CA >= PorcImu:
        print(Dia)
        break

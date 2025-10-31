comprimentodapizza=int(input("Qual o comprimento da pista?Nao te atrevas a meter texto:"))
ndevoltasdacompetitione=int(input("E QUANTAS VOLTAS SAO?"))
COMOESTACLIMA=int(input("\n1-bom clima \n2-chuva:"))

distacia=comprimentodapizza*ndevoltasdacompetitione

Bomferr=(distacia/3)*2.5
Chuferr=(distacia/2.7)*2.5
BomfHoda:(distacia/3.4)*2.5
ChuHodar:(distacia/3)*2.5

if COMOESTACLIMA ==2:
    print("Para a ferrari Terenos um total de ",distacia,"km. como clima ta bom serao gastos", Bomferr)
else:
    print("Para a ferrari Terenos um total de ", distacia, "km. como clima ta mau serao gastos", Chuferr)

if COMOESTACLIMA ==2:
    print(" Para o Honda Terenos um total de ",distacia,"km. como clima ta bom serao gastos",BomfHoda)
else:
    print("Para o Honda Terenos um total de ", distacia, "km. como clima ta mau serao gastos", ChuHodar)





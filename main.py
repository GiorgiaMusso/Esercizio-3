#inserire parametri iniziali
print("Inserire l'intervallo temporale t [s]: ")
t = float(input())
print("Inserire la posizione iniziale x0 [m]: ")
x0 = float(input())
print("Scegliere il tipo di moto scrivendo 'u' per uniforme oppure 'a' per accelerato:")
moto = input()
#moto rettilineo uniforme
if(moto=="u"):
  print("Inserire velocità [m/s]: ")
  v_u = float(input())
  print("Spazio percorso in moto uniforme con velocità "+ str(v_u) + " [m/s]: ")
  x_u =(v_u*t)+x0
  print(x_u)
#moto rettilineo accelerato
elif(moto=="a"):
  print("Inserire velocità [m/s]: ")
  v_a = float(input())
  print("Inserire accelerazione [m/s^2]: ")
  acc = float(input())
  print("spazio percorso in moto accelerato con velocità "+ str(v_a) + " [m/s] e accelerazione " + str(acc) + " [m/s^2]: ")
  x_a =(acc*t*t/2)+(v_a*t)+x0
  print(x_a)
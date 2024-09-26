print("Cauculadora da Fórmula de Bhaskara: ")


valora = float(input("Digite o valor de a: "))
valorb = float(input("Digite o valor de b: "))
valorc = float(input("Digite o valor de c: "))

while valora == 0:
    print("O coeficiente a não pode ser igual a zero.")
    valora =  float(input("Digite o valor de a: "))

discriminante = (valorb ** 2) - 4 * valora * valorc


if discriminante < 0 : 
    print(f"Resultado: {discriminante}. A equação não possui raízes reais.")
elif discriminante == 0 :
    x1 = (-valorb / (2 * valora))
    print(f"A única raiz real é: {x1:.3f}.")
else: 
    x1 =  (-valorb + discriminante ** 0.5 / (2 * valora))
    x2 =  (-valorb - discriminante ** 0.5 / (2 * valora))
    print(f"As raizes reais são: {x1:.3f} e {x2:.3f}.")
   
   
   
      
   
   
   
    
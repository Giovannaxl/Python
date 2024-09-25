#Escreva um programa para caucular a redução do tempo de vida de um fumante
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou
#considere que um fumante perde 10 minutos de vida a cada cigarro,e caucule
#quantos dias de vida um fumante perderá.Exiba o total de dias


#Variáveis
cigarros_pordia= int(input("Digite a quantidade de cigarros: "))
anos_fumados= float(input("Digite por quanto tempo você fuma: "))

perda_em_minutos = anos_fumados * 360 * cigarros_pordia * 10
reducao_em_dias = perda_em_minutos / (4*60)
print(f"Você perdeu {reducao_em_dias:.2f} anos de vida")
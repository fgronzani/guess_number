
def guessing():
	import random, sys
	random_number=random.randint(0,100)
	guess=input("Estou pensando em um número entre 0 e 100, tente adivinhar\n")
	for trying in range(1,100):
		if int(guess)<random_number:
			guess=input("O número que eu pensei é mais alto\n")
		elif int(guess)>random_number:
			guess=input("O número que eu pensei é mais baixo\n")
		else:
			print("Parabéns! Você acertou em "+ str(trying)+ " tentativas")
			break
	answ_yn=input("Gostaria de jogar novamente ? y/n\n")
	while answ_yn!="n":
		guessing()
	else:
		sys.exit("Obrigado por jogar!")
guessing()




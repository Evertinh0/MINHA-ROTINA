# -*- coding: utf-8 -*-
"""
Autor: Everton yan de jesus souza
Criado: 12/04/2022
"""

print("")
print(" Um homem precisa atravessar um rio com um barco que possui capacidade ")
print(" de transportar apenas ele mesmo e mais uma de suas três cargas, que são: ")
print(" um lobo, um bode e uma caixa de alfafa. ")
print(" Indique as ações necessárias para que o homem consiga atravessar")
print(" o rio sem perder suas cargas. ")
print("")

print (" Lobo = 1")
print (" Bode = 2")
print (" Alfafa = 3")
print("")

print(" Qual será ordem correta para que joão consiga atravesar")
print(" o rio sem que o lobo nâo coma o bode, é o bode não coma a alfafa.")
viagem1 = int(input(" Digite aqui a opção: "))
if viagem1 == 1:
    print("")
    
    print(" Está correto, ")
    print(" Quem será o proximo a ser levado por seu joão? ")
elif viagem1 != 1:
    print(" Tente denovo ")
viagem2 = int(input(" Digite aqui a opção: "))   
if viagem2 == 3:
    print("")
    
    print(" Está correto, ")
    print(" Estamos quase lá, quem seu joão devera levar dessa vez?")
elif viagem2 != 3:
    print(" Tente denovo ")    
viagem3 = int(input(" Digite aqui a opção: "))   
if viagem3 == 2:
    print("")
    
    print(" Está correto, ")
    print(" Voce conseguiu, seu joão levou todos para o outro lado do rio.")
elif viagem3 != 2:
    print(" Tente denovo ")  


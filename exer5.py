# -*- coding: utf-8 -*-
"""exer5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rgwlqbvhjV9JTpVEvMHVSI4wm_SrEgCQ
"""

string_original = input("Digite uma string: ")  # solicita que o usuário digite uma string

string_invertida = ""

for i in range(len(string_original)-1, -1, -1):  # percorre a string original de trás para frente
    string_invertida += string_original[i]  # adiciona cada caractere ao final da string invertida

print("String original:", string_original)
print("String invertida:", string_invertida)
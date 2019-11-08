my_string = "Hola Mundo!"
print (my_string)

#Saltos de linea van entre 3 comillas dobles o simples
#Nota las comillas simples sirven para poner comillas dobles dentro del mensaje
my_string = '''Este es un mensaje \ncon saltos de linea \ncomo se puede observar \nBye'''
print(my_string)

#Diferentes maneras de concatenar strings
name = "Hector"
study = "Python3"
message_one = "Yo "+name+" Estoy aprendiendo "+study+"\n" #1
message_two = "Yo %s Estoy aprendiendo %s \n" %(name, study) #2
message_three = "Yo {} Estoy aprendiendo {} \n".format(name, study)

print(message_one + message_two + message_three)

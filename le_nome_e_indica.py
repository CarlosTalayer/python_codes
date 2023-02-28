# Lê o nome de uma cidade. Diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Qual o nome da sua cidade? ')).strip() # .strip elimina quaisquer espaços que tiver no nome digitado
print(cidade[:5].upper() == 'SANTO') # Com o nome SANTO em maiúsculas, indica que qualquer outra forma digitada será aceito.

# Entre os colchetes informa que tem 5 dígitos e deve ser cortado o início quando nada foi digitado.
# .upper informa que mesmo que digite letras maiúsculas misturadas será aceitável (True)
# == Verifica se o que foi digitado é igual a palavra santo

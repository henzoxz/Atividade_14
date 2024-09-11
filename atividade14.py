# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado
nota1 = int(input(" Digite a 1ª Nota "))
nota2 = int(input(" Digite a 2ª Nota "))
nota3 = int(input(" Digite a 3ª Nota "))
media = (nota1 + nota2 + nota3)/3


if(media>7):
    print(f" Sua media é {media} então você foi Aprovado ")

if(media==7):
    print(f" Sua media é {media} então você foi Aprovado ")

if(media<5):
    print(f" Sua media é {media} então você foi Reprovado ")

if(media==6):
    print(f" Sua media é {media} então você está de Recuperação ")

    print(media)
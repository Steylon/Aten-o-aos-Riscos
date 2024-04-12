# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


label start:
    #narrador 01
    voice "narrador/narrador 01.ogg"
    "Pedro, o porteiro do turno da manhã, estava em mais um dia tranquilo quando um rapaz toca o interfone da portaria" with dissolve

    voice "pedro/pedro dialogo 01.ogg"
    porteiro "Portaria do condomínio CondEduc, em que posso ajudar?" with dissolve

    voice "rodolfo/rodolfo dialogo 01.ogg"
    ladrao "Olá, me chamo Rodolfo, sou amigo da Maria do apartamento 402. Ela me convidou para passar o dia aqui." with dissolve

# label menu:
label escolha_primeiro:

    #firt menu:
    menu:

        "Liberar a entrada":

            #narrador 02
            voice "narrador/narrador 02.ogg"
            "Oh não, você liberou a entrada de um estranho sem se certificar antes, 
            ele invadiu um apartamento e roubou várias coisas de um morador!"

            #retorna para as perguntas!

            jump escolha_primeiro

        "Interfonar para o apartamento 402.":
            voice "narrador/narrador 03.ogg"
            "É isso aí! Sempre devemos interfonar antes para ter certeza se o visitante não é alguém mal intencionado!"

        # a frase abauxo irá aparecer na tela enquanto o menu estiver ativo

        "O que Pedro deve fazer?"

    voice "pedro/pedro dialogo 02.ogg"
    porteiro "Só um segundo, vou interfonar para ela." with dissolve

    voice "narrador/narrador 04.ogg"
    "Pedro interfona para o apartamento 402 mas ninguém atende." with dissolve

    voice "pedro/pedro dialogo 03.ogg"
    porteiro "Sinto muito, senhor, ninguém atendeu. Não posso liberar sua entrada." with dissolve

    voice "rodolfo/rodolfo dialogo 02.ogg"
    ladrao "Mas que bobagem, me deixe entrar! Eu já vim aqui várias vezes, você é novo aqui, por algum acaso?" with dissolve

# segundo menu

label segundo_escolha:

    menu: 
        "Interfonar novamente.":
            voice "narrador/narrador 05.ogg"
            "Parabéns! Interfonando novamente você pode assegurar se o morador conhece o visitante evitando assaltos e vandalismo!" with dissolve
        
        "Deixar ele entrar.":
            voice "narrador/narrador 06.ogg"
            "Você liberou acesso sem permissão do morador, o visitante acabou vandalizando vários lugares do condomínio." with dissolve
        
        # retorna ao menu segundo_minijogo:

            jump segundo_escolha
    voice "pedro/pedro dialogo 04.ogg"
    porteiro "Na verdade, eu trabalho aqui já tem 1 ano, senhor. Mas posso interfonar novamente." with dissolve

    voice "narrador/narrador 07.ogg"
    "Pedro tenta pela segunda vez, e novamente ninguém atende."

    voice "pedro/pedro dialogo 05.ogg"
    porteiro "Infelizmente ninguém atendeu, não posso autorizar sua entrada no prédio." with dissolve

    voice "rodolfo/rodolfo dialogo 03.ogg"
    ladrao "Isso é um absurdo! Eu vou reclamar com o síndico, pode esperar! "

    # voice "narrador/narrador 07.ogg"
    voice "narrador/narrador 08.ogg"
    "O homem foi embora e mais tarde, naquele mesmo dia, ele soube pelo seu amigo porteiro de outro condomínio." with dissolve
 
    voice "narrador/narrador 09.ogg"
    "Que esse rapaz entrou no condomínio e acabou roubando algumas coisas dos moradores." with dissolve

    voice "narrador/narrador 10.ogg"
    "Pedro ficou com a consciência limpa após tudo isso." with dissolve
    # fim de jogo!  
    return


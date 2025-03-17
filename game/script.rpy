# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pyo = Character("Pyo")
define k = Character("Kitties")
define p = Character("Protagonista")
define pl = Character("Pluey")

image red = Solid("#FF0000")

default shoes = True

transform pluey_zoom:
    zoom 7  # Adjust this number (e.g., 1.5 = 150% of original size)
    xpos 0.5 ypos 0.5 anchor (0.5, 0.5)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    p "(Kitties me invitó a ir a su casa.)"

    p "(Dijo algo sobre pasar un rato juntos.)"

    #scene bg room
    scene casa lejos

    p "(Creo que esa es su casa. Una casa blanca.)"

    scene casa puerta cerrada

    p "(Ahora que lo pienso...)"

    p "(Dicen que Kitties tuvo entrenamiento y que me puede desarmar 7 veces antes de tocar el suelo.)"

    p "(Tal vez no sea buena idea tocarle la puerta.)"

    menu:
        "Tocar la puerta.":
            jump lbl_tocar_puerta
        "Irse.":
            jump lbl_irse

label lbl_irse:
    p "(Ahora que lo pienso, creo que mejor lo dejo así.)"

    scene black

    p "(Mejor me voy con todas mis partecitas en donde deben de estar.)"

    "END: Te vas a tu casa."

    return

label lbl_tocar_puerta:
    p "(Bueno... Ya estoy aquí. De paso me dan agua y como.)"

    play audio knock_door

    "..."

    scene casa puerta abierta

    play audio open_door

    "???" "¿Hola...?"

    p "Hola, soy yo. Eres Kitties, ¿no?"
    extend " Me invitaste a tu casa hoy." 

    scene casa puerta abierta kitties sorprendido

    k "¡Ah! Tenía la duda de si ibas a llegar a la hora. ¡Pasa!"

    scene casa puerta abierta kitties feliz

    menu:
        "Pasar a la casa.":
            jump lbl_pasar_casa
        "No aceptar":
            jump lbl_no_pasar_casa

label lbl_no_pasar_casa:
    "(Ahora que lo pienso... No creo que sea buena idea pasar."
    extend " Quien sabe si pueda salir una vez entre.)"

    p "Sabes, creo que mejor otro día."
    extend " Dejé la estufa prendida y no hay nadie en mi casa."

    scene casa puerta abierta kitties confundido
    k "Oh, um... No te preocupes, no vaya a ser que tu casa explote o algo."
    k "Me avisas cuando llegues a tu casa."

    scene casa lejos abierta

    "..."

    #Crear imagen de calle
    scene calle

    p "(Estuvo cerca, casi me atrapa. Mejor ya me regreso a mi casa.)"
    
    show pluey cuchillo at pluey_zoom

    pl "¡Manos arriba y patas a la barriga!"

    pl "¡Dame esos zapatos, ya!"

    menu:
        "Defenderte.":
            play audio punch

            p "¡Toma!"

            "..."

            show pluey enojado

            pl "¡Ya te cargó el payaso!"

            play sound stab

            scene red with dissolve

            pause 1.0

            scene black with fade
            
            "END: Pluey te mató."

            return

        "Dialogar.":

            p "¡Está bien! ¡Está bien! Pero no me hagas nada. ¿No podemos razonar?"

            pl "¡Dame tus zapatos ya. Pero rápido!"

            menu:
                "Preguntar sobre su día.":
                    p "Pero... Pero no me has dicho como ha ido tu día."

                    show pluey enojado

                    pl "¿Mi día? ¡No te hagas güey! ¡Dámelos!"

                    play sound stab

                    scene red with dissolve

                    pause 1.0

                    scene black with fade
                    
                    "END: No pudiste evitar a Pluey."

                    return

                "Mencionar que se ve sexy.":
                    p "No me había dado cuenta, pero... Tu color verde, tu forma de limón... Hacen que te veas sexy."

                    pl "Hey..."

                    show pluey sonrojado

                    play music dating

                    extend " No había visto que bonitos ojos tienes."
                    
                    p "¿Bonitos... Ojos...?"

                    pl "Ahora los veo de cerca y no me había dado que los tienes bonitos."

                    pl "Sabes... Nomás quería tus zapatos, pero me estás robando el corazón."

                    pl "Dámelo."

                    play sound stab

                    scene red with dissolve

                    pause 1.0

                    scene black with fade
                    
                    "END: Justo en el corazón."

                    return


        "Negociar.":
            p "¿Qué es lo que quieres? ¡Dime y te lo doy!"

            pl "¡Te dije que me dieras tus zapatos!"

            p "¿Mis zapatos? ¡Toma, toma! ¡Ten!"

            play sound shoes

            "(Rápidamente me quito los zapatos...)"

            #Sacar imagen de Tims
            show shoes at Transform(zoom=0.4, xpos=0.7, ypos=0.6, anchor=(0.5, 0.4)) with dissolve

            $ shoes = False

            pl "¡Órale! ¡Quítese, solo damelos y vete!"

            jump lbl_volver_corriendo_casa

        "Escapar.":
            p "(Esperaré a que se distraiga y...)"

            menu:
                "Seguir corriendo a la calle.":
                    p "¡Déjeme solo! ¡AAAAAAH!"

                    play sound running

                    scene calle at Transform(zoom=1.5, xpos=0.5, ypos=0.5, anchor=(0.5, 0.4)) with dissolve

                    p "(¡No no no no no! ¡Son mis zapatos!)"

                    scene calle at Transform(zoom=2.0, xpos=0.5, ypos=0.5, anchor=(0.5, 0.3)) with dissolve

                    play sound running

                    pause 1.0

                    p "(Creo... Creo que ya lo perdí...)"

                    show pluey enojado at pluey_zoom

                    pl "¡Dame tus mugres zapatos!"

                    play sound stab

                    scene red with dissolve

                    pause 1.0

                    scene black with fade
                    
                    "END: No escapaste de Pluey."

                "Correr a casa de Kitties.":

                    jump lbl_volver_corriendo_casa
    return

label lbl_volver_corriendo_casa:
    p "¡Ah! ¡AAAAAAAAAAH!"

    play sound running

    scene casa lejos abierta

    pause 1.0

    scene casa puerta abierta kitties sorprendido with dissolve

    k "¡Oh! ¡Volviste!"

    scene casa puerta abierta kitties feliz

    p "Déjame pasar..."
    extend " ¡Déjame pasar ya!"

    scene casa puerta abierta kitties confundido

    k "O-Oh, u-um... ¡E-Está bien!"

    scene sala

    p "(Eso... Eso estuvo... Cerca...)"
    
    jump lbl_pasar_casa

label lbl_pasar_casa:
    scene sala

    p "(¿Esta... Es la casa de Kitties? La imaginé más grande y..."
    extend " Peligrosa.)"

    return


    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pyo = Character("Pyo")
define k = Character("Kitties")
define p = Character("Protagonista")
define pl = Character("Pluey")

image red = Solid("#FF0000")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    "Kitties me invitó a ir a su casa."

    "Dijo algo sobre pasar un rato juntos."

    #scene bg room
    scene casa lejos

    "Creo que esa es su casa. Una casa blanca."

    scene casa puerta cerrada

    "Ahora que lo pienso..."

    "Dicen que Kitties tuvo entrenamiento y que me puede desarmar 7 veces antes de tocar el suelo."

    "Tal vez no sea buena idea tocarle la puerta."

    menu:
        "Tocar la puerta.":
            jump lbl_tocar_puerta
        "Irse.":
            jump lbl_irse

label lbl_irse:
    "Ahora que lo pienso, creo que mejor lo dejo así."

    scene black

    "Mejor me voy con todas mis partecitas en donde deben de estar."

    "END: Te vas a tu casa."

    return

label lbl_tocar_puerta:
    "Bueno... Ya estoy aquí. De paso me dan agua y como."

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
    "Ahora que lo pienso... No creo que sea buena idea pasar."
    extend "Quien sabe si pueda salir una vez entre."

    p "Sabes, creo que mejor otro día."
    extend "Dejé la estufa prendida y no hay nadie adentro."

    scene casa puerta abierta kitties confundido
    k "Oh, um... No te preocupes, no vaya a ser que tu casa explote o algo."
    "Me avisas cuando llegues a tu casa."

    scene casa lejos abierta

    "..."

    scene calle

    "Estuvo cerca, casi me atrapa. Mejor ya me regreso a mi casa."
    
    show pluey cuchillo

    pl "¡Manos arriba y patas a la barriga!"

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

            p "¡Está bien! ¡Está bien! Pero no me hagas nada."

            pl "Así me gusta, sueltitos y obedientes."

            play music dating

            Pluey "Hey..."

            show pluey sonrojado

            extend "No había visto que bonitos ojos tienes."





    p "¡Ah! ¡No me hagas nada! ¡No me hagas nada!"

    return

label lbl_pasar_casa:
    return


    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

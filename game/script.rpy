# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Shizune = Character("Shizune", color="#72ADEE", what_suffix='"', what_prefix='"')
define Misha = Character("Misha", color="#FF809F", what_suffix='"', what_prefix='"')
define Hisao = Character("Hisao", color="#629276", what_suffix='"', what_prefix='"')
define Lilly = Character("Lilly", color="#f9eaa0",  what_suffix='"', what_prefix='"')
define Emi = Character("Emi", color="#FF8E7F", what_suffix='"', what_prefix='"')
define Rin = Character("Rin", color="#b14343", what_suffix='"', what_prefix='"')
define Meiko = Character("Meiko", color="#9C5051",  what_suffix='"', what_prefix='"')
define Saki = DynamicCharacter("saki_name", color="#b77029",  what_suffix='"', what_prefix='"')
define Chi = Character("Chisato", color="#cd4b34",  what_suffix='"', what_prefix='"')
define other = DynamicCharacter("other_name", color="#69b129",  what_suffix='"', what_prefix='"')
define Nori = Character("Noriko", color="#b849ab",  what_suffix='"', what_prefix='"')
define Saka = DynamicCharacter("saka_name", color="#9339c7",  what_suffix='"', what_prefix='"')
define Mutou = Character("Mutou", color="#bf7937",  what_suffix='"', what_prefix='"')
define Nurse = Character("Nurse", color="#ffffff",  what_suffix='"', what_prefix='"')
define Mae = Character("Maeda", color="#178a00",  what_suffix='"', what_prefix='"')
define Nomiya = Character("Nomiya", color="#e0e0e0",  what_suffix='"', what_prefix='"')

define Kyle = Character("Kyle", color="#f3f3f3",  what_suffix='"', what_prefix='"')

define SakiNvl = Character(None, kind=nvl, what_prefix="\"", what_suffix="\"", what_color="#b77029")
define HisaoNvl = Character(None, kind=nvl, what_prefix="\"", what_suffix="\"", what_color="#629276")

define story = nvl_narrator


image start_menu_bus_ride = "event/busride_ni.jpg"

# The game starts here.

label start:     

    scene start_menu_bus_ride
    with dissolve

    $ saki_name = "Saki"
    $ saka_name = "Saka"


    menu:
        "Where do you want to go?"

        "Act 1":
            jump act_1
        "Act 2":
            jump act_2
        "Act 3":
            jump act_3
        "Act 4":
            jump act_4

    return

label act_1:
    menu:
        "Where do you want to go?"

        "Scene 1":
            jump saki_sc1
        "Scene 2":
            jump saki_sc2
        "Scene 3":
            jump saki_sc3
        "Scene 4":
            jump saki_sc4

label act_2:
    menu:
        "Where do you want to go?"

        "Scene 5":
            jump saki_sc5
        "Scene 6":
            jump saki_sc6
        "Scene 7":
            jump saki_sc7
        "Scene 8":
            jump saki_sc8
        "Scene 9":
            jump saki_sc9
        "Scene 10":
            jump saki_sc10
        "Scene 11":
            jump saki_sc11
        "Scene 12":
            jump saki_sc12

label act_3:
    menu:
        "Where do you want to go?"

        "Scene 14":
            jump saki_sc14
        "Scene 15":
            jump saki_sc15
        "Scene 16":
            jump saki_sc16
        "Scene 17":
            jump saki_sc17
        "Scene 18":
            jump saki_sc18
        "Scene 19":
            jump saki_sc19
        "Scene 20":
            jump saki_sc20
        "Scene 21":
            jump saki_sc21
        "Scene 22":
            jump saki_sc22
        "Scene 23":
            jump saki_sc23
        "Scene 24":
            jump saki_sc24
        "Scene 25":
            jump saki_sc25

label act_4:
    menu:
        "Where do you want to go?"

        "Scene 26":
            jump saki_sc26
        "Scene 27":
            jump saki_sc27
        "Scene 28":
            jump saki_sc28
        "Scene 29":
            jump saki_sc29
        "Scene 30":
            jump saki_sc30
        "Scene 31":
            jump saki_sc31
        "Scene 32":
            jump saki_sc32
        "Scene 33":
            jump saki_sc33
        "Scene 34":
            jump saki_sc34
        "Scene 35":
            jump saki_sc35
        "Scene 36":
            jump saki_sc36
        "Scene 37":
            jump saki_sc37
        "Scene 38":
            jump saki_sc38
        





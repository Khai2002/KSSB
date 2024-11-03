label promo:

    scene black
    with delayblinds

    scene suburb_konbiniext
    show saki slightsmile_close at left
    with dissolve

    show Sprites_for_Chisato
    show Sprites_for_Noriko at right:
        xoffset -150

    Kyle "We are looking for sprite artist with similar style to Katawa Shoujo to draw characters of Learning to Fly."

    Kyle "With your Patreon support, we can commission more outfits for Saki, and sprites for Chisato and Noriko, and more CGs as well!"

    show saki slightsmile_close_ss
    with dissolve

    Kyle "If you enjoy our project, please consider supporting Stories Beyond on Patreon. We'll try our best to deliver you the best quality mod we can offer!"

    Kyle "And if you haven't got the chance to try out the game, be sure to give it a shot. The download link is down below. And be sure to give me some feedbacks once you're finished."


    scene thanksBG
    show thanks
    with delayblinds


    Kyle "Hi, my name is Kyle. I'd like to thank you for trying out our mod and I hope you are pleased with our work."

    Kyle "This is part of a larger project that we plan to do until 2024."

    Kyle "The story that you've played is Act 1 of Saki's story, which is 15 percent of the entire route. 
    By the time you're playing this, we are already on our way to make Act 2 a reality."

    Kyle "We hope to deliver it to you in the shortest amount of time, with the highest quality of course."

    Kyle "To do that however, we'd need your help."
    
    Kyle "If you enjoy our game and would like to support, you can do that through {a=https://www.patreon.com/KyleDaBoss}Patreon (clickable link).{/a}"

    Kyle "Your support will help us get more people on board and afford more CGs/Character Sprites (for example, sprites for Chisato and Noriko)."

    Kyle "Thank you so much and I hope you've enjoy your time here!"

    Kyle "This has been Katawa Shoujo: Stories Beyond, made with love from me and my friends. And I hope to see you later! Goodbye for now!"

    stop music fadeout 1.5

    pause(0.5)

    scene black
    with delayblinds

    return

label timeskip:

    
    stop sound fadeout 2.0
    stop music fadeout 2.0
    
    # if suppress_window_before_timeskip:
    #     window hide None
    # else:
    #     window hide
    # with Pause(2.0)


    scene black
    with Dissolve(1.0)

    pause(1.0)

    play music passing_of_time fadein 1.0

    show kslogo heart at Position(xalign=0.5, yalign=0.5) 
    with clockwipe

    scene black
    show kslogo words at Position(xalign=0.5, yalign=0.5) 
    with clockwipe

    with Pause(2.0)

    stop music fadeout 2.0

    scene black
    with clockwipe

    with Pause(2.0)

    # if not suppress_window_after_timeskip:
    #     window show

    # $ suppress_window_before_timeskip = False
    # $ suppress_window_after_timeskip = False

    return


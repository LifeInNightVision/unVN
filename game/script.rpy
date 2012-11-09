# You can place the script of your game in this file.

# Backgrounds go here
image bg outdoor = "outdoor.jpg"
image bg classroom = "classroom2.jpg"


# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image taro neutral = "taro-neutral.png"
image taro waving = "taro-waving.png"
image taro happy = "taro-happy.png"
image taro doubtful = "taro-doubtful.png"
image taro shy = "taro-shy.png"
image taro shocked = "taro-shocked.png"
image taro angry = "taro-angry with vein.png"
################################################
image bibi waving = "bibi-waving.png"
image bibi curious = "bibi-curious.png"
image bibi neutral = "bibi-neutral.png"
image bibi happy = "bibi-happy.png"
image bibi concentrating = "bibi-concentrating.png"
image bibi disappointed = "bibi-disappointed.png"
image bibi shocked = "bibi-curious.png"
################################################
image prof happy = "prof-happy.png"
image prof neutral = "prof-neutral.png"
image prof awkward = "prof-embarrassed.png"
image prof angry = "prof-angry.png"
################################################
image mina happy = "mina-happy.png"
image mina worried = "mina-worried.png"
image mina neutral = "mina-neutral.png"
################################################

# Declare characters used by this game.
define ta = Character('Taro', color="#cc3300", what_slow_cps=30)
define bi = Character('Bibi', color="#009933", what_slow_cps=30)
define pr = Character('Professor', color="#F7D358", what_slow_cps=30)
define mi = Character('Mina', color="#F781F3", what_slow_cps=30)
define na = Character('', what_slow_cps=30)


# The game starts here.
label start:

    #hero thinks in his head.mp3/speaking with teacher.mp3 goes here
    scene bg outdoor
    show taro happy at left
    
    
    window show

    ta "Hello! My name is Taro{w} and this is the world that I live in.{w} The world of Anime."    
    show taro neutral at left    
    ta "It doesn’t seem much different from the human world, since this world is a reflection of human imagination."    
    ta "Except for the fact that commoners in our world can easily fly, cast magic spells, and what not..."    
    show taro happy at left    
    ta "Just like this little creature here.{w} Her name is Bibi."    
    #street anthem.mp3 goes here
    show bibi waving at right
    bi "Hi Taro! Good Morning!"
    show taro waving at left
    
    menu:
    
        ta "Good morning, Bibi."
    
        "The school is this way! Where are you going?":
    
            show bibi neutral
            show taro doubtful    
            ta "Wait a minute...{w} The school is this way! Where are you going?"  
            show bibi happy
            bi "I am planning to go to the mountain to get some mushrooms..." 
            bi "...these mushrooms makes the eater laugh...{w} to death!"
            bi "Why don’t you join me?"
            show taro doubtful
            ta "Sounds fun... but what about school?"
            show bibi neutral
            bi "Oh, come to think of it..."
            show taro neutral
            show bibi happy
            bi "then...{w} let’s play hide and seek in the school!"
            show taro doubtful
            ta "Uh... Bibi, the school isn't for hide and seek!{w} It is for us to study."

    
        "Do you know when the test results will be out?":
    
            show bibi neutral
            show taro doubtful
            ta "Do you happen to know when the test results will be returned?"
            show bibi curious
            bi "What are you talking about?"
            ta "We took an exam in history class, remember?"
            show bibi neutral
            bi "Examination is the ritual in the school in which we all avoid talking each other" 
            show bibi curious
            bi "...and draw pictures on the paper, right?"            
            show taro doubtful
            bi "What will happen to it today, then?"
            ta "Well, today, professor will give us some points according to our performance in that...{w} ritual."
            show bibi happy
            bi "I see. It sounds very fun. Let’s go to school today..."
            show taro neutral
            bi "...instead of going to the mountain."
            show taro doubtful
            ta "You were actually planning to go to the mountain...{w} You didn't study for the exam, did you?"
        
        
        
    bi "huh?{w} What is...{w} 'study'?"
    show taro doubtful
    ta "You’ve been in school for years and you don’t know what studying is?!"
    show taro happy
    ta "To study is to learn letters, grammar, magic and the history of anime."
    show taro neutral
    ta "Bibi, do you know why we have to study?"
    show bibi curious
    bi "I have no idea at all.{w} I’ve never done 'study'."
    show taro doubtful
    ta "It's amazing how you can say that so proudly!"
    ta "Let's go to school..."
    
    #hero thinks in his head.mp3/speaking with teacher.mp3 goes here
    
    hide taro
    with Dissolve(.5)
    hide bibi
    with Dissolve(.5)
    na "According to our Professor, people of our world should be obliged to please humanity."
    na "We must be great and famous{w} just like our great alumni Hello Kitty, Son Gokuu and Rei Ayanami."
    na "My favorite character is Broly from Dragon Ball Z; the strongest Saiyan in the world."
    na "After his appearance in the three movies, we can now see him in minor productions on NicoNicoVideos!"
    na "Unfortunately, I was not designed to be a fighter.{w} I was desgined to be a small cute boy aimed at the Fujoshi layer."
    na "So even though I was born in this world of fantasy, my life is restricted by the law of nature that equally confines the free-will of mankind." 
        
    
    scene bg classroom
    with Dissolve(.9)
    
    show prof neutral
    with Dissolve(.7)
    
    pr "Gooten morgen everyone."
    pr "We have several things to cover up today. But before that,{w} I would like to announce that one of your classmates, Mina, was chosen as a main character of \"Magical Girl Pretty Mina\"!"
    show prof happy
    pr "I am delighted to know that one of my students was spotted by the makers and is going to be loved by many people!"
    pr "I hope that someday she’ll be a member of the pantheon of the great anime characters.{w} I would like to ask others to follow in her steps."
    pr "Would you like to say something, Mina?"
    
    show prof happy at left
    show mina happy at right
    with Dissolve(.6)
    
    mi "Good morning everyone. My name is Akaboshi Mina.{w} I am 15 years old."
    show mina worried at right
    mi "I am a bit clumsier than others...{w} That's how my character was designed."
    show mina neutral at right
    mi "One day a strange cat called El Tigre Chino appeared and made me into a magical girl." 
    show mina worried at right
    mi "El Tigre told me to fight evil powers...{w} but I'm really nervous..."
    show mina happy at right
    mi "Thank you for your support and nice to meet you."    
    hide prof
    hide mina
    
    show bibi disappointed at left
    show taro neutral at right    
    bi "Taro...{w} she is lying!{w} She is one day old."
    show taro shocked
    ta "Huh???{w} We have known her for years now!{w} How can you forget your friend?"
    show bibi shocked
    bi "No ways..."
    hide bibi
    hide taro
    
    show prof neutral
    pr "Next, I will return the results of your history test...{w} I was actually disappointed by the fact that some of you couldn't answer questions about Rei Ayanami despite my emphasis on her significance in the history of anime!" 
    hide prof
    show bibi curious
    bi "Professor, I have a question.{w} May I have your permission to ask it?"
    show prof happy at left
    show bibi neutral at right
    pr "Yes?" 
    bi "Who is this...{w} Rei Ayanami?"
    show prof awkward
    na "...{w} the class goes silent{w} ..."
    hide prof
    show taro shocked at left
    ta "D-Don't you know Rei Ayanami?"
    show bibi curious
    bi "I don’t know at all."
    hide bibi
    hide taro
    
    show prof angry
    pr "Bibi...{w} you must study more..."
    show prof neutral
    pr "Rei Ayanami is a heroine of a very famous anime.{w} A lot of people have been fascinated by her mysterious, loyal, and innocent personality. She was very elegant with her slender body and short blue hair." 
    pr "The emergence of Ayanami was the turning point in the history of anime heroines along with the series itself.{w} More importantly, she is the pioneer of the so-called \"ku-dere\" or \"expressionless but loving characters.\"" 
    show prof happy
    pr "Some of the prime \"ku-dere\" characters, Yuki Nagato, Jinno Nagi, and Ku-ko exist because of her.{w} Even today, we can feel her influence."
    pr "She is one of the best role models for you, my dear students."

    show bibi concentrating at right
    show prof neutral at center
    bi "I see... I understood...{w} But, where is Rei Ayanami?{w} I want to make friends with her."
    show prof awkward
    pr "Well, Bibi, she is not a very friendly person...{w} Actually, she is schizophrenic, and it is not easy for her to relate with society." 
    show prof neutral
    pr "Moreover, she is too great and it is difficult for you to be her friend."  
    show bibi disappointed
    bi "I understood that she is not friendly and I cannot be her friend. But can I see her picture? I cannot find one in the history book."
    show prof awkward
    pr "For some reasons, we cannot show you her pictures here..."
    show bibi curious
    bi "Why can't you show her pictures here?{w} Is it because she is always naked?"

    show taro angry at left
    ta "(I am sure you knew her all along){w} Legally speaking, we cannot use any character's pictures without permission from the maker." 
    show taro neutral
    ta "To show a picture of Rei Ayanami, we need permission from Gainax that we don’t have." 
    show bibi disappointed
    bi "Huh? It is so complicated."
    show prof happy
    pr "You have learnt well Taro.{w} Anyway, time to return the results."
    show bibi curious
    bi "Before that, I have another question.{w} May I have your permission to ask it, Professor?"
    pr "Bibi, are you finally becoming serious about your study? What is your question?"
    show bibi neutral
    bi "I do not understand the meaning of the word on the board."
    show prof awkward
    show taro shocked
    na "The board says \'Rei Ayanami\'"
    pr "…………………………"






    return

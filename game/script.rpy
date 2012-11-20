# You can place the script of your game in this file.

# Step 1 - Copy Paste from actual script
# Step 2 - Correct grammar and convert to more spoken English. Syntax it into character speech
# Step 3 - Add characters with expressions/backgrounds etc; 
# Step 4 - play and simultaneously give final touches (repeat till perfected)

# Step ? - Music?

# Backgrounds go here
image bg outdoor = "outdoor.jpg"
image bg classroom = "classroom2.jpg"
image bg home = "house2.jpg"
image bg eoVolOne = "EndofVolumeOne.png"


# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image taro = "taro-neutral.png"
image taro waving = "taro-waving.png"
image taro happy = "taro-happy.png"
image taro doubtful = "taro-doubtful.png"
image taro shy = "taro-shy.png"
image taro shocked = "taro-shocked.png"
image taro angry = "taro-angry with vein.png"
image taro curious = "taro-curious.png"
image taro disappointed = "taro-disappointed.png"
image taro shocked = "taro-shocked.png"
image taro worried = "taro-disappointed.png"
################################################
image bibi waving = "bibi-waving.png"
image bibi curious = "bibi-curious.png"
image bibi = "bibi-neutral.png"
image bibi neutral = "bibi-neutral.png"
image bibi happy = "bibi-happy.png"
image bibi concentrating = "bibi-concentrating.png"
image bibi disappointed = "bibi-disappointed.png"
image bibi shocked = "bibi-curious.png"
################################################
image prof happy = "prof-happy.png"
image prof = "prof-neutral.png"
image prof awkward = "prof-embarrassed.png"
image prof angry = "prof-angry.png"
image prof worried = "prof-worried.png"
################################################
image mina happy = "mina-happy.png"
image mina worried = "mina-worried.png"
image mina = "mina-neutral.png"
image mina shocked = "mina-shocked.png"
image mina disappointed = "mina-disappointed.png"
################################################
image tmom = "taros mom-neutral.png"
image tmom angry = "taros mom-angry.png"

# Declare characters used by this game.
define ta = Character('Taro', color="#B2A997", what_slow_cps=30)
define bi = Character('Bibi', color="#96AD40", what_slow_cps=30)
define pr = Character('Professor', color="#D2AB71", what_slow_cps=30)
define mi = Character('Mina', color="#E9AC95", what_slow_cps=30)
define tm = Character('Taro\'s Mom', color="#A6201D", what_slow_cps=30)
define na = Character('', what_slow_cps=30)


############################################################################################################# 


# The game starts here.
label start:

    #memories.mp3 goes here
    scene bg outdoor
    show taro at left
    with Dissolve(.6) 
    
    window show
    
    ta "Hello! My name is Taro{w} and this is the world that I live in.{w} The world of Anime."   
    ta "It doesn’t seem much different from the human world, since this world is a reflection of human imagination."    
    ta "Except for the fact that commoners in our world can easily fly, cast magic spells, and what not..."    
    show taro happy at left    
    ta "Just like this little creature here.{w} Her name is Bibi."    
    
        
    #Urban Spy 2.mp3 goes here
    
    show bibi waving at right
    with Dissolve(.6)
    bi "Hi Taro! Good Morning!"

    
    na "This small creature with light green hair is called Bibi."
    na "To begin with, I don't think she is human... First, she is normally hovering in the air." 
    na "Add to that, even though I address her as I would address a girl, nobody really knows if she is a girl or a boy."
        
    show taro waving at left        
    ta "Good morning, Bibi."
      
    na "Wait, she is coming from the school where we are supposed to go.{w} She is probably planning to skip the class meeting like she normally does."
    na "I've heard from the others that she claimed to be lost in the mountains or oversleeping, when asked." 

    
    
    menu:

        na "In today's case, maybe she wants to avoid the class where the results of the history exam will be returned. I should ask her..."
        
    
        "The school is this way! Where are you going?":
    
            show bibi
            show taro doubtful    
            ta "Wait a minute...{w} The school is this way! Where are you going?"  
            show bibi happy
            bi "I am planning to go to the mountain to get some mushrooms..." 
            bi "...these mushrooms makes the eater laugh...{w} to death!"
            bi "Why don’t you join me?"
            show taro doubtful
            
            na "Mushrooms that can kill by laughter...{w} I've never heard of this variety before."
            na "Even though I'm curious,{w} school comes first."
            
            ta "Sounds fun... but what about school?"
            show bibi
            bi "Oh, come to think of it..."
            show taro
            show bibi happy
            bi "then...{w} let’s play hide and seek in the school!"
            show taro doubtful
            
            na "Explaning even the simplest of tasks to her is a big challenge. One has to describe even the simplest concept in excruciating detail."
            
            ta "Uh... Bibi, the school isn't for hide and seek!{w} It is for us to study."

    
        "Do you know when the test results will be out?":
    
            show bibi
            show taro doubtful
            ta "Do you happen to know when the test results will be returned?"
            show bibi curious
            bi "What are you talking about?"
            ta "We took an exam in history class, remember?"
            show bibi
            bi "Examination is the ritual in the school in which we all avoid talking each other" 
            show bibi curious
            bi "...and draw pictures on the paper, right?"            
            show taro doubtful
            bi "What will happen to it today, then?"
            
            na "As expected, she doesn't know what's going on in school..."
            
            ta "Well, today, professor will give us some points according to our performance in that...{w} ritual."
            show bibi happy
            bi "I see. It sounds very fun. Let’s go to school today..."
            show taro
            bi "...instead of going to the mountain."
        
            
            na "Between test results and hiking in the mountain, I believe hiking would be more fun."
            na "But it is good that she realized that we are going to school."
            
        
            show taro doubtful
            ta "You were actually planning to go to the mountain...{w} You didn't study for the exam, did you?"
        
        
        
    bi "huh?{w} What is...{w} 'study'?"
    show taro doubtful    
    na "*sigh*{w} She has a habit of asking about the most basic of things..."
    ta "You’ve been in school for years and you don’t know what studying is?!"
    show taro happy
    ta "To study is to learn letters, grammar, magic and the history of anime."
    show taro
    ta "Bibi, do you know why we have to study?"
    show bibi curious
    bi "I have no idea at all.{w} I’ve never done 'study'."
    show taro doubtful
    ta "It's amazing how you can say that so proudly!"
    ta "Let's go to school..."
    
    #memories.mp3 goes here
    
    hide taro
    with Dissolve(.5)
    hide bibi
    with Dissolve(.5)
    na "According to our Professor, people of our world should be obliged to please humanity."
    na "We must be great and famous{w} just like our great alumni Hello Kitty, Son Gokuu and Rei Ayanami."
    na "My favorite character is Broly from Dragon Ball Z; the strongest Saiyan in the world."
    na "After his appearance in the three movies, we can now see him in minor productions on NicoNicoVideos!"
    na "Unfortunately, I was not designed to be a fighter.{w} I was designed to be a small cute boy aimed at the Fujoshi layer."
    na "So even though I was born in this world of fantasy, my life is restricted by the law of nature that equally confines the free-will of mankind." 
    
    #############################################################################################################     
    
    scene bg classroom
    with Dissolve(.9)
    

    na "The bell rings and the class begins. The professor enters and greets everyone like any other day..."

    #Diving Turtle.mp3 goes here
    show prof
    with Dissolve(.7)
    
    pr "Gooten morgen everyone."
    pr "We have several things to cover up today. But before that,{w} I would like to announce that one of your classmates, Mina, was chosen as a main character of \"Magical Girl Pretty Mina\"!"
    show prof happy
    pr "I am delighted to know that one of my students was spotted by the makers and is going to be loved by many people!"
    pr "I hope that someday she’ll be a member of the pantheon of the great anime characters.{w} I would like to ask others to follow in her steps."
    pr "Would you like to say something, Mina?"
    
    show prof happy at left
    with Dissolve(.6)
    show mina happy at right
    with Dissolve(.6)
    
    na "A girl with pinky hair, stands in front of the class.{w} She has been a classmate of me and Bibi for the past few years."
    

    
    mi "Good morning everyone. My name is Akaboshi Mina.{w} I am 15 years old."
    show mina worried at right
    mi "I am a bit clumsier than others...{w} That's how my character was designed."
    show mina at right
    mi "One day a strange cat called El Tigre Chino appeared and made me into a magical girl." 
    show mina worried at right
    mi "El Tigre told me to fight evil powers...{w} but I'm really nervous..."
    show mina happy at right
    mi "Thank you for your support and nice to meet you."    
    hide prof
    with Dissolve(.6)
    hide mina
    with Dissolve(.6)
    
    
    na "Finishing her mimicry of old magical girls, Mina goes back to her seat."
    
    #urban spy 2.mp3 goes here
    show bibi disappointed at left
    with Dissolve(.6)
    show taro at right    
    with Dissolve(.6)
    bi "Taro...{w} she is lying!{w} She is one day old."
    show taro shocked
    ta "Huh???{w} We have known her for years now!{w} How can you forget your friend?"
    show bibi shocked
    bi "No ways..."
    hide bibi
    with Dissolve(.6)
    hide taro
    with Dissolve(.6)
    
    
    #diving turtles.mp3 goes here
    show prof
    with Dissolve(.6)
    pr "Next, I will return the results of your history test...{w} I was actually disappointed by the fact that some of you couldn't answer questions about Rei Ayanami despite my emphasis on her significance in the history of anime!" 
    hide prof
    with Dissolve(.6)
    
    na "Professor writes the name on the black board and starts preaching about old Japanese animations...{w} Not this again..."
    
    show bibi curious
    with Dissolve(.6)
    bi "Professor, I have a question.{w} May I have your permission to ask it?"
    show prof happy at left
    with Dissolve(.6)
    show bibi waving at right
    
    
    na "Face filled with curiosity, Bibi raises her hand."
    
    pr "Yes?"
    
    #urban spy 2.mp3 goes here 
    show bibi at right
    bi "Who is this...{w} Rei Ayanami?"
    show prof awkward
    na "...{w} the class goes silent{w} ..."
    hide prof
    show taro shocked at left
    with Dissolve(.6)
    ta "D-Don't you know Rei Ayanami?"
    show bibi curious
    bi "I don’t know at all."
    hide bibi
    hide taro
    with Dissolve(.6)

    
    show prof angry
    with Dissolve(.6)

    
    na "Clearly dissatisfied, the professor frowns."
    
    pr "Bibi...{w} you must study more..."
    show prof
    pr "Rei Ayanami is a heroine of a very famous anime.{w} A lot of people have been fascinated by her mysterious, loyal, and innocent personality. She was very elegant with her slender body and short blue hair." 
    pr "The emergence of Ayanami was the turning point in the history of anime heroines along with the series itself.{w} More importantly, she is the pioneer of the so-called \"ku-dere\" or \"expressionless but loving characters.\"" 
    show prof happy
    pr "Some of the prime \"ku-dere\" characters, Yuki Nagato, Jinno Nagi, and Ku-ko exist because of her.{w} Even today, we can feel her influence."
    pr "She is one of the best role models for you, my dear students."

    show bibi concentrating at right
    with Dissolve(.6)
    show prof at center
    bi "I see... I understood...{w} But, where is Rei Ayanami?{w} I want to make friends with her."    
    
    na "Bibi's second question isn't even related to the exam anymore! Is this really a question or is she just messing around..."
    
    show prof awkward
    pr "Well, Bibi, she is not a very friendly person...{w} Actually, it is not easy for her to relate with society." 
    show prof
    pr "Moreover, she is too great and it is difficult for you to be her friend."  
    show bibi disappointed
    bi "I understood that she is not friendly and I cannot be her friend. But can I see her picture? I cannot find one in the history book."
    show prof awkward
    pr "For some reasons, we cannot show you her pictures here..."
    show bibi curious
    bi "Why can't you show her pictures here?{w} Is it because she is always naked?"

    show taro angry at left
    with Dissolve(.6)
    ta "(I am sure you knew her all along){w} Legally speaking, we cannot use any character's pictures without permission from the maker." 
    show taro
    ta "To show a picture of Rei Ayanami, we need permission from Gainax that we don’t have." 
    show bibi disappointed
    bi "Huh? It is so complicated."
    show prof happy
    pr "You have learnt well Taro.{w} Anyway, time to return the results."
    show bibi curious
    bi "Before that, I have another question.{w} May I have your permission to ask it, Professor?"
    pr "Bibi, are you finally becoming serious about your study? What is your question?"
    show bibi
    bi "I do not understand the meaning of the word on the board."
    show prof awkward
    show taro shocked
    na "The board says \'Rei Ayanami\'"
    pr "oh god..."
    
    hide prof
    with Dissolve(.6)
    hide taro
    with Dissolve(.6)
    na "........."
    hide bibi
    with Dissolve(.6)
    
    #diving turtles.mp3 goes here    
    na "The test results are returned. Students express their satisfaction, dissatisfaction, amazement or a sigh of relief as they receive their results." 
    
    show taro disappointed at left
    with Dissolve(.6)
    ta "80 on 100...{w} Could've been better.{w} But, I can still hope for an A.{w} Mina, how was it?"
    show mina happy at right
    with Dissolve(.6)
    mi "...{w} 90!{w} Better than I expected. I am glad it turned out this way!"
    
    na "Now that I think of it, Mina has always been a good student. She is good in all the subjects and her athletic ability stands out in this class filled with magical creatures." 
    na "Add to that, unlike the maid-cafe maids training at our university, she is not clumsy at all!"
    
    show bibi happy at center
    with Dissolve(.6)
    bi "Taro and Mina, look at my score! This is very fun to see!"
    
    #urban spy 2 .mp3 goes here
    na "With a big smile, she shows us her result."
    
    show mina shocked
    show taro shocked
    mi "Zero?!?!{w} ......you wrote your name wrong..."
    show taro curious
    ta "Wait a second... in the 'Name' section, why does it say...{w}  \"Rest in Peace?\""
    show bibi
    bi "I found the phrase beautiful and healing that's why!"
    show mina disappointed
    show taro doubtful
    mi "This phrase is for the dead you know..."
    bi "But... but...{w} No body dies in the world of fantasy."
    hide taro
    with Dissolve(.6)
    hide mina
    with Dissolve(.6)
    hide bibi
    with Dissolve(.6)
    
    
    #diving turtles.mp3 goes here    
    show prof
    with Dissolve(.5)
    pr "Do you have any question about your scores?{w} If no, then class dismissed." 
    show prof worried
    pr "err... Bibi...{w} can I have a word with you?"
    hide prof
    with Dissolve(.6)
    show bibi at right
    with Dissolve(.6)
    bi "Yes, Ma'am. I understood."
    
    na "She replies in a cheerful voice. It seems she doesn't understand the implication of that call."
    
    show bibi happy
    
    #Urban Spy 2.mp3 goes here

    bi "Taro, it seems professor will give me something."
    show taro doubtful at left
    with Dissolve(.6)
    
    na "...As expected..."
    
    ta "I don’t think so..."
    show taro
    show bibi
    bi "Do you think so?{w} In that case,{w} let’s go to the sea!"
    show taro disappointed
    ta "But weren't you called by the Professor just now?"
    show bibi happy
    bi "Oh yeah..."
    show bibi
    bi "I almost forgot that she would give me something."
    show taro shocked
    ta "............"
    
    show bibi shocked
    bi "Taro! Taro!{w} I’ve acquired flying spell very recently."
    
    na "...Flying spell?{w} ...Of course she knows that! She has been hovering the day since I met her."
    
    ta "Huh?{w} Aren't you flying all the times?"
    show bibi
    bi "No, no. This is a different one!" 
    show bibi concentrating
    
    na "I feel a chill go down my spine."
    
    bi "Behold, I will show you the power of...{w} \'the force\'!"
    hide taro
    with Dissolve(.6)
   
    na "Bibi casts the Zoom spell..." 
    hide bibi
    with Dissolve(.6)
    na "...and with that their party bumps into the ceiling!"
    na "THUD!"
    na "Bibi releases the spell and they both fall down!"
    na "THUD!!!"
    na "Somehow Bibi lands perfectly{w} but Taro doesn't..."
    na "Groaning in agony, Taro manages to stand up..."
    show taro angry at left
    with Dissolve(.3)
    ta "Don't{w} EVER{w} use that spell in class...{w} especially with the teachers in the next room!"
    show bibi happy at right
    with Dissolve(.6)
    bi "hee{w}hee{w}hee{w} Don’t you wanna know why you are listed in my party?"
    ta "That was my next question. Why am I in your party without knowing that?"
    show bibi curious
    bi "Because it is your destiny."
    show taro doubtful
    ta "What???"
    show bibi waving
    bi "I am leaving now.{w} See you soon."
    hide bibi
    with Dissolve(.5)
    na "Saying so, Bibi flies away..."
    show taro disappointed
    ta "Why did she have to use that spell from Dragon Quest instead of just flying like she normally does?{w} jeez..."
    show mina at right
    with Dissolve(.6)
    mi "Let's wait and see what the professor tells her. This might be interesting."
    show taro doubtful
    ta "Well, I am a bit worried about her..."

#############################################################################################################    
    
    na "Taro and Mina leave..."


    hide taro
    with Dissolve(.6)
    hide mina
    with Dissolve(.6)

    #gentle thoughts 1.mp3
    na "...leaving Bibi and the Professor alone in the classroom.{w} The Professor's irritation with Bibi and passion to regenerate the delinquent creates a dark purple aura."
    na "Unaware of what is coming next, Bibi continues smiling...{w} It would have been easier for the Professor if Bibi was angry, violent and vicious, like a real delinquent."
    
    
    show prof worried
    with Dissolve(.6)
    pr "Bibi, your scores have been bad from the start...{w} To top it, this time you filled your name as 'Rest in Peace!'"
    show prof angry
    pr "Writing your name wrong is one thing but this...{w} this is very offensive."
    show prof worried
    pr "I'm afraid you can't get through your campus life like this..."
    show prof worried at left
    with Dissolve(.6)
    show bibi at right
    with Dissolve(.6)
    bi "Huh?{w} 'Rest in Peace' means to stop working and to be happy...{w} right?"
    bi "What is wrong with the phrase?"
    show prof worried
    
    na "The Professor's concern is clearly visible."
    
    pr "I am sincerely worried about your future. What do you normally do after class?"
    show bibi curious
    bi "I eat what I like.{w} I go play in the mountains and the seas.{w} I talk with other characters.{w} I sleep in the air." 
    show bibi happy
    bi "This is how the creator designed me..."

    show prof angry
    show bibi curious
    pr "So all you do is eat, play, chat and sleep?"
    show prof worried
    show bibi
    pr "But you have to be a good student. Do you know why this university is free?"
    show prof angry
    pr "I'm sure you know nothing.{w} The citizen of this world want you to be loved by mankind."
    pr "It enables you to be like our great alumni. This also helps the world of fantasy to progress."
    show prof worried
    pr "To be loved by many people, you must finish your training in this university first."
    show prof
    pr "That is why many anime characters donate funds towards us."
    show bibi happy
    bi "Thank you very much for explanation.{w} I am relieved that this university is still free."
    show prof angry
    pr "That's not what I'm saying! I'm explaning why you need to study!"
    show bibi disappointed
    bi "I don’t have to study for I am not designed for studying. Come on, this is the world of fantasy."
    bi "The university should be a place for the students to nurture own characteristics."
    show prof awkward
    pr "I get your point. But don't you want to be something in the future?"
    show prof worried
    pr "The more you act like that, the more difficult it will be for you to survive this highly competitive world."
    show bibi concentrating
    bi "I will become what I will be as I have been.{w} I will never die as I am a concept, not a human."
    show prof angry
    pr "That's it.{w} I have nothing more to say.{w} You are dismissed."
    show bibi waving
    
    na "Professor's dark purple aura not only comes from her inability to convince Bibi but also due to the fact that she herself is bound, in a way."
    na "What Bibi said shattered professor's ego{w} as a professor{w}, as someone who has the right to dominate the truth."
    
    bi "kthxbai..."
    hide bibi
    with Dissolve(.6)
    na "............."
    hide prof
    with Dissolve(.6)

    na "Meanwhile in the corridor..."
    show taro shocked at left
    with Dissolve(.6)
    show mina disappointed at right
    with Dissolve(.6)
    ta "How can she even say that?!?!?!"
    mi "That was very...{w} interesting." 
    show mina worried
    mi "We have seen something unusually...{w} great..."
    show taro curious
    ta "What do you mean?"
    show mina happy
    mi "I will become what I will be as I have been. I have been Mina, and I will be Mina forever."

############################################################################################################# 

    scene bg outdoor
    with Dissolve(.9)
    #Warm Interlude.mp3 goes here

    #na "Taro and Mina head home."
    
    na "The school has ended for today. The sun is about to set. Mina and I decide to walk home together."
    
    
    show taro shy at left
    with Dissolve(.6)
    
    ta "By the way, you were chosen as the main character of an upcoming anime, right?{w} Congratulations!"
    show mina happy at right
    with Dissolve(.6)
    mi "Wehihihihi...{w} Thanks. But, it is not easy to complete my responsibility."
    
    na "It is very rare to see Mina being weak like this.{w} There must be something she is worried about. I should ask..."
    

    menu:
        
        "Are you nervous about being a MAIN CHARACTER?":
            show taro curious
            ta "Are you nervous about being a main character?"
            show mina worried
            mi "I am a bit nervous but morely, I am happy to be a main character. Actually, I was worried if my life had ended as a one of the background mob characters."
            show mina happy
            show taro
            mi "I am very happy that I was chosen as somebody important."
            show taro doubtful
            ta "Then, what is the problem?"
            show mina worried
            mi "It is about the safety of our lives. You know... We are not safe anymore."
            show mina worried
            mi "The conditions of hiring a magical girl are completely different from the Sailor Moon days."
            ta "I see... Being a magical girl is not easy anymore I guess."
            show taro
            ta "Look at me, I have no serious danger of losing my life. I don’t have to fight."
            show mina disappointed
            mi "But, you never accomplish your dream of being a Super Saiyan either, did you?"
            show taro shocked
            ta "Well... that's true..."
            show taro
            ta "...as Bibi said, maybe this is my nature.{w} I should be happy with my state."
            show mina
            mi "Well, I think so too..."
    
            na "It seems a life of magical girl is much more dangerous these days. One of the reasons is the demand from people who want to watch 'real' fight of young girls." 
            na "One of the most famous magical girls in our time was called the 'White Devil Magician Girl' for her relentless attack toward both villains and other magical girls."
            na "It is possible that a magical girl can lose her life. Still, their daily lives seem more meaningful and lively to me."
    

    
        "Are you nervous about being a MAGIC GIRL?":
            show taro curious
            ta "Are you nervous about being a magic girl?"
            show mina worried
            mi "Well, in a way, yes. A life of a magical girl is not safe anymore."
            show taro worried
            show mina shocked
            mi "Did you know... recently, one of our alumni died in the third episode of the anime!" 
            show mina worried
            mi "I think it disappoints magic girl anime fans who expect the warmth and the victory of the righteous on a typical Sunday morning." 
            mi "Think about my position...{w} I have to fight very seriously now, since that death went viral and affected many other people."
            ta "I see. Things seem to be getting very serious these days." 
            ta "The life of an anime character is not very safe ever since the launch of Neon Genesis of Evangelion. But, maybe we should be happy with our own destiny."
            show mina disappointed
            mi "I don't think you understand my situation here."
            show taro doubtful
            ta "Well, my problem is a bit different than yours. I can't be a super star like you, even if I wanted."
            show mina worried
            mi "Oh, I am so sorry..."
    
            na "It seems the life of magical girl is much more dangerous these days. One reasons is because of people who want to watch 'real' fights." 
            na "One of the most famous magical girls in our time was called the 'White Devil Magician Girl' for her relentless attack toward both villains and other magical girls."
            na "It is possible that a magical girl can lose her life. Still, their daily lives seem more meaningful and lively to me."
    

############################################################################################################# 

    scene bg home
    with Dissolve(.9)
    
    #memories.mp3 goes here
    
    na "Back home, taro thinks to himself"
    ta "I wonder what Bibi is upto right now. Was she just trying to piss professor off or did she really mean everything she said?"
    ta "...and what was that all about, being in her party because it was my destiny..."
    ta "I hear footsteps...{w} Someone is approaching my room."
    
    show tmom at right
    with Dissolve(.6)
    tm "Taro, have you finished your homework yet?"
    
    na "This is my mom.{w} Everytime she talks to me like that, it feels like school continues at home."
    
    show taro disappointed at left
    with Dissolve(.6)
    ta "I don’t have to."

    
    #kickstarter.mp3 goes here
    show tmom angry
    tm "You aren't getting supper till you finish your home work, young man."
    show taro angry
    ta "But mom... I don’t have to study. I am great the way I am. I want to be myself forever."
    
    na "I was tempted to imitate Bibi as my mother spoke exactly like the Professor."
    
    tm "What are you talking about? If you will forever be the way you are, we will be in a tight spot." 
    tm "Study hard, work hard, be like Rei Ayanami or Son Goku and get money for us! Stop being a fool!" 
    tm "Didn't you learn anything from your Naruto senpai?"
    tm "Listen, even if you don't need money, you will need food and you can't even buy a meal the way you are!"
    tm "So stop spouting nonsense and finish your homework before the food gets cold."
    hide tmom
    na "She storms out and slams the door..."
    show taro disappointed
    ta "Guess I don't have a choice..."
    hide taro
    with Dissolve(.6)
    
    #memories.mp3 goes here

    ta "As I said earlier, unfortunately, I am restricted by this nature of humanity."
    ta "I need food to sustain myself. Bibi's way of life doesn't really apply here."

    #end of volume one
    
    scene bg eoVolOne
    with Dissolve(.6)


    return

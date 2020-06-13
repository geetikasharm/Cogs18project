import string

def canonicalize(input_string):
    #make all words lowercase
    temp_string = input_string.lower()
    #remove punctuation
    temp_string = ''.join([x for x in temp_string if x not in string.punctuation])
    #put each words into list
    out_list = temp_string.split()
    return out_list

def select_topic(input_string):
    #user can select one of three possible topics, or can choose to exit and end chatting
    blm_words = set(['black', 'lives', 'matter', 'blm', 'message'])
    george_words = set(['murder', 'george', 'floyd'])
    police_words = set(['police', 'brutality', 'history'])
    exit_words = set(['stop', 'exit', 'quit', 'out'])

    #function to probabilisitically interpret the user's input
    def compute_probs(input_string):
        input_set = set(input_string)
        blm_prob = len(input_set.intersection(blm_words)) / len(blm_words)
        george_prob = len(input_set.intersection(george_words)) / len(george_words)
        police_prob = len(input_set.intersection(police_words)) / len(police_words)
        exit_prob = len(input_set.intersection(exit_words)) / len(exit_words)
        output_dict = {'blm': blm_prob, 'gf': george_prob, 'pb': police_prob, 'exit': exit_prob}
        return output_dict

    #get probs and max prob
    probs = compute_probs(input_string)
    #gets key of max value from dictionary
    max_prob = max(probs, key=probs.get)

    #checks first to see if user wishes to leave else checks if any responses are likely
    if probs['exit'] > 0:
        output = 'exit'
    elif probs[max_prob] == 0:
        output = ""
    else:
        output = max_prob

    return output

def said_yes(response):
    yes_responses = ['y', 'ye', 'yes', 'yeah', 'yea']
    return any([x in yes_responses for x in response])

def have_a_chat():

    """Main function to run our chatbot."""
    #George Floyd, Polic Brutality, and BLM Movement, respectively
    topics = ['gf', 'pb', 'blm']
    #responses to topics
    george = "\nGeorge Floyd was a 46 year old black man living in Minneapolis. He had an altercation with the police that ended his life. On May 25, 2020 the police were called on a fake bill found at the store. The incident led to Floyd being handcuffed and forced on the ground with officer Derek Chauvin's knee on his neck for 8 minutes and 26 seconds. After repeating that he couldn't breathe, George Floyd died according to an independent autopsy report from asphyxiation. Floyd was a coach, a father, a son and a citizen who had his life taken over a non-threatening alleged issue.\nUnfortunately, George Floyd is among the thousands of Black lives that are killed every year. Other American citizens like Breonna Taylor and Ahmaud Abery along with countless others who have had their lives ended over police brutality are being advocated to reopen their cases to start a fresh investigation in order to get justice. Would you like to learn more about these stories? "
    history = "\nThe history of the modern police originated in the American south from slave patrols whose primary purpose was to in order to 1) chase down, apprehend and return runaway slaves 2) provide a form of organized terror to deter slave revolts and 3) maintain a form of discipline for slaves, if violated any plantation rules. During the Jim Crow era, these police departments developed primarily as means to control freed slaves who were now laborers in the agricultural system. Currently, California has updated their spending plan which adds a $147.5 million increase to the police budget, resulting in excessive militarization of the police force. Due to recent uprisings of American civilians in the peaceful protest of excessive police force on Black lives, the police have been equipped with gear such as tear gas, rubber bullets, armour, batons, shields and water cannons to deter and disband these protesters which have been causing deaths. Would you like to know more about the history of police brutality in the United States? "
    black_lives = "\nThis paragraph's source is the Black Lives Matter's website about their movement: '#BlackLivesMatter was founded in 2013 in response to the acquittal of Trayvon Martin’s murderer. Black Lives Matter Foundation, Inc is a global organization in the US, UK, and Canada, whose mission is to eradicate white supremacy and build local power to intervene in violence inflicted on Black communities by the state and vigilantes. By combating and countering acts of violence, creating space for Black imagination and innovation, and centering Black joy, we are winning immediate improvements in our lives.' Would you like to learn more about the Black Lives Matter movement? "

    topics_dict = {'gf': george, 'pb': history, 'blm': black_lives}

    george_website = "\nFor more info, visit https://www.dosomething.org/us/articles/black-lives-taken"
    history_website = "\nFor more info, visit https://www.smithsonianmag.com/smithsonian-institution/long-painful-history-police-brutality-in-the-us-180964098/"
    blm_website = "\nFor more info, visit https://blacklivesmatter.com/"

    website_dict = {'gf': george_website, 'pb': history_website, 'blm': blm_website}


    while len(topics) > 0:

        #initial greeting introducing the topics of discussion
        greet = '\nHello, I am #BLM Bot! I am here to inform you of recent events involving the murder of George Floyd, the history of police brutality and the message of the Black Lives Matter movement. Which would you like to hear about first? '

        # Get a message from the user
        msg = input(greet)

        # Prepare the input message
        msg = canonicalize(msg)

        #select topic from input message
        topic = select_topic(msg)

        #if user wants to exit
        if topic == 'exit':
            break

        #restarts loop because user input was invalid
        if not topic or topic not in topics:
            print("\nI'm sorry, try another response!")
            continue

        #getting here means input is valid
        #removing topic means it can't be selected again
        topics.remove(topic)

        #ask new question and get yes/no response
        response = canonicalize(input(topics_dict[topic]))

        #if no, ask if they want to continue chatting, else loop restarts
        if not said_yes(response):
            second_response = canonicalize(input("\nWould you like to learn more about the other topics described? "))
            if said_yes(second_response):
                continue
            else:
                break
        else:
            print(website_dict[topic])

    print('\nThank you so much for listening! Here is a link to some petitions you can sign in order raise awareness and importance for other less known cases: https://www.bleumag.com/2020/06/03/30-blm-petitions-you-should-sign-right-now/. Stay safe!')

have_a_chat()

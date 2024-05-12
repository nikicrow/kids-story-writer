from openai import OpenAI
import streamlit as st

# function to get response from model
def getresponse(plotline):
    client = OpenAI()
    
    # Prompt template
    template = f"""
                Act as an experienced childrens book writer. Use simple words a kids ages 10-13 would understand. 
                Pay attention to pacing, suspense, and character growth to create a short story that will engage kids ages 10-13 and ignite their imagination.
                Make sure to maintain a consistent tone and writing style. Make sure and the plot is cohesive and engaging.
                Make sure the characters are consistent and the interactions between characters maintain a interesting but consistent dynamic.
                Use the plotline given below to write the short story.
                Make sure the story is appropriate for children. Do not include adult themes or excessive gore or violence.
                ```
                {plotline}
                ```
                Write the short story in less than 1000 words.
                """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": template},
            {"role": "user", "content": "Can you generate a short story given the plotline?"}
        ]
    )
    print(response)

    return response

# page config
st.set_page_config(page_title="AI Short Story Writer",
                   page_icon=':books:',
                   layout='centered',
                   initial_sidebar_state='expanded')

st.header("AI Short Story Writer")
st.write("Made for Andrew, William, Peter, Isaiah and Annie!")
password = st.sidebar.text_input("Password to use the app")
st.sidebar.write("Made by Aunty Niki :two_hearts:")

# input from user
plotline=st.text_area("Write a brief summary of the plotline for the short story you want me to write", height=5)

submit = st.button("Generate")

if password != st.secrets['APP_PASSWORD']:
    st.warning('Check password!', icon="⚠️")
elif submit and password == st.secrets['APP_PASSWORD']: 
    with st.status('👩🏾‍🍳 Whipping up your short story...', expanded=True) as status:
        next_chapter_response = getresponse(plotline)
        st.header('Short Story')
        st.write(next_chapter_response.choices[0].message.content)

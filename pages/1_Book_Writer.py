from openai import OpenAI
import streamlit as st

# function to get response from model
def getresponse(input_text="Nothing written so far",plotline="",no_words=600):
    client = OpenAI()
    
    # Prompt template
    template = f"""
                Act as an experienced childrens book writer. Use simple words a kids ages 10-13 would understand. 
                Pay attention to pacing, suspense, and character growth to create a short story that will engage kids ages 10-13 and ignite their imagination.
                Make sure to maintain a consistent tone and writing style that aligns with the rest of the book.
                Make sure the characters are consistent and the interactions between characters maintain a interesting but consistent dynamic.
                Make sure and the plot is cohesive and engaging. 
                End with a cliff hanger that makes a reader want to continue to read.
                Write the next chapter of a book given the previous chapters of the book below. Use the plotline as well as the extra notes on the characters and scene.
                Make sure the story is appropriate for children. Do not include adult themes or excessive gore or violence.
                The following input gives the book so far.
                ```
                {input_text} 
                ```
                Use the plotline given below to write the next chapter.
                ```
                {plotline}
                ```
                Write the chapter in less than {no_words}
                """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": template},
            {"role": "user", "content": "Can you generate the next chapter of the childrens book using the style and characters of the book given so far and the plotline of the next chapter?"}
        ]
    )
    print(response)

    return response

# page config
st.set_page_config(page_title="AI Kids Book Writer",
                   page_icon=':books:',
                   layout='centered',
                   initial_sidebar_state='expanded')

st.header("AI Kids Book Writer :book:")
st.write("Made for the McGill kiddos")
password = st.sidebar.text_input("Password to use the app")
st.sidebar.write("Made by Aunty Niki :two_hearts:")


# input from user
input_text=st.text_area("Input the book so far", height = 15)
plotline=st.text_area("Write a brief summary of the plotline for the next chapter you want me to write", height=5)
no_words = st.text_input('Maximum number of words for the chapter you want me to write')

submit = st.button("Generate")

if password != st.secrets['APP_PASSWORD']:
    st.warning('Check password!', icon="⚠️")
elif submit and password == st.secrets['APP_PASSWORD']: 
    with st.status('👩🏾‍🍳 Whipping up your next chapter...', expanded=True) as status:
        next_chapter_response = getresponse(input_text,plotline,no_words)
        st.header('Next Chapter')
        st.write(next_chapter_response.choices[0].message.content)

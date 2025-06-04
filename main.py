import streamlit as st
import numpy as np

# Character data with emojis and quotes
characters = {
    "Ross Geller": {
        "img": "images/ross.jpg",  # Add this image to your folder too
        "quote": "“We were on a break!”"
    },
    "Rachel Green": {
        "img": "images/rachel.jpg",
        "quote": "“No uterus, no opinion.”"
    },
    "Monica Geller": {
        "img": "images/monica.jpg",
        "quote": "“Welcome to the real world! it sucks. you're gonna love it!”"
    },
    "Chandler Bing": {
        "img": "images/chandler.png",  # .png in your folder
        "quote": "“Could I *be* wearing any more clothes?”"
    },
    "Phoebe Buffay": {
        "img": "images/phoebe.jpg",
        "quote": "“Smelly Cat, Smelly Cat, what are they feeding you?”"
    },
    "Joey Tribbiani": {
        "img": "images/joey.jpg",
        "quote": "“How you doin’?”"
    }
}

# Result logic
def get_character(score):
    if score <= 15:
        return "Ross Geller"
    elif score <= 22:
        return "Rachel Green"
    elif score <= 29:
        return "Monica Geller"
    elif score <= 35:
        return "Chandler Bing"
    elif score <= 40:
        return "Phoebe Buffay"
    else:
        return "Joey Tribbiani"

# Streamlit app
def app():
    st.set_page_config(page_title="🎬 Friends Character Quiz", layout="centered")

    st.markdown("<h1 style='text-align: center;'>🌟 Which Friends Character Are You?</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Answer the questions below and find your Central Perk twin! ☕</p>", unsafe_allow_html=True)

    # Quiz questions
    questions = [
        "How do you feel about sarcasm? 😏",
        "How detail-oriented and organized are you? 📋",
        "Do you handle breakups well? 💔",
        "Do you believe in love at first sight? 💘",
        "How often do you crack jokes? 😂",
        "How spontaneous and adventurous are you? 🎉",
        "How much do you care about your hairstyle? 💇",
        "Do you play any musical instruments? 🎸",
        "Are you naturally competitive? 🏆"
    ]

    choices = [
        "Not at all", 
        "A little", 
        "Sometimes", 
        "Often", 
        "Very much"
    ]
    
    answers=    []
    for i in range(0, len(questions), 3):
        row = st.columns(3)
        for j in range(3):
            if i + j < len(questions):
                with row[j]:
                    st.markdown(f"**{questions[i + j]}**")
                    ans = st.radio(
                        "", 
                        choices, 
                        index=None, 
                        key=f"q{i + j}", 
                        label_visibility="collapsed"
                    )
                    if ans is not None:
                        answers.append(choices.index(ans) + 1)
                    else:
                        answers.append(None)




    # Button
    if st.button("💡 Reveal My Character!"):
        if any(a is None for a in answers):
            st.warning("Please answer all questions before continuing!")
        else:
            # Extract numeric values from strings like "1️⃣ Not at all"

            result = get_character(np.sum(answers))

            char = characters[result]

            st.markdown(f"<h2 style='text-align: center;'>🎉 You are most like <span style='color:#f63366'>{result}</span>!</h2>", unsafe_allow_html=True)
            st.image(char["img"], use_column_width=True)
            # st.markdown(f"<p style='text-align: center; font-style: italic;'>“{char['quote']}”</p>", unsafe_allow_html=True)



if __name__ == "__main__":
    app()

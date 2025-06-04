import streamlit as st
import numpy as np


# Character data with emojis and quotes
characters = {
    "Ross Geller": {
        "img": "images/ross.jpg",
        "quote": "“We were on a break!”",
        "fact": (
            "You've been married three times—yes, *three*—and somehow still believe in love (we admire the optimism). "
            "As a PhD-level paleontologist, you’re incredibly passionate about dinosaurs, fossils, and correcting people’s grammar. "
            "And let’s not forget the time you whitened your teeth so much they literally glowed in black light."
        )
    },
    "Rachel Green": {
        "img": "images/rachel.jpg",
        "quote": "“No uterus, no opinion.”",
        "fact": (
            "You once left your fiancé at the altar and jumped headfirst into adulthood with just a coffee cup and a dream. "
            "You’ve grown into a confident, stylish fashion buyer who knows what she wants. "
            "You also know how to stand your ground—especially when it comes to voicing the important things."
        )
    },
    "Monica Geller": {
        "img": "images/monica.jpg",
        "quote": "“Welcome to the real world! It sucks. You're gonna love it!”",
        "fact": (
            "You're the queen (or king!) of cleanliness, competition, and cooking. "
            "You’ve hosted Thanksgiving dinner more times than anyone can count, and your attention to detail is legendary. "
            "You're fiercely loyal, a natural leader, and your apartment is probably spotless right now."
        )
    },
    "Chandler Bing": {
        "img": "images/chandler.png",
        "quote": "“Could I *be* wearing any more clothes?”",
        "fact": (
            "Sarcasm is basically your second language. You make awkward situations even more awkward—but hilariously so. "
            "You work in...well, no one really knows exactly what you do. But you’re dependable and secretly have a huge heart. "
            "You also might just be the funniest person in the room, even if it's by accident."
        )
    },
    "Phoebe Buffay": {
        "img": "images/phoebe.jpg",
        "quote": "“Smelly Cat, Smelly Cat, what are they feeding you?”",
        "fact": (
            "You’re wonderfully eccentric, spiritually open, and unbothered by anyone’s opinions. "
            "You’ve lived on the street, sung at Central Perk, and taught us that weird is wonderful. "
            "Also, your songs are unforgettable—especially when they're about cats with gastrointestinal issues."
        )
    },
    "Joey Tribbiani": {
        "img": "images/joey.jpg",
        "quote": "“How you doin’?”",
        "fact": (
            "You're charming, loyal, and probably thinking about your next sandwich right now. "
            "Your acting career may have its ups and downs, but your heart is always in the right place. "
            "And let’s be honest—you never share food. Ever. And we love you for it."
        )
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
    # st.image("images/logo.png", width=50)  # Adjust path and size

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
            st.balloons()  # or 
            # st.snow()

            st.markdown(f"<h2 style='text-align: center;'>🎉 You are <span style='color:#f63366'>{result}</span>!</h2>", unsafe_allow_html=True)
            st.image(char["img"], use_column_width=True)
            st.markdown(f"<p style='text-align: center; font-style: italic;'>{char['quote']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center; font-size: 18px;'>{char['fact']}</p>", unsafe_allow_html=True)




if __name__ == "__main__":
    app()

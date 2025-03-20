import streamlit as st
import random

# Set up the page layout and title
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🚀", layout="centered")

# Title of the app
st.title("Growth Mindset Challenge 🚀")

# Introduction message
st.markdown("""
    Welcome to the Growth Mindset Challenge! 🌱
    A growth mindset is the belief that your abilities and intelligence can be developed with time and effort.
    Embrace the challenges ahead, learn from feedback, and keep improving! 💪
""")

# Random Growth Mindset Challenge Questions
challenges = [
    "Think of a recent challenge you faced. How did you approach it? What did you learn from the experience? 🤔",
    "Describe a time when you failed at something. How did you bounce back from that experience? 💡",
    "What is one area of your life where you would like to develop a growth mindset? What steps can you take to grow in that area? 🌱",
    "List a few things you could do to push yourself out of your comfort zone and face challenges more effectively. 🚀",
    "Think of someone who embodies a growth mindset. What qualities do they have that you admire? 🌟"
]

# Display a random challenge from the list
challenge = random.choice(challenges)
st.markdown(f"### **Challenge of the Day:**\n\n{challenge}")

# User input to reflect on the challenge
user_response = st.text_area("How would you respond to this challenge? Share your thoughts:", height=200)

# Response handling and feedback
def handle_response():
    if user_response:
        st.success("Great job! Keep embracing challenges and improving! 💪")
        st.write(f"**Your response:**\n\n{user_response}")
    else:
        st.warning("Please share your thoughts before submitting. 📝")

# Button to submit response
submit_button = st.button("Submit Response", key="submit", on_click=handle_response)

# Display a motivational quote
st.write("---")
st.markdown("**Motivational Quote** 🧠")
st.write("""
    "It's not that I'm so smart, it's just that I stay with problems longer."
    - Albert Einstein
""")

# Button to get another challenge
st.markdown('<div style="text-align: center;"><button>Get Another Challenge 🔄</button></div>', unsafe_allow_html=True)

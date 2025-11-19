import streamlit as st
import pickle
import random

# Load the trained model and vectorizer
with open("sentiment_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Define chatbot responses
positive_responses = [
    "That's amazing to hear! 😊 Moments like this are worth holding onto 💫. Be proud of how far you’ve come and how you’re feeling right now 🙌. You deserve all the joy you’re experiencing, and I hope it keeps flowing into every part of your life 🌈. Keep shining—your energy is inspiring! ✨",

    "What a beautiful moment you're in right now 🌞. Whether it’s peace, happiness, or motivation, I’m so glad you're feeling it 🧡. Take a second to soak it all in—you’ve earned this 🏆. Let this feeling remind you that good things are always possible, and they can return when you least expect it 🍀.",

    "Hearing that you're doing well truly brightens the day ☀️. Keep nurturing the things that lift you up, whether it's people, passions, or little moments of calm 🌿. The more you invest in your well-being, the more powerful your light becomes. Keep glowing and growing 🌻.",

    "That's the spirit! 💥 Your positivity is contagious, and it’s a beautiful thing 💖. Let this be your reminder that you're capable of creating joy—not just for yourself, but for others too 🌟. When you’re in a good place, everything around you starts to bloom 🌸. Keep that energy alive!",

    "Yes! Celebrate those wins, no matter how big or small 🎉. Every good day, every positive emotion, is worth recognizing 🌟. Let this moment fuel you for the journey ahead—you’re building something beautiful inside and out 🧱. Keep believing in the good things, because you’re living proof they exist 🌈.",

    "It’s so refreshing to hear that you're feeling good 💚. Hold onto that feeling—bottle it up and revisit it whenever you need a boost 🫶. Positive moments like these are reminders that growth and healing are real, and they’re happening inside you every single day 🌼. Keep going, you're doing wonderfully."
]

negative_responses = [
    "I know things might feel overwhelming right now 😞, but it's important to remember that you don’t have to have it all figured out today 🧭. Life comes with ups and downs ⛰️, and you’re allowed to take it one step at a time 👣. What matters most is that you keep going, even if all you can manage today is to take a deep breath 🌬️ and hold on. You are doing better than you think 💪.",
    
    "It’s okay to not be okay 💔. Struggles don’t mean you’re weak—they mean you’re human 🌱. You’re allowed to feel what you’re feeling without guilt or shame 🙏. But please don’t let those feelings convince you that you’re stuck 🕳️. You have the ability to grow through what you’re going through 🌻, and in time, this pain will shape you into someone even stronger 🦋.",
    
    "Everyone has moments where they doubt themselves or feel weighed down by life 🌧️. It doesn't mean you're failing ❌. It means you're facing something difficult, and that in itself is a sign of courage 🛡️. Keep showing up for yourself, even on the hard days 💖. You never know how close you might be to a breakthrough ✨.",
    
    "You might not see it right now, but there’s a quiet strength in you 🔥. Every single day that you’ve made it through until now, you’ve proven that strength 💫. The feelings you have today won’t last forever 🕰️, and your future is still full of potential 🌈. Don’t give up on yourself—great things can still come from this chapter, even if it’s a hard one 📖.",
    
    "When life feels heavy 🪨, it’s okay to pause and rest 🧘‍♀️—but never forget how far you’ve come 🛤️. Every challenge you've faced has prepared you for this moment 🏋️. You have survived storms before ⛈️, and you’ll make it through this one too 🌤️. The path ahead may not be easy, but it is still yours to walk 🚶, and it’s worth walking 💎.",
    
    "You might be facing things others don’t see 👀, and that’s not easy. But the very fact that you're still here, still trying, still moving forward 🚀—that’s proof of your resilience 💖. Take a moment to appreciate your own strength 🪞. You deserve compassion, from others and from yourself 🫂. You are worthy of peace and healing 🕊️."
]

# Function to generate chatbot response & sentiment label
def get_chatbot_response(user_input):
    user_input_tfidf = vectorizer.transform([user_input])
    sentiment = model.predict(user_input_tfidf)[0]
    
    if sentiment == 1:
        return random.choice(positive_responses), "🙂 Positive Sentiment"
    else:
        return random.choice(negative_responses), "☹️ Negative Sentiment"

# Set Streamlit page config
st.set_page_config(page_title="Mental Health Chatbot", page_icon="🌟", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
    
    .main { 
        font-family: 'Poppins', sans-serif;
        padding: 1.5rem;
        max-width: 800px;
        margin: 0 auto;
    }
    
    .stTitle {
        color: #2E4057;
        text-align: center;
        margin-bottom: 2rem;
        font-size: 2.5rem !important;
    }
    
    .stChatMessage {
        font-size: 16px !important;
        margin: 1rem 0;
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .stChatMessage.user {
        background: linear-gradient(135deg, #6B9AC4 0%, #4B7BE5 100%);
        border-radius: 15px;
        padding: 15px;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .stChatMessage.assistant {
        background: linear-gradient(135deg, #FF9A8B 0%, #FF6A88 100%);
        border-radius: 15px;
        padding: 15px;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .sentiment-label {
        font-size: 14px;
        color: #666;
        font-style: italic;
        margin-top: 5px;
        padding: 5px 10px;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.9);
        display: inline-block;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #6B9AC4 0%, #4B7BE5 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }
    
    .stTextInput>div>div>input {
        border-radius: 25px;
        border: 2px solid #E0E0E0;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #4B7BE5;
        box-shadow: 0 0 0 2px rgba(75, 123, 229, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar with extra features
st.sidebar.title("✨ Mental Health Companion")
st.sidebar.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <h3 style='color: #2E4057;'>Welcome! 🌟</h3>
        <p style='color: #666; margin: 1rem 0;'>I'm here to listen, support, and chat with you about anything that's on your mind.</p>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("### Features 🎯")
st.sidebar.markdown("""
- 🎭 Sentiment Analysis
- 💝 Personalized Responses
- 🤝 24/7 Support
- 🔒 Private Conversations
""")

if st.sidebar.button("✨ Start Fresh"):
    st.session_state.messages = []

# Add JavaScript for auto-scrolling
st.markdown("""
    <script>
        const scrollToBottom = () => {
            const messages = document.querySelector('.stChatMessageList');
            if (messages) {
                messages.scrollTop = messages.scrollHeight;
            }
        };
        
        // Create a MutationObserver to watch for changes in the chat container
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                if (mutation.addedNodes.length) {
                    scrollToBottom();
                }
            });
        });
        
        // Start observing the chat container
        const startObserver = () => {
            const messages = document.querySelector('.stChatMessageList');
            if (messages) {
                observer.observe(messages, { childList: true, subtree: true });
                scrollToBottom();
            } else {
                setTimeout(startObserver, 100);
            }
        };
        
        startObserver();
    </script>
""", unsafe_allow_html=True)

# Main UI
st.title("🌟 Mental Health Companion")
st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <p style='color: #666; font-size: 1.2rem;'>Share your thoughts and feelings with me. I'm here to listen and support you on your journey. 💫</p>
    </div>
    """, unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Add a container for better visual organization
with st.container():
    # Display chat history with enhanced styling
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(f"<div class='message-content'>{message['content']}</div>", unsafe_allow_html=True)
            if "sentiment" in message:
                st.markdown(
                    f'<div class="sentiment-wrapper"><span class="sentiment-label">{message["sentiment"]}</span></div>',
                    unsafe_allow_html=True
                )

# User input with enhanced styling
user_input = st.chat_input("✨ Share your thoughts...")

if user_input:
    # Display user message with animation
    user_message = {"role": "user", "content": f"💭 {user_input}"}
    st.session_state.messages.append(user_message)
    with st.chat_message("user"):
        st.markdown(f"<div class='message-content'>{user_message['content']}</div>", unsafe_allow_html=True)

    # Get chatbot response and sentiment with loading animation
    with st.spinner("Thinking... 🤔"):
        response, sentiment_label = get_chatbot_response(user_input)

    # Display chatbot response with enhanced styling
    chatbot_message = {"role": "assistant", "content": f"🌟 {response}", "sentiment": sentiment_label}
    st.session_state.messages.append(chatbot_message)

    with st.chat_message("assistant"):
        st.markdown(f"<div class='message-content'>{chatbot_message['content']}</div>", unsafe_allow_html=True)
        st.markdown(
            f'<div class="sentiment-wrapper"><span class="sentiment-label">{chatbot_message["sentiment"]}</span></div>',
            unsafe_allow_html=True
        )
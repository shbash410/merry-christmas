import streamlit as st
import time
import random
import os
import google.generativeai as genai
from dotenv import load_dotenv

def typewriter(text, speed=0.03, css_class="card"):
    placeholder = st.empty()
    rendered = ""
    for char in text:
        rendered += char
        placeholder.markdown(
            f"<div class='{css_class}'>{rendered}</div>",
            unsafe_allow_html=True
        )
        time.sleep(speed)


# ----------------------------
# Gemini Setup
# ----------------------------
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Anime Christmas for Miizuki 🎄",
    page_icon="🎄",
    layout="centered"
)

# ----------------------------
# CSS (Anime + Christmas)
# ----------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #0b102f, #1c245a);
}
.title {
    text-align: center;
    font-size: 58px;
    font-weight: bold;
    color: #ffe6ff;
}
.subtitle {
    text-align: center;
    font-size: 30px;
    color: #ffb7dd;
}
.card {
    background: rgba(255,255,255,0.14);
    padding: 26px;
    border-radius: 20px;
    margin-top: 20px;
    color: #ffffff;
    font-size: 20px;
    text-align: center;
    box-shadow: 0 0 22px rgba(255,180,255,0.35);
}
.footer {
    text-align: center;
    margin-top: 50px;
    font-size: 14px;
    color: #cccccc;
}

/* Snow Animation */
@keyframes snow {
  0% { transform: translateY(-10vh); opacity: 0; }
  100% { transform: translateY(110vh); opacity: 1; }
}
.snowflake {
  position: fixed;
  top: -10vh;
  color: white;
  font-size: 18px;
  animation: snow linear infinite;
  z-index: 0;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Snowflakes
# ----------------------------
for _ in range(30):
    st.markdown(
        f"<div class='snowflake' style='left:{random.randint(0,100)}%;"
        f"animation-duration:{random.randint(6,15)}s;'>❄️</div>",
        unsafe_allow_html=True
    )

# ----------------------------
# Title
# ----------------------------
st.markdown("<div class='title'>🎄 Merry Christmas 🎄</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Miizuki 🌙 | Christmas Vibe</div>", unsafe_allow_html=True)

# ----------------------------
# Typewriter Intro (Transliterated Telugu)
# ----------------------------
intro = (
    "Ee chali raatri, mellaga padutunna manchu madhyalo...\n\n"
    "Ee Christmas oka anime scene laa anipistondi.\n"
    "Aa kathalo main character nuvve, Miizuki."
)

box = st.empty()
typed = ""
for char in intro:
    typed += char
    box.markdown(f"<div class='card'>{typed}</div>", unsafe_allow_html=True)
    time.sleep(0.035)

# ----------------------------
# Gemini Message Generator (ONLY Telugu Transliteration)
# ----------------------------
st.write("")
st.markdown("<div class='card'>🌸 Anime Style Christmas Message 🌸</div>", unsafe_allow_html=True)

if st.button("✨ Generate Special Message for Miizuki"):
    prompt = """
    Write an anime-style Christmas message.

    Rules (VERY IMPORTANT):
    - Use ONLY Telugu language in English transliteration.
    - Do NOT use Telugu script.
    - Do NOT use Japanese words.
    - No emojis inside the text.
    - Tone should feel like a calm anime slice-of-life scene.
    - Soft, gentle, emotional, respectful.
    - Address the girl as Miizuki or Miizu.

    Example style:
    "Ee raatri chaala prashantamga undi. Nuvvu pakkana unte,
     prapancham koncham slow ga nadustunnattu anipistondi."

    Now generate the message.
    """
    response = model.generate_content(prompt)
    typewriter(response.text, speed=0.025)


# ----------------------------
# Anime Dialogue Mode
# ----------------------------
# st.write("")
# st.markdown("<div class='card'>🎌 Anime Dialogue Mode 🎌</div>", unsafe_allow_html=True)

# user_line = st.text_input(
#     "Miizuki dialogue (anime scene):",
#     placeholder="Ee chali raatri chaala baagundi kada..."
# )

# if user_line:
#     prompt = f"""
#     Continue this as an anime-style dialogue scene.

#     Rules:
#     - Use ONLY Telugu in English transliteration.
#     - No Telugu script.
#     - No Japanese words.
#     - Calm, emotional anime tone.
#     - Christmas night, snowfall, city lights.

#     Miizuki says:
#     "{user_line}"

#     Respond like an anime protagonist.
#     """
#     response = model.generate_content(prompt)
#     st.info(response.text)

# ----------------------------
# Anime Wishes
# ----------------------------
st.write("")
if st.button("🎁 Christmas Wish"):
    wishes = [
        "Ee Christmas, nee manasuki koncham prashanti, koncham navvu ivvali ani korukuntunna.",
        "Nee jeevitam oka slow anime episode laa mellaga andamga nadavali.",
        "Nee kallalo unde velugu ee chali raatrullo kuda thaggakudadhu.",
        "Nee rojulanni oka gentle story laa gurthundipovali."
    ]
    st.write(random.choice(wishes))

# ----------------------------
# Final Magic (Balloons)
# ----------------------------
st.write("")
if st.button("🌟 Final Moment"):
    for i in range(3, 0, -1):
        st.markdown(f"<h2 style='text-align:center;'>{i}</h2>", unsafe_allow_html=True)
        time.sleep(0.6)
    st.balloons()
    st.markdown(
        "<div class='card'>Ee Christmas nee jeevitamlo oka andamaina chapter laa nilichipovali, Miizuki. Merry Christmas once again.!</div>",
        unsafe_allow_html=True
    )

# ----------------------------
# Footer
# ----------------------------
st.markdown("<div class='footer'>Merry Christmas • Gemini Powered ✨</div>", unsafe_allow_html=True)

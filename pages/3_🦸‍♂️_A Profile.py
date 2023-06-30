from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Someone's Profile", page_icon=":student:", layout="wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("./pages/style/style.css")

# meta
lottie_anim = load_lottie("https://assets8.lottiefiles.com/packages/lf20_akpeKtNy3z.json")
img_cover1 = Image.open("./images/cover1.png")
img_squashspider = Image.open("./images/squashspider.png")

# header
with st.container():
    st.subheader("Hi, I am Peter Parker :spider:")
    st.title("A Student from New York")
    st.write("Beside helping people, I am also passionate about studying Mobile Cloud Computing in BINUS University to help publish my photos more efficient and effective for my projects.")
    st.write("[Learn More about me>](https://marvel.fandom.com/wiki/Peter_Parker_(Earth-616))")

# body 1
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            All right, let's do this one last time. My name is Peter Parker. I was bitten by a radioactive spider, and for ten years I've been the one and only Spider-Man. I'm pretty sure you know the rest. I saved a bunch of people, fell in love, saved the city, and then I saved the city again... and again and again and again.
            We don't really talk about this. Look, I'm a comic book, I'm a cereal, did a Christmas album. I have an excellent theme song. And a so-so popsicle. I mean, I've looked worse. But after everything, I still love being Spider-Man. I mean, who wouldn't? So no matter how many hits I take, I always find a way to come back. Because the only thing standing between this city and oblivion is me. There's only one Spider-Man. And you're looking at him.
            """
        )
        st.write("[Real World Projects >](https://www.marvel.com/characters/spider-man-peter-parker)")
    with right_column:
        st_lottie(lottie_anim, height=300, key="spiderman")

# body 2
with st.container():
    st.write("---")
    st.header("My Story")
    st.write("##")
    image_column, text_column = st.columns((1,2))

    with image_column:
        st.image(img_cover1)
    with text_column:
        st.subheader("Spider-Man's Legacy")
        st.write(
            """
            The FIRST issue of Amazing Spider-Man! The amazing Spider-Man swings into his very first starring series, fresh off of his debut. In one of his earliest adventures following Uncle Ben's death, Spider-Man must save a crew of astronauts aboard a malfunctioning space ship! Then, Spider-Man tries to join the Fantastic Four and then runs afoul of the Chameleon!
            """
        )
        st.markdown("[Read my story...](https://www.marvel.com/comics/issue/6482/the_amazing_spider-man_1963_1)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_squashspider)
    with text_column:
        st.subheader("Life's Report")
        st.write(
            """
            With one of the most extensive and vile rogues gallery of any super hero, Spider-Man counts among his enemies and adversaries a collection of the world’s wickedest villains.
            Wealthy Norman Osborn crossed swords with the young hero in the early days of Peter Parker’s costumed career and, decked out in his Green Goblin persona. Other villains—most notably the Hobgoblin—have also patterned their villainous identities after the Green Goblin. Doctor Otto Octavius became the dreaded Doctor Octopus when an accident merged a set of mechanical, robotic limbs to the nuclear scientist’s body and accentuated his antisocial personality. One of the wallcrawler’s first enemies, the Chameleon, used his mastery of disguise and impersonation to make Spider-Man question the identity of everyone around him. Kraven the Hunter took big game hunting to evil extremes and turned Spider-Man’s very existence into a jungle of mystery and intrigue, not to mention immense danger. The threat of Venom began when an alien parasite arrived on Earth as a replacement costume found on a far-off world by Spider-Man.
            Other formidable foes Spider-Man has faced over the years include memorable threats like the Vulture, Electro, Sandman, Rhino, Scorpion, Kingpin, Shocker, and the Lizard. While Spider-Man has managed to fend them off numerous times, they’ve all been notably resilient, returning to fight him time after time.
            """
        )
        st.markdown("[Know more about my life...](https://www.marvel.com/characters/spider-man-peter-parker/in-comics)")

# body 3
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/11frnkybryn@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name goes here" required>
        <input type="email" name="email" placeholder="And your email's here" required>
        <textarea name="message" placeholder="What's up???" required></textarea>
        <button type="submit">Send</button>
     </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Avik_Resume.pdf"
profile_pic = current_dir / "assets" / "passport.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Avik Mukherjee"
PAGE_ICON = ":wave:"
NAME = "Avik Mukherjee"
DESCRIPTION = """
Machine Learning Enthusiast, always trying to learn new things.
"""
EMAIL = "avikm744@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/avik-mukherjee-8ab9911bb/",
    "GitHub": "https://github.com/Avik-creator",
    "Twitter": "https://twitter.com/avikm744",
}
PROJECTS = {
    "🏆 News App - Made using React and NewsAPI":"https://react-news-app-cyan.vercel.app/",
    "🏆 Cyber Bullying Classification - Made a Model for Dataset":"https://github.com/Avik-creator/Machine-Learning-Projects/tree/main/Cyber%20Bullying%20Classification",
    "🏆 Brain Stroke Prediction - Made Using Different ML Models":"https://github.com/Avik-creator/Machine-Learning-Projects/tree/main/Brain%20Stroke%20Prediction",
    "🏆 Udacity AWS AI/ML Scholarship":"https://confirm.udacity.com/KKADZCPV",
    "🏆 GSSoC Contributor":"https://drive.google.com/file/d/1Q1MbmYJ9D_N_z6VAkqvAJdGjIX1SCTrE/view?usp=sharing"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Machine Learning Enthusiast.
- ✔️ Good hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks.
- ✔️ Always Eager to Learn New Things.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, 
- 📊 Data Visulization: Matplotlib, PowerBi, 
- 📚 Modeling: Logistic regression, linear regression, decition trees, SVM, NB
- 🗄️ Databases: MongoDB, MySQL
- 🎥 Video Editing Software Used: Final Cut Pro, Davinci Resolve.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Content Writing Intern | Qwerty Thoughts**")
st.write("08/2022 - 10/2022")
st.write(
    """
- ► Wrote about Many Spiritual Things.
- ► Learned about different aspects of Indian Culture.
- ► Learned about SEO and Google KeyWords.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Content Writing Intern | Framed Media**")
st.write("10/2022 - 02/2023")
st.write(
    """
- ► Learned About Technical Writing.
- ► Learned About SEO and Google KeyWords and Google Indexes.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

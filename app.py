import streamlit as st
import datetime

# --- 1. 页面配置与 Ins 简洁风样式 ---
st.set_page_config(page_title="灵魂音乐实验室", page_icon="🎧", layout="centered")

st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }
    h1 { color: #000000 !important; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; text-align: center; font-weight: 300 !important; padding-bottom: 20px; }
    .stSubheader { color: #AAAAAA !important; text-align: center; font-size: 1.0rem !important; font-weight: 300 !important; margin-bottom: 40px; }
    .stSelectbox label, .stDateInput label { color: #555555 !important; font-weight: 300 !important; }
    
    /* 按钮样式 */
    .stButton>button {
        background-color: #000000 !important; color: white !important; border-radius: 20px !important; 
        border: none !important; width: 100% !important; height: 50px !important;
        font-size: 1.1rem !important; font-weight: 300 !important; transition: background-color 0.3s ease;
    }
    .stButton>button:hover { background-color: #333333 !important; }

    /* 链接按钮样式 (一键创作) */
    .stDownloadButton>button, .stLinkButton>a {
        background-color: #000000 !important; color: white !important; border-radius: 20px !important;
        padding: 10px 20px; text-decoration: none; display: block; text-align: center; font-weight: 300;
    }

    .stInfo { background-color: #FFFFFF !important; color: #555555 !important; border: 1px solid #EEEEEE !important; border-radius: 10px; padding: 20px !important; font-size: 1rem !important; font-weight: 300 !important; }
    .stInfo b { color: #000000; font-weight: 400 !important; }
</style>
""", unsafe_allow_html=True)

# --- 2. 补全 16 种 MBTI 映射逻辑 ---
def get_music_description(mbti, birthday):
    mbti_map = {
        # 分析家
        "INTJ": "Cinematic orchestral, strategic rhythms, complex electronic pulses.",
        "INTP": "Experimental ambient, glitchy textures, complex modular synth.",
        "ENTJ": "Grand orchestral, powerful brass, driving cinematic percussion.",
        "ENTP": "Avant-garde electronic, playful rhythmic shifts, future bass.",
        # 外交家
        "INFJ": "Gentle cello, deep meditation vibes, minimalist piano.",
        "INFP": "Healing piano, ethereal ambient, dreamy Lo-fi chill.",
        "ENFJ": "Uplifting orchestra, vocal harmonies, grand and hopeful.",
        "ENFP": "Upbeat indie pop, vibrant synths, sun-drenched energy.",
        # 守护者
        "ISTJ": "Classical baroque, structured fugue, steady rhythmic pulse.",
        "ISFJ": "Warm acoustic guitar, chamber music, safe and cozy harmony.",
        "ESTJ": "Marching band precision, bold horns, structured classical.",
        "ESFJ": "Jovial pop, melodic piano, warm community vibes.",
        # 探险家
        "ISTP": "Industrial rock, gritty bass, mechanical rhythmic precision.",
        "ISFP": "Soft acoustic folk, intimate vocals, atmospheric reverb.",
        "ESTP": "High energy rock, punchy drums, bold electric guitar riffs.",
        "ESFP": "Disco pop, funky bassline, celebratory dance energy."
    }
    
    month = birthday.month
    seasons = {"Spring": [3,4,5], "Summer": [6,7,8], "Autumn": [9,10,11], "Winter": [12,1,2]}
    vibe = next((s for s, m in seasons.items() if month in m), "Special")

    base_style = mbti_map.get(mbti, "Lyrical piano")
    return f"{base_style} <b>with {vibe} vibe</b>."

# --- 3. 界面展示 ---
st.title("🎧 创造你专属的音乐吧")
st.subheader("输入性格与生日，领取属于你的灵魂 BGM 指令")

col1, col2 = st.columns(2)
with col1:
    # 完整 16 种 MBTI 列表
    mbti_list = ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP", 
                 "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"]
    user_mbti = st.selectbox("1. 你的 MBTI", mbti_list)
with col2:
    user_birth = st.date_input("2. 你的生日", datetime.date(2000, 1, 1))

st.write("")

if st.button("✨ 领取我的音乐灵魂"):
    prompt = get_music_description(user_mbti, user_birth)
    st.write("---")
    st.markdown("**你的音乐基因 (复制下方指令):**", unsafe_allow_html=True)
    st.info(prompt)
    
    st.write("")
    st.write("👇 **一键开启音乐创作**")
    # 这里链接到 Suno，这是目前最火的 AI 创作网站
    st.link_button("🚀 前往 Suno 制作完整单曲", "https://suno.com/create")
    st.caption("注：点击后在 Suno 的 'Style of Music' 框中粘贴上方指令即可。")

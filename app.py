import streamlit as st
import datetime

# --- 1. 设置 纯白简洁风 页面样式 ---
# 修改：1. 标题改为🎧 2. layout改为centered
st.set_page_config(page_title="灵魂音乐实验室", page_icon="🎧", layout="centered")

# 使用 CSS 自定义 纯白简洁配色
st.markdown("""
<style>
    /* 全局背景改为纯白 */
    .stApp {
        background-color: #FFFFFF; 
    }
    
    /* 标题样式：修改为黑色，更细的字体 */
    h1 {
        color: #000000 !important; 
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        text-align: center;
        font-weight: 300 !important; /* 修改：更细的字体 */
        padding-bottom: 20px;
    }
    
    /* 副标题样式：改为更淡的灰色 */
    .stSubheader {
        color: #AAAAAA !important;
        text-align: center;
        font-size: 1.0rem !important; /* 修改：稍微调小 */
        font-weight: 300 !important; /* 修改：更细的字体 */
        margin-bottom: 40px;
    }

    /* 下拉框和日期选择器的文字颜色：改为深灰色 */
    .stSelectbox label, .stDateInput label {
        color: #555555 !important; 
        font-weight: 300 !important; /* 修改：更细的字体 */
    }

    /* 按钮样式：改为黑色，保持圆角 */
    .stButton>button {
        background-color: #000000 !important; /* 修改：改为黑色按钮 */
        color: white !important;
        border-radius: 20px !important; 
        border: none !important;
        width: 100% !important;
        height: 50px !important;
        font-size: 1.1rem !important;
        font-weight: 300 !important; /* 修改：更细的字体 */
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #333333 !important; /* 悬停时变深灰色 */
    }

    /* 结果展示区样式：保持白色背景，灰色边框 */
    .stInfo {
        background-color: #FFFFFF !important;
        color: #555555 !important;
        border: 1px solid #EEEEEE !important; /* 修改：更淡的灰色边框 */
        border-radius: 10px;
        padding: 20px !important;
        font-size: 1rem !important;
        line-height: 1.8 !important;
        font-weight: 300 !important; /* 修改：更细的字体 */
    }
    .stInfo b {
        color: #000000; /* 结果关键词高亮黑色 */
        font-weight: 400 !important; /* 稍微加粗一点点关键词 */
    }
</style>
""", unsafe_allow_html=True)

# --- 2. 核心映射逻辑 (Prompt) ---
def get_music_description(mbti, birthday):
    mbti_map = {
        "INFP": "Healing piano, ethereal ambient, dreamy melody, Lo-fi chill.",
        "ENFP": "Upbeat indie pop, sun-drenched synths, jumpy rhythm, vibrant energy.",
        "INTJ": "Cinematic orchestral, complex electronic pulses, calm and deep.",
        "INFJ": "Gentle cello, meditation vibes, minimalism, sound of water.",
        "ENTP": "Experimental electronic, glitchy beats, curious melodies, future bass.",
        "ESTP": "Hard rock, strong bass, energetic riffs line, powerful drums.",
        "ISFJ": "Chamber music, acoustic guitar, warm and safe, classical harmony.",
        "ENFJ": "Vocal harmonies, uplifting orchestra, grand and hopeful, gospel elements."
    }
    
    month = birthday.month
    seasons = {
        "Spring": [3, 4, 5],
        "Summer": [6, 7, 8],
        "Autumn": [9, 10, 11],
        "Winter": [12, 1, 2]
    }
    
    vibe = ""
    for s_name, months in seasons.items():
        if month in months:
            vibe = f"with {s_name} vibe"
            break

    base_style = mbti_map.get(mbti, "Light music")
    return f"{base_style}; <b>{vibe}</b>."

# --- 3. 干净的界面展示 ---
# 修改：1. 标题改为 "创造你专属的音乐吧" 2. 增加🎧图标
st.title("🎧 创造你专属的音乐吧")
st.subheader("输入性格与生日，领取属于你的灵魂 BGM 指令")

# 用户选择
col1, col2 = st.columns(2)
with col1:
    # 增加更多MBTI
    mbti_input = st.selectbox("1. 你的 MBTI", ["INFP", "ENFP", "INTJ", "INFJ", "ENTP", "ESTP", "ISFJ", "ENFJ"])
with col2:
    birth_input = st.date_input("2. 你的生日", datetime.date(2000, 1, 1))

st.write("") # 加点空行

# 生成按钮
# 修改：文字改为 "✨ 领取我的音乐灵魂"
if st.button("✨ 领取我的音乐灵魂"):
    result_prompt = get_music_description(mbti_input, birth_input)
    
    st.write("---")
    
    # 干净的结果展示（客户复制这个）
    st.markdown(f"**你的音乐基因（复制此内容进行创作）:**", unsafe_allow_html=True)
    st.info(result_prompt)

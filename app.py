import streamlit as st
import datetime

# --- 1. 设置 Ins 风格页面样式 ---
st.set_page_config(page_title="灵魂音乐实验室", page_icon="💖", layout="centered")

# 使用 CSS 自定义 Ins 少女风配色 (粉色/白)
st.markdown("""
<style>
    /* 全局背景和文字颜色 */
    .stApp {
        background-color: #FFF5F7; /* 极淡的粉色背景 */
    }
    
    /* 标题样式 */
    h1 {
        color: #FF6B9B !important; /* Ins 玫瑰粉 */
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        text-align: center;
        font-weight: 300 !important;
        padding-bottom: 20px;
    }
    
    /* 副标题样式 */
    .stSubheader {
        color: #888888 !important;
        text-align: center;
        font-size: 1.1rem !important;
        font-weight: 300 !important;
        margin-bottom: 40px;
    }

    /* 下拉框和日期选择器的文字颜色 */
    .stSelectbox label, .stDateInput label {
        color: #FF85A2 !important; /* 稍淡的粉色 */
        font-weight: 400 !important;
    }

    /* 按钮样式：Ins 粉色 */
    .stButton>button {
        background-color: #FF85A2 !important;
        color: white !important;
        border-radius: 20px !important; /* 圆角按钮 */
        border: none !important;
        width: 100% !important;
        height: 50px !important;
        font-size: 1.2rem !important;
        font-weight: 400 !important;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #FF6B9B !important; /* 悬停时变深 */
    }

    /* 结果展示区样式 */
    .stInfo {
        background-color: white !important;
        color: #555555 !important;
        border: 1px solid #FFD1DC !important;
        border-radius: 10px;
        padding: 20px !important;
        font-size: 1rem !important;
        line-height: 1.8 !important;
    }
    .stInfo b {
        color: #FF6B9B; /* 结果关键词高亮粉 */
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
        # 如果需要更多MBTI，请在这里添加
    }
    
    month = birthday.month
    vibe = "Fresh Spring" if month in [3,4,5] else \
           "Sun Summer" if month in [6,7,8] else \
           "Golden Autumn" if month in [9,10,11] else \
           "Silent Winter"
    
    base_style = mbti_map.get(mbti, "Experimental electronic")
    return f"{base_style}; <b>{vibe} vibe</b>."

# --- 3. 干净的界面展示 ---
st.title("💖 你的专属 AI 音乐频率")
st.subheader("输入性格与生日，领取属于你的灵魂 BGM 指令")

# 用户选择
col1, col2 = st.columns(2)
with col1:
    mbti_input = st.selectbox("1. 你的 MBTI", ["INFP", "ENFP", "INTJ", "INFJ"])
with col2:
    birth_input = st.date_input("2. 你的生日", datetime.date(2000, 1, 1))

st.write("") # 加点空行

# 生成按钮
if st.button("✨ 领取我的音乐灵魂"):
    result_prompt = get_music_description(mbti_input, birth_input)
    
    st.write("---")
    
    # 干净的结果展示（客户复制这个）
    st.markdown(f"**你的音乐基因（复制此内容进行创作）:**", unsafe_allow_html=True)
    st.info(result_prompt)
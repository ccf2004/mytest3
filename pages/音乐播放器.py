import streamlit as st
import random

#标签页文字和图标
st.set_page_config(page_title="music",page_icon="🎵")
st.header("🎵音乐播放器")
st.text("使用streamlit制作的简单音乐播放器，支持切歌和基本播放控制")


# 初始化会话状态：记录当前播放歌曲的索引，默认从第0首开始
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

#音乐列表
music=[
    {
        'url':"http://p2.music.126.net/EDhgL1S2DLGVE_5cjU-hfQ==/109951172410328709.jpg?param=130y130",
        'audio_url':'https://music.163.com/song/media/outer/url?id=3327141886.mp3',
        'text':'大东北我的家乡',
        'time':'04分43秒',
        'author':'袁娅维TIA RAY'

        },{
        'url':"http://p1.music.126.net/RiyVemaQPh2coRH0EAlpyQ==/109951172360400179.jpg?param=130y130",
        'audio_url':'https://music.163.com/song/media/outer/url?id=3323077522.mp3',
        'text':'爱情的索嗨',
        'time':'04分43秒',
        'author':'广东烂仔Zaage炸鸡 / 广东说唱王'

        },{
       'url':"http://p1.music.126.net/RFbUrR2x2JEMB0WGYvwVQg==/109951169642392307.jpg?param=130y130",
       'audio_url':'https://music.163.com/song/media/outer/url?id=2161991028.mp3',
        'text':'江南雪',
        'time':'03分56秒',
        'author':'礼越'

        }
    ]



c1,c2 =st.columns([1,2])
# 下一张
def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1)%len(music)
# 上一张
def lastImg():
    st.session_state['ind']=(st.session_state['ind']-1)%len(music)
# 随机播放：切换到非当前索引的随机歌曲
def random_play():
    """随机播放：切换到非当前索引的随机歌曲"""
    current_ind = st.session_state['ind']
    random_ind = current_ind
    # 确保随机索引≠当前索引，避免重复播放同一首
    while random_ind == current_ind:
        random_ind = random.randint(0, len(music)-1)
    st.session_state['ind'] = random_ind
# 直接将当前索引设为点击的歌曲索引
def play_index(idx):
    st.session_state['ind'] = idx  

# 分两列展示
with c1:
    st.image(music[st.session_state['ind']]['url'],caption='专辑封面',width=160)

with c2:
    st.subheader(music[st.session_state['ind']]['text'])
    st.text('歌手:' + music[st.session_state['ind']]['author'])
    st.text('时间:' + music[st.session_state['ind']]['time'])
    # 控制按钮分三列：上一首、随机播放、下一首
    c3,c4,c5 =st.columns(3)
    with c3:
        st.button("⏮上一首",on_click=lastImg,use_container_width=True)
    with c4:
        st.button("🔀随机播放", on_click=random_play, use_container_width=True)
    with c5:
        st.button("⏭下一首",on_click=nextImg,use_container_width=True)



# 音频播放组件
st.audio(music[st.session_state['ind']]['audio_url'])

# 歌曲列表
# 分割线
st.divider() 
st.subheader("📜 歌曲列表")
for idx, song in enumerate(music):
    # 统一格式化按钮文字，无多余空格
    if idx == st.session_state['ind']:
        song_name = f"正在播放：{song['text']} - {song['author']}"
    else:
        song_name = f"{song['text']} - {song['author']}"
    
    # 生成按钮
    st.button(
        song_name,
        on_click=play_index,
        args=(idx,),
        use_container_width=True,
        key=f"song_btn_{idx}"
    )

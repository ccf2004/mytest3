import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime
import base64
from PIL import Image
import io

# 全局页面配置（只设置一次，避免重复）
st.set_page_config(page_title="综合信息面板", page_icon="📋", layout="wide")

st.title("综合信息管理面板")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🔍 数字档案", 
    "🍜 南宁美食数据", 
    "🖼 我的相册", 
    "🎶 音乐播放器", 
    "📺 视频播放", 
    "📄 简历生成器"
])

# 增加分割线
st.markdown("---")

with tab1:
    st.title('🔑基础信息')
    st.header('学生ID:NEO-2022-001')
    # 显示注册时间、精神状态
    st.subheader('注册时间: :green[2022-10-01 08:30:17] |精神状态: :green[正常]')
    # 显示当前教室、安全等级
    st.subheader('当前教室: :green[实训楼108]安全等级: :green[绝密]')
    # 技能矩阵区域
    st.markdown('# 📊技能矩阵')
    # 定义列布局，分成3列
    c1, c2, c3 = st.columns(3)
    c1.metric(label="c语言", help='这是工具提示', value="95%", delta="2%")
    c2.metric(label="Pyhon", value="87%", delta="-1%")
    c3.metric(label="Java", help='这是工具提示', value="68%", delta="-10%")

    # Streamlit课程进度区域
    st.subheader("Steamlit课程进度")
    st.progress(60)

    st.markdown('# 📝任务日志')
    # 定义数据,以便创建数据框
    data = {
        '日期': ['2023-10-01', '2023-10-05', '2023-10-12'],
        '任务': ['学生数字档案', '课程管理系统', '数据图表展示'],
        '状态': ['✅完成', '⚪进行中', '❌未完成'],
        '难度': ['⭐⭐⛤⛤⛤', '⭐⛤⛤⛤⛤', '⭐⭐⭐⛤⛤']
    }
    # 显示数据框
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    
    st.markdown('# 🔐最新代码成果')
    python_code = '''def matrix_breach():
    while True:
           if detect_vulnerability():
               exploit()
               return "ACCESS GRANTED"
           else:
               stealth_evade()
    '''
    # 添加 st.code() 展示代码，指定语言为 python
    st.code(python_code, language='python')

    # 分割线
    st.markdown('***')
    st.markdown('>> SYSTEM MESSAGE: 下一个任务目标已解锁...')
    st.markdown('>> TARGET: 课程管理系统')
    st.markdown('>> COORDINATE: 2025-05-13 01:24:58')
    st.markdown('系统状态：在线 连接状态：已加密')


with tab2:
    st.title("🥢南宁美食探索")
    st.text("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")

    st.header("📍南宁美食地图")
    # 地图数据
    map_data = {
        "latitude": [22.853966, 22.810761, 22.845768, 22.790446, 23.202054, 22.838009],
        "longitude": [108.222561, 108.401252, 108.301052, 108.312107, 108.182322, 108.268402]
    }
    mp_df = pd.DataFrame(map_data)
    st.map(mp_df)
    
    st.header("⭐餐厅评分")
    # 餐厅数据
    restaurants_data = {
        "餐厅": ["北方土菜馆", "肯德基(盛天地店)", "兰州拉面(秀隆店)", "三品王(江南万达店)", "塔斯汀(武鸣大帽路店)", "正宗南宁老友粉"],
        "类型": ["自助餐", "西餐", "中餐", "中餐", "快餐", "中餐"],
        "评分": [4.2, 3.2, 4.6, 2.7, 3.8, 5.0],
        "人均消费(元)": [50, 20, 15, 20, 10, 10],
        "latitude": [22.853966, 22.810761, 22.845768, 22.790446, 23.202054, 22.838009],
        "longitude": [108.222561, 108.401252, 108.301052, 108.312107, 108.182322, 108.268402]
    }
    # 定义数据框所用的新索引
    index = pd.Series([1, 2, 3, 4, 5, 6], name='序号')
    # 根据上面创建的data，创建数据框
    df = pd.DataFrame(restaurants_data, index=index)

    # 条形图
    st.bar_chart(df.set_index('餐厅')['评分'])

    st.header("💰不同类型餐厅价格")
    different_data = {
        "类型": ["自助餐", "西餐", "中餐", "中餐", "快餐", "中餐"],
        "价格": [70, 100, 50, 20, 16, 120]
    }
    # 根据上面创建的different_data，创建数据框
    df = pd.DataFrame(different_data)
    # 通过x指定类型所在这一列为折线图的x轴
    st.line_chart(df, x='类型')

    st.header("💰不同餐厅12月价格走势")
    price_data = {
        '月份': ['01月', '02月', '03月', '04月', '05月', '06月', '07月', '08月', '09月', '10月', '11月', '12月'],
        '北方土菜馆(人均)': [85, 82, 80, 78, 83, 86, 88, 90, 85, 87, 92, 95],
        '肯德基(盛天地店)(人均)': [45, 43, 42, 40, 42, 44, 45, 46, 44, 43, 45, 48],
        '兰州拉面(秀隆店)(单碗)': [18, 18, 19, 19, 20, 20, 21, 21, 20, 20, 21, 22],
        '三品王(江南万达店)(单碗)': [16, 16, 17, 17, 18, 18, 19, 19, 18, 18, 19, 20],
        '塔斯汀(武鸣大帽路店)(单人餐)': [25, 24, 23, 22, 24, 25, 26, 26, 25, 24, 26, 28],
        '正宗南宁老友粉(单碗)': [15, 15, 16, 16, 17, 17, 18, 18, 17, 17, 18, 19]
    }
    # 根据上面创建的price_data，创建数据框
    df = pd.DataFrame(price_data)
    # 通过x指定月份所在这一列为折线图的x轴
    st.line_chart(df, x='月份')

    st.header("🕛用餐高峰时段")
    # 餐厅数据
    time_data = {
        '时间': ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00'],
        '北方土菜馆': [10, 15, 20, 50, 180, 150, 60, 30, 40, 80, 200, 180, 120, 70, 40, 20, 10],
        '肯德基(盛天地店)': [60, 70, 80, 100, 160, 140, 90, 80, 90, 110, 180, 160, 130, 110, 90, 70, 50],
        '兰州拉面(秀隆店)': [50, 60, 50, 80, 150, 120, 60, 40, 50, 70, 120, 90, 60, 40, 30, 20, 10],
        '三品王(江南万达店)': [100, 120, 80, 90, 140, 100, 50, 30, 40, 60, 80, 60, 40, 30, 20, 10, 5],
        '塔斯汀(武鸣大帽路店)': [20, 25, 30, 80, 160, 120, 70, 90, 80, 100, 200, 170, 110, 80, 60, 40, 20],
        '正宗南宁老友粉': [150, 180, 100, 70, 120, 80, 40, 20, 30, 50, 70, 50, 30, 20, 10, 5, 0]
    }
    # 根据上面创建的time_data，创建数据框
    df = pd.DataFrame(time_data)
    # 通过x指定时间所在这一列为面积图的x轴
    st.line_chart(df, x='时间')


with tab3:
    st.title("我的相册")
    # 初始化图片索引ind，默认显示第0张图片
    if 'ind_album' not in st.session_state:  # 重命名索引避免和其他标签冲突
        st.session_state['ind_album'] = 0

    images = [
        {
            'url': "https://ts4.tc.mm.bing.net/th/id/OIP-C.F15Td8baE_F5y4UzxGppDwHaE7?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3",
            'text': '猫'
        },
        {
            'url': "https://img.pconline.com.cn/images/upload/upc/tx/itbbs/1406/16/c18/35339323_1402908540795.jpg",
            'text': '猴子'
        },
        {
            'url': "https://ts1.tc.mm.bing.net/th/id/OIP-C._ITStaPCyDNy4feFPGQxWgHaFG?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3",
            'text': '兔子'
        }
    ]
            
    # 显示当前图片
    st.image(images[st.session_state['ind_album']]['url'], caption=images[st.session_state['ind_album']]['text'])

    # 下一张
    def nextImg_album():
        st.session_state['ind_album'] = (st.session_state['ind_album'] + 1) % len(images)
    
    # 上一张
    def lastImg_album():
        st.session_state['ind_album'] = (st.session_state['ind_album'] - 1) % len(images)

    c1, c2 = st.columns(2)
    with c1:
        st.button("上一张", on_click=lastImg_album, use_container_width=True)
    with c2:
        st.button("下一张", on_click=nextImg_album, use_container_width=True)


with tab4:
    st.header("🎵音乐播放器")
    st.text("使用streamlit制作的简单音乐播放器，支持切歌和基本播放控制")

    # 初始化会话状态：记录当前播放歌曲的索引（重命名避免冲突）
    if 'ind_music' not in st.session_state:
        st.session_state['ind_music'] = 0

    # 音乐列表
    music = [
        {
            'url': "http://p2.music.126.net/EDhgL1S2DLGVE_5cjU-hfQ==/109951172410328709.jpg?param=130y130",
            'audio_url': 'https://music.163.com/song/media/outer/url?id=3327141886.mp3',
            'text': '大东北我的家乡',
            'time': '04分43秒',
            'author': '袁娅维TIA RAY'
        },
        {
            'url': "http://p1.music.126.net/RiyVemaQPh2coRH0EAlpyQ==/109951172360400179.jpg?param=130y130",
            'audio_url': 'https://music.163.com/song/media/outer/url?id=3323077522.mp3',
            'text': '爱情的索嗨',
            'time': '04分43秒',
            'author': '广东烂仔Zaage炸鸡 / 广东说唱王'
        },
        {
            'url': "http://p1.music.126.net/RFbUrR2x2JEMB0WGYvwVQg==/109951169642392307.jpg?param=130y130",
            'audio_url': 'https://music.163.com/song/media/outer/url?id=2161991028.mp3',
            'text': '江南雪',
            'time': '03分56秒',
            'author': '礼越'
        }
    ]

    c1, c2 = st.columns([1, 2])
    
    # 下一张
    def nextImg_music():
        st.session_state['ind_music'] = (st.session_state['ind_music'] + 1) % len(music)
    
    # 上一张
    def lastImg_music():
        st.session_state['ind_music'] = (st.session_state['ind_music'] - 1) % len(music)
    
    # 随机播放：切换到非当前索引的随机歌曲
    def random_play():
        current_ind = st.session_state['ind_music']
        random_ind = current_ind
        # 确保随机索引≠当前索引，避免重复播放同一首
        while random_ind == current_ind:
            random_ind = random.randint(0, len(music)-1)
        st.session_state['ind_music'] = random_ind
    
    # 直接将当前索引设为点击的歌曲索引
    def play_index(idx):
        st.session_state['ind_music'] = idx  

    # 分两列展示
    with c1:
        st.image(music[st.session_state['ind_music']]['url'], caption='专辑封面', width=160)

    with c2:
        st.subheader(music[st.session_state['ind_music']]['text'])
        st.text('歌手:' + music[st.session_state['ind_music']]['author'])
        st.text('时间:' + music[st.session_state['ind_music']]['time'])
        # 控制按钮分三列：上一首、随机播放、下一首
        c3, c4, c5 = st.columns(3)
        with c3:
            st.button("⏮上一首", on_click=lastImg_music, use_container_width=True)
        with c4:
            st.button("🔀随机播放", on_click=random_play, use_container_width=True)
        with c5:
            st.button("⏭下一首", on_click=nextImg_music, use_container_width=True)

    # 音频播放组件
    st.audio(music[st.session_state['ind_music']]['audio_url'])

    # 歌曲列表
    # 分割线
    st.divider() 
    st.subheader("📜 歌曲列表")
    for idx, song in enumerate(music):
        # 统一格式化按钮文字，无多余空格
        if idx == st.session_state['ind_music']:
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


with tab5:
    st.title("喜狼狼与灰太狼")

    # 剧集信息
    video_arr = [
        {
            'url': "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/34/99/33748159934/33748159934-1-192.mp4?e=ig8euxZM2rNcNbRVhbdVhwdlhWdghwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&platform=html5&og=hw&deadline=1765772890&oi=144233936&mid=0&trid=21d9f02809354c68b00dbc42e2cd608h&gen=playurlv3&os=estghw&nbs=1&upsig=961262b97ec3bb13c1cb08b44b8bac67&uparams=e,uipk,platform,og,deadline,oi,mid,trid,gen,os,nbs&bvc=vod&nettype=0&bw=818414&buvid=&build=0&dl=0&f=h_0_0&agrr=0&orderid=0,1",
            'title': '第1集',
            'description': '本集讲述了喜羊羊和伙伴们如何巧妙地应对灰太狼的新陷阱。'
        },
        {
            'url': "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/46/22/33748222246/33748222246-1-192.mp4?e=ig8euxZM2rNcNbRV7wdVhwdlhWdMhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&mid=0&oi=1385955528&trid=74f55deadc5e49708f7fc12dc690a82h&deadline=1765773018&og=cos&platform=html5&gen=playurlv3&os=estgcos&nbs=1&upsig=5787679f7fa43c7b8bfbe9845b369479&uparams=e,uipk,mid,oi,trid,deadline,og,platform,gen,os,nbs&bvc=vod&nettype=0&bw=834844&agrr=0&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1",
            'title': '第2集',
            'description': '灰太狼使用高科技武器捕捉小羊，引发一系列爆笑场面。'
        },
        {
            'url': "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/36/31/33748223136/33748223136-1-192.mp4?e=ig8euxZM2rNcNbRV7bdVhwdlhWdjhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&os=estgcos&og=cos&nbs=1&uipk=5&trid=ce460698b3914a03accdf43fd2abf2fh&mid=0&gen=playurlv3&oi=144233936&deadline=1765773046&platform=html5&upsig=cfc9dad0554a5ddf341f8b3aebd32281&uparams=e,os,og,nbs,uipk,trid,mid,gen,oi,deadline,platform&bvc=vod&nettype=0&bw=851606&buvid=&build=0&dl=0&f=h_0_0&agrr=0&orderid=0,1",
            'title': '第3集',
            'description': '懒羊羊意外获得超能力，却在使用中闹出不少笑话。'
        },
        {
            'url': "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/71/41/33748224171/33748224171-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&deadline=1765773081&uipk=5&platform=html5&gen=playurlv3&og=cos&nbs=1&trid=21ce35d75d58476aa94c726d9714235h&oi=2067284620&os=estgoss&upsig=1f01753f00d22aad7e7af8457e348a5c&uparams=e,mid,deadline,uipk,platform,gen,og,nbs,trid,oi,os&bvc=vod&nettype=0&bw=792995&agrr=0&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1",
            'title': '第4集',
            'description': '美羊羊举办选美大赛，引发草原上的热潮。'
        },
        {
            'url': "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/66/52/33748225266/33748225266-1-192.mp4?e=ig8euxZM2rNcNbRV7zdVhwdlhWdahwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=144233936&gen=playurlv3&os=estgcos&og=hw&nbs=1&mid=0&deadline=1765773110&uipk=5&platform=html5&trid=6818dfb385eb44f79daf697f1352360h&upsig=52b3c82e13c60dd94a98bdb0b1e00ab9&uparams=e,oi,gen,os,og,nbs,mid,deadline,uipk,platform,trid&bvc=vod&nettype=0&bw=857360&f=h_0_0&agrr=0&buvid=&build=0&dl=0&orderid=0,1",
            'title': '第5集',
            'description': '灰太狼假扮成老师混入学校，企图抓住小羊们。'
        }
    ]

    # 演职人员信息
    cast_info = [
        {
            'name': '喜羊羊',
            'role': '主角',
            'description': '聪明机智的领头羊，总能带领大家化解危机。'
        },
        {
            'name': '美羊羊',
            'role': '时尚达人',
            'description': '热爱美丽与时尚，擅长烹饪和手工制作。'
        },
        {
            'name': '懒羊羊',
            'role': '吃货',
            'description': '贪吃但善良，关键时刻总能发挥重要作用。'
        },
        {
            'name': '灰太狼',
            'role': '反派',
            'description': '坚持不懈抓羊的狼，虽然失败但充满喜感。'
        },
        {
            'name': '红太狼',
            'role': '灰太狼妻子',
            'description': '性格火爆，经常用平底锅教训灰太狼。'
        }
    ]

    # 初始化会话状态,默认从第一集开始（重命名避免冲突）
    if 'ind_video' not in st.session_state:
        st.session_state['ind_video'] = 0
        
    # 当前播放信息
    st.subheader(f"正在播放：{video_arr[st.session_state['ind_video']]['title']}")
    st.video(video_arr[st.session_state['ind_video']]['url'], autoplay=True)

    # 剧集介绍
    st.markdown("### 🎬 剧集介绍")
    st.write(video_arr[st.session_state['ind_video']]['description'])

    # 集数选择区域标题
    st.markdown("---")
    st.subheader("选择集数")

    def play_video(i):
        st.session_state['ind_video'] = int(i)

    # 每行显示3个按钮
    cols = st.columns(3)
    for i in range(len(video_arr)):
        col_index = i % 3  # 计算列索引
        with cols[col_index]:
            st.button('第' + str(i + 1) + '集', use_container_width=True, on_click=play_video, args=(i,))

    # 演职人员展示（移动到视频下方并移除图片）
    st.markdown("---")
    st.markdown("### 👥 演职人员")
    # 使用columns布局展示演职人员信息
    cast_cols = st.columns(len(cast_info))
    for i, person in enumerate(cast_info):
        with cast_cols[i]:
            # 只显示姓名、角色和描述，不显示图片
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <h4>{person['name']}</h4>
                    <p style="font-size: 0.9em; color: #666;">{person['role']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            # 描述信息
            st.write(person['description'])

    # 底部信息
    st.markdown("---")
    st.info("💡 提示：点击任意集数按钮即可切换播放内容")


with tab6:
    st.title("📝 个人简历生成器")
    st.markdown('<p style="font-size:1.2rem;">使用Streamlit创建您的个性化简历</p>', unsafe_allow_html=True)

    # 左右分栏（左侧表单，右侧预览）
    c1, c2 = st.columns([1, 2])

    with c1:
        # 左侧：个人信息表单 - 基础信息分区
        st.header("基础信息")
        
        # 证件照上传
        uploaded_file = st.file_uploader("上传证件照", type=["jpg", "jpeg", "png"])
        
        # 基础信息
        name = st.text_input('姓名', autocomplete='name')
        # 性别（水平单选）
        xb = st.radio(
            '性别',
            ['男', '女', '其他'],
            horizontal=True
        )
        
        zw = st.text_input('职位', autocomplete='job-title')
        phone = st.text_input("联系电话", placeholder="请输入11位手机号")
        email = st.text_input('邮箱', autocomplete='email')
        date = st.date_input("出生日期", value=None)
        
        # 学历（下拉选择）
        xl = st.selectbox(
            '学历',
            ['高中', '专科', '本科','硕士','博士']
        )
        # 工作经验（滑块）
        gzjy = st.slider('工作经验（年）', 0, 30, 0)
        
        # 技能分区
        st.header("技能信息")
        # 技能（多选）
        jn = st.multiselect(
            '技能（可多选）',
            ['Python', 'Java', 'JavaScript', 'HTML/CSS', 'SQL', '数据分析','机器学习','深度学习','UI/UX设计']
        )
        # 语言能力（多选）
        yynl = st.multiselect(
            '语言能力',
            ['中文', '英语', '日语', '法语', '德语', '西班牙语']
        )
        # 期望薪资（范围滑块）
        qwxz = st.slider(
            '期望薪资范围（元）',
            5000, 50000, (10244, 20000)
        )
        # 教育背景分区
        st.header("教育背景")
        # 教育背景输入
        school = st.text_input("毕业院校")
        major = st.text_input("专业")
        edu_date = st.text_input("在校时间", placeholder="例如：2018.09 - 2022.06")
        gpa = st.text_input("GPA/成绩", placeholder="例如：3.8/4.0 或 专业前10%")
        
        # 个人简介（文本域）
        grjj = st.text_area(
            label='个人简介',
            placeholder='请简要介绍您的专业背景、职业目标和个人特点...',
            value='这个人很神秘，没有留下任何介绍...',
            height=200,
            max_chars=200
        )

    with c2:
        # 右侧：简历实时预览
        st.header("📄 简历实时预览")
        
        # 显示照片和姓名在同一行
        photo_col, name_col = st.columns([1, 3])
        
        with photo_col:
            if uploaded_file is not None:
                # 显示上传的照片
                st.image(uploaded_file, width=100, caption="")
            else:
                # 显示默认占位图
                st.image("https://cdn-icons-png.flaticon.com/512/847/847969.png", width=100, caption="")
        
        with name_col:
            st.title(name if name else "姓名")
        
        st.markdown("---")
        
        # 预览区分左右两栏（左：基础信息，右：补充信息）
        preview_col1, preview_col2 = st.columns([2, 1])  
        
        with preview_col1:
            # 左栏：基础信息
            st.subheader("📋 基本信息")
            st.text(f"💼 职位：{zw if zw else '未填写'}")
            st.text(f"📞 电话：{phone if phone else '未填写'}")
            st.text(f"📧 邮箱：{email if email else '未填写'}")
            st.text(f"🎂 出生日期：{date.strftime('%Y-%m-%d') if date else '未填写'}")
            st.text(f"🚻 性别：{xb}")
        
        with preview_col2:
            # 右栏：补充信息
            st.subheader("📊 其他信息")
            st.text(f"🎓 学历：{xl}")
            st.text(f"🌐 语言能力：{', '.join(yynl) if yynl else '无'}")
            st.text(f"🔧 技能：{', '.join(jn) if jn else '无'}")
            st.text(f"📊 工作经验：{gzjy}年")
            st.text(f"💰 期望薪资：{qwxz[0]} - {qwxz[1]}元")
        
        # 教育背景预览
        st.subheader("📚 教育背景")
        st.markdown("---")
        if school or major or edu_date or gpa:
            st.text(f"🏫 院校：{school if school else '未填写'}")
            st.text(f"📖 专业：{major if major else '未填写'}")
            st.text(f"📅 时间：{edu_date if edu_date else '未填写'}")
            st.text(f"📈 成绩：{gpa if gpa else '未填写'}")
        else:
            st.text("暂无教育背景信息")
        
        # 个人简介模块
        st.subheader("📝 个人简介")
        st.markdown("---")
        st.text(grjj)

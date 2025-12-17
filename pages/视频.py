import streamlit as st

# 标签页文字和图标
st.set_page_config(page_title="影视", page_icon="🎬")
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

# 初始化会话状态,默认从第一集开始
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0
    
# 当前播放信息
st.subheader(f"正在播放：{video_arr[st.session_state['ind']]['title']}")
st.video(video_arr[st.session_state['ind']]['url'], autoplay=True)

# 剧集介绍
st.markdown("### 🎬 剧集介绍")
st.write(video_arr[st.session_state['ind']]['description'])

# 集数选择区域标题
st.markdown("---")
st.subheader("选择集数")

def play(i):
    st.session_state['ind'] = int(i)

# 每行显示3个按钮
cols = st.columns(3)
for i in range(len(video_arr)):
    col_index = i % 3  # 计算列索引
    with cols[col_index]:
        st.button('第' + str(i + 1) + '集', use_container_width=True, on_click=play, args=(i,))

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

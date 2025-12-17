import streamlit as st

#标签页文字和图标
st.set_page_config(page_title="相册",page_icon="🦜")

st.title("我的鹦鹉")

if'ind' not in st.session_state:
    st.session_state['ind']=0

#图片以及名称
images=[
    {
        'url':"https://miaobi-lite.bj.bcebos.com/miaobi/5mao/b%276bmm6bmJ6bifXzE3MzQ1NDY3NDYuMTc4NDU5Mg%3D%3D%27/0.png",
        'text':'玫瑰鹦鹉'

        },{
        'url':"https://miaobi-lite.bj.bcebos.com/miaobi/5mao/b%276bmm6bmJ56eN57G7XzE3MzUwNjMzMDQuMTE3Njg5Ng%3D%3D%27/0.png",
        'text':'绿翅金刚鹦鹉'

        },{
        'url':"https://img0.baidu.com/it/u=2110929142,2997516617&fm=253&fmt=auto&app=120&f=JPEG?w=682&h=1023",
        'text':'美冠鹦鹉'

        }
    ]

st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['text'])

#按钮函数
def nextImg():
    st.session_state['ind']=(st.session_state['ind']+1)%len(images)

#分列容器
c1,c2=st.columns(2)
    
#按钮
with c1:
    st.button("上一张",on_click=nextImg,use_container_width=True)

with c2:
    st.button("下一张",on_click=nextImg,use_container_width=True)

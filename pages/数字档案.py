import streamlit as st
import pandas as pd


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
c1.metric(label="c语言",help='这是工具提示',value="95%", delta="2%")
c2.metric(label="Pyhon", value="87%", delta="-1%")
c3.metric(label="Java",help='这是工具提示',value="68%", delta="-10%")

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
#  显示数据框
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

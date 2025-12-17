import streamlit as st
from datetime import datetime
import base64
from PIL import Image
import io

# 页面配置
st.set_page_config(page_title="个人简历生成器", page_icon="📝", layout="wide")

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
    
   
    #学历（下拉选择）
    xl = st.selectbox(
        '学历',
        ['高中', '专科', '本科','硕士','博士']
    )
    #工作经验（滑块）
    gzjy = st.slider('工作经验（年）', 0, 30, 0)
    
    # 技能分区
    st.header("技能信息")
    # 技能（多选）
    jn = st.multiselect(
        '技能（可多选）',
        ['Python', 'Java', 'JavaScript', 'HTML/CSS', 'SQL', '数据分析','机器学习','深度学习','UI/UX设计']
    )
    #语言能力（多选）
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

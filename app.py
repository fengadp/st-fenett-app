import os
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_pdf_viewer import pdf_viewer
# for python 3.10 correct [from typing_extensions import TypedDict, List, NotRequired] line 3 in st_env/Lib/site-packages/streamlit_carousel/__init__.py
#from streamlit_carousel import carousel

hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.image('./asset/logo.png')
st.title("The 11th National Food Engineering Conference :red[_Febuary 13-14, 2025_]")
#st.subheader('host by')
st.title(":green[Kasetsart University Kamphaeang Saen Campus]")
st.image('./asset/background.webp')

tabs = st.tabs(["หน้าแรก", "ลงทะเบียน", "ส่งบทความ", "ดาวน์โหลดเอกสาร"])

tabs[0].title(":green[Transforming Thailand’s Food Industry:] :red[_AI-Powered Solutions_]")
tabs[0].markdown("ประเทศไทยมีความอุดมสมบูรณ์ด้านทรัพยากรอาหาร มีอุตสาหกรรมแปรรูปอาหารจำนวนมาก งานวิจัย นวัตกรรม และเทคโนโลยีใหม่ ๆ ในด้านวิศวกรรมอาหารจะช่วยส่งเสริมให้เกิดการพัฒนาอุตสาหกรรมอาหารของประเทศ การประยุกต์ปัญญาประดิษฐ์ (Artificial Intelligence) เพื่อช่วยวิเคราะห์และประเมินผลข้อมูลกระบวนการผลิตอาหารสามารถเพิ่มประสิทธิภาพการทำงานในด้านต่าง ๆ ทำให้ระบบการผลิตใช้ทรัพยากรอย่างคุ้มค่า ประหยัดเวลา ใช้แรงงานน้อยลง เป็นกระบวนการผลิตที่มีความแม่นยำ น่าเชื่อถือ และปลอดภัย ทำให้เกิดการผลิตสินค้าและบริการที่ตอบสนองความต้องการของผู้บริโภคที่แตกต่างกัน")
tabs[0].markdown("วิศวกรรมอาหารเป็นสาขาวิชาทางวิศวกรรมที่บูรณาการความรู้ทางวิศวกรรมและวิทยาศาสตร์ร่วมกัน เพื่อใช้ในการพัฒนาเครื่องจักรผลิตอาหาร กระบวนการผลิตอาหาร และบริหารจัดการผลิตอาหาร โดยคำนึงถึงความปลอดภัยต่อผู้บริโภค และผลกระทบต่อสิ่งแวดล้อม วิศวกรรมอาหารจึงมีบทบาทสำคัญต่อการพัฒนาอุตสาหกรรมอาหาร และช่วยให้อุตสาหกรรมอาหารไทยมีการพัฒนาอย่างเข้มแข็งต่อเนื่องและสามารถแข่งขันได้ในระดับนานาชาติ")

tabs[0].header(':blue[หัวข้อการประชุม]')
tabs[0].markdown("หัวข้อการประชุมจะครอบคลุมงานวิจัยและนวัตกรรมทางวิศวกรรม วิทยาศาสตร์ และเทคโนโลยี ที่เกี่ยวข้องกับอุตสาหกรรมอาหารและสาขาอื่น ๆ ที่เกี่ยว โดยการประชุมครั้งนี้ส่งเสริมให้นำเสนอผลงานดังหัวข้อต่อไปนี้")
tabs[0].markdown(":balloon: Food Machinery")
tabs[0].markdown(":balloon: Food Processing Technology")
tabs[0].markdown(":balloon: Robotics and Automation in Food Processing")
#tabs[0].markdown(":balloon: Food Quality Control and Evaluation")
#tabs[0].markdown(":balloon: Food Safety and Supply Chain Management")
tabs[0].markdown(":balloon: Artificial Intelligence and Big Data Analytics in Food Industry")
tabs[0].markdown(":balloon: Related Topics in Food and Engineering Technology")

tabs[0].header(':blue[กำหนดการประชุมวิชาการ]')
with tabs[0].container(border=True):
    page_number = st.number_input(label='', min_value=1, max_value=3, label_visibility="collapsed", key='input_page_number')
    pdf_viewer('./documents/กำหนดการประชุมวิชาการวิศวกรรมอาหารแห่งชาติ ครั้งที่ 11.pdf', pages_to_render=[page_number])

#options = ['page 1', 'page 2', 'page 3']
#opt = st.selectbox("", options, label_visibility="collapsed", key='select_info')
#selected_index = options.index(opt)
#st.write(selected_index)
#if opt is not None:
#    with st.container(border=True):
#        pdf_viewer('./documents/กำหนดการ.pdf', pages_to_render=[selected_index + 1])

def display_map(location_data):
    fig = px.scatter_mapbox(location_data, lat='latitude', lon='longitude', hover_name='location', zoom=10)
    fig.update_layout(mapbox_style='open-street-map')
    return fig

cols_2 = tabs[0].columns(2)
cols_2[0].subheader('การจองห้องพัก')
cols_2[0].markdown('หอพักนานาชาติ (ภายในมหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตกำแพงแสน)')
cols_2[0].markdown(':blue[:phone: 034-355593]')
#cols_2[0].markdown(':blue[:phone: 034-355585-92]')
cols_2[0].markdown('แสนปาล์ม เทรนนิ่ง โฮม (ภายนอกมหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตกำแพงแสน)')
cols_2[0].markdown(':blue[:phone: 034-355166, 092-2495861, 092-2495285]')

# Create the pandas DataFrame for map locations
data = {'location': ['หอพักนานาชาติ', 'แสนปาล์ม เทรนนิ่ง โฮม'],
        'latitude': [14.01582, 14.00752],
        'longitude': [99.98053, 99.96962]}
        #'mark_size': [5, 5, 5]}
        #'mark_color': ['rgb(255, 0, 0)', 'rgb(0, 0, 255)', 'rgb(0, 255, 0)']}
df = pd.DataFrame(data)
px_map = display_map(df)
cols_2[0].plotly_chart(px_map, use_container_width=True)

cols_2[1].subheader('สอบถามข้อมูลเพิ่มเติม')
cols_2[1].markdown("คุณวริศรา สมตน เจ้าหน้าที่ประสานงานประชุมวิชาการฯ")
cols_2[1].markdown("ภาควิชาวิศวกรรมการอาหาร คณะวิศวกรรมศาสตร์ กำแพงแสน มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตกำแพงแสน")
cols_2[1].markdown("1 หมู่ 6 ถ.มาลัยแมน ต.กำแพงแสน อ.กำแพงแสน จ.นครปฐม 73140")
cols_2[1].markdown(":phone: 080-823-5072 :email: fengwaso@ku.ac.th")
cols_2[1].image('./asset/QR_Web.svg', width=150, caption="https://fenett-2025.streamlit.app")

tabs[0].write('')
tabs[0].subheader('ผู้สนับสนุนการประชุมวิชาการ')
cols_3 = tabs[0].columns(2)
cols_3[0].image('./asset/S1.jpg')
cols_3[1].image('./asset/S2.jpg')

#tabs[0].divider()

#tabs[0].header(':blue[บรรยากาศงานประชุมวิชาการวิศวกรรมอาหารแห่งชาติ ครั้งที่ 6]')
#with tabs[0].container(border=True):
#    image_index = tabs[0].slider(":blue[รูปภาพกิจกรรม]", 1, 12, 1,)
#    image_file = './photos/photo' + str(image_index) + '.jpg'
#    tabs[0].image(image_file)

#tabs[0].header(':blue[บทความประชุมวิชาการฉบับสมบูรณ์]')
#with tabs[0].container(border=True):
#    page_number = st.number_input(label='', min_value=1, label_visibility="collapsed", key='input_page_number')
#    pdf_viewer('./documents/บทความประชุมวิชาการฉบับสมบูรณ์.pdf', pages_to_render=[page_number])

#st.header(':blue[การประเมินบทความทางวิชาการ]')
#link = '[Click ผู้ทรงคุณวุฒิสามารถเลือกสาขาเชี่ยวชาญเพื่อประเมินบทความ](' + st.secrets.google.form3 + ')'
#st.markdown(link, unsafe_allow_html=True)
#st.image('./asset/QR_Form3.svg', width=200, caption="Scan เพื่อเลือกสาขาเชี่ยวชาญ")

tabs[1].header(':blue[ลงทะเบียน]')
tabs[1].markdown("ลงทะเบียนภายในวันที่ 29 มกราคม 2568 โดยมีอัตราค่าลงทะเบียนดังนี้")
tabs[1].markdown(":cat: ผู้นำเสนอภาคบรรยายระดับชาติ 2000 บาท")
tabs[1].markdown(":frog: ผู้นำเสนอโครงงานระดับปริญญาตรี (ภาคบรรยายและโปสเตอร์) 1000 บาท")
tabs[1].markdown(":tiger: อาจารย์และบุคคลทั่วไปเข้าร่วมประชุม 1000 บาท")
tabs[1].markdown(":dog: นักศึกษาเข้าร่วมประชุม 500 บาท")
tabs[1].markdown(":red[หมายเหตุ] กรณีส่งผลงานมากกว่าหนึ่งผลงานให้ลงทะเบียนแยกแต่ละผลงาน")
tabs[1].markdown("ชำระเงินค่าลงทะเบียนโดยการโอนเงินเข้าบัญชีธนาคารไทยพาณิชย์ จำกัด (มหาชน) สาขากำแพงแสน (มหาวิทยาลัยเกษตรศาสตร์) ชื่อบัญชี :rainbow[มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตกำแพงแสน] เลขที่ :rainbow[769-200001-0]")
link = '[Click เพื่อลงทะเบียน](' + st.secrets.google.form1 + ')'
tabs[1].markdown(link, unsafe_allow_html=True)
tabs[1].image('./asset/QR_Form1.svg', width=150, caption="Scan เพื่อลงทะเบียน")

tabs[2].header(':blue[ส่งบทความ]')
tabs[2].markdown("เปิดรับบทคัดย่อ/บทความฉบับเต็ม :rainbow[วันที่ 1 ตุลาคม - 6 ธันวาคม 2567]")
tabs[2].markdown("แจ้งผลพิจารณาบทความ :rainbow[วันที่ 9 มกราคม 2568]")

link = '[Click เพื่อส่งบทคัดย่อ/บทความฉบับเต็ม/ไฟล์นำเสนอภาคบรรยาย กรุณาส่งทีละไฟล์](' + st.secrets.google.form2 + ')'
tabs[2].markdown(link, unsafe_allow_html=True)
tabs[2].image('./asset/QR_Form2.svg', width=150, caption="Scan เพื่อส่งบทความ")

tabs[3].header(':blue[ดาวน์โหลดเอกสาร]')
#path = os.getcwd() + '//documents//'
path = './documents/'
files = os.listdir(path)
file_name = []
file_ext = []
for f in files:
    split_up = os.path.splitext(f)
    file_name.append(split_up[0])
    file_ext.append(split_up[1])

opt = tabs[3].selectbox("", file_name, label_visibility="collapsed", key='select_document')
selected_index = file_name.index(opt)

file = files[selected_index]
#path = os.getcwd() + '//info//' + file
path = './documents/' + file
#st.write(path)
if opt is not None:
    with open(path, "rb") as f:
        tabs[3].download_button(
            label="Download",
            data=f,
            file_name=file,
        )

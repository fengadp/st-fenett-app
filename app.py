import os
import streamlit as st
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

#st.header(':blue[วัตถุประสงค์]')
#st.markdown("1. เพื่อเป็นเวทีให้นิสิตนักศึกษาระดับอุดมศึกษา อาจารย์ นักวิจัย และนักวิชาการ จากสถาบันการศึกษา และหน่วยงานต่าง ๆ ได้มีโอกาสเผยแพร่ผลงานทางวิชาการสู่สาธารณะ")
#st.markdown("2. เพื่อให้เกิดการแลกเปลี่ยนแนวคิด ความรู้ และประสบการณ์ในการทำวิจัย เพื่อนำไปสู่ข้อสรุปหรือข้อเสนอแนะที่เป็นประโยชน์ระหว่างนักวิจัย นักวิชาการตลอดจนผู้ประกอบการด้านอุตสาหกรรมอาหารและอุตสาหกรรมอื่น ๆ ที่เกี่ยวข้อง")
#st.markdown("3. เพื่อสร้างเครือข่ายความร่วมมือทางวิชาการด้านวิศวกรรมอาหารระหว่างสถาบันการศึกษา หน่วยงานทั้งภาครัฐและเอกชน และหน่วยงานอื่น ๆ ที่เกี่ยวข้อง")

st.title(":green[Transforming Thailand’s Food Industry:] :red[_AI-Powered Solutions_]")
st.markdown("ประเทศไทยมีความอุดมสมบูรณ์ด้านทรัพยากรอาหาร มีอุตสาหกรรมแปรรูปอาหารจำนวนมาก งานวิจัย นวัตกรรม และเทคโนโลยีใหม่ ๆ ในด้านวิศวกรรมอาหารจะช่วยส่งเสริมให้เกิดการพัฒนาอุตสาหกรรมอาหารของประเทศ การประยุกต์ปัญญาประดิษฐ์ (Artificial Intelligence) เพื่อช่วยวิเคราะห์และประเมินผลข้อมูลกระบวนการผลิตอาหารสามารถเพิ่มประสิทธิภาพการทำงานในด้านต่าง ๆ ทำให้ระบบการผลิตใช้ทรัพยากรอย่างคุ้มค่า ประหยัดเวลา ใช้แรงงานน้อยลง เป็นกระบวนการผลิตที่มีความแม่นยำ น่าเชื่อถือ และปลอดภัย ทำให้เกิดการผลิตสินค้าและบริการที่ตอบสนองความต้องการของผู้บริโภคที่แตกต่างกัน")
st.markdown("วิศวกรรมอาหารเป็นสาขาวิชาทางวิศวกรรมที่บูรณาการความรู้ทางวิศวกรรมและวิทยาศาสตร์ร่วมกัน เพื่อใช้ในการพัฒนาเครื่องจักรผลิตอาหาร กระบวนการผลิตอาหาร และบริหารจัดการผลิตอาหาร โดยคำนึงถึงความปลอดภัยต่อผู้บริโภค และผลกระทบต่อสิ่งแวดล้อม วิศวกรรมอาหารจึงมีบทบาทสำคัญต่อการพัฒนาอุตสาหกรรมอาหาร และช่วยให้อุตสาหกรรมอาหารไทยมีการพัฒนาอย่างเข้มแข็งต่อเนื่องและสามารถแข่งขันได้ในระดับนานาชาติ")

#st.image('./asset/robotic1.jpg')
#cols_1 = st.columns(2)
#cols_1[0].markdown('')
#cols_1[0].image('./asset/robotic1.jpg')
#cols_1[1].markdown('')
#cols_1[1].image('./asset/fig9.jpg')
#cols_1[1].write('')

st.header(':blue[หัวข้อการประชุม]')
st.markdown("หัวข้อการประชุมจะครอบคลุมงานวิจัยและนวัตกรรมทางวิศวกรรม วิทยาศาสตร์ และเทคโนโลยี ที่เกี่ยวข้องกับอุตสาหกรรมอาหารและสาขาอื่น ๆ ที่เกี่ยว โดยการประชุมครั้งนี้ส่งเสริมให้นำเสนอผลงานที่สอดคล้องกับนโยบายการพัฒนาประเทศ Thailand 4.0 โดยมีหัวข้อดังนี้")
st.markdown(":balloon: Food Machinery")
st.markdown(":balloon: Food Processing Technology")
st.markdown(":balloon: Robotics and Automation in Food Processing")
st.markdown(":balloon: Food Quality Control and Evaluation")
st.markdown(":balloon: Food Safety and Supply Chain Management")
st.markdown(":balloon: Artificial Intelligence and Big Data Analytics in Food Industry")
st.markdown(":balloon: Related Topics in Food and Engineering Technology")

st.header(':blue[กำหนดการประชุมวิชาการ]')
with st.container(border=True):
    pdf_viewer('./documents/กำหนดการประชุมวิชาการวิศวกรรมอาหารแห่งชาติ ครั้งที่ 6.pdf')
#options = ['page 1', 'page 2', 'page 3']
#opt = st.selectbox("", options, label_visibility="collapsed", key='select_info')
#selected_index = options.index(opt)
#st.write(selected_index)
#if opt is not None:
#    with st.container(border=True):
#        pdf_viewer('./documents/กำหนดการ.pdf', pages_to_render=[selected_index + 1])

st.header(':blue[ลงทะเบียน]')
st.markdown("ลงทะเบียนภายในวันที่ 12 กุมภาพันธ์ 2568 โดยมีอัตราค่าลงทะเบียนดังนี้")
st.markdown(":cat: ผู้นำเสนอภาคบรรยายระดับชาติ 2000 บาท")
st.markdown(":frog: ผู้นำเสนอโครงงานระดับปริญญาตรี (ภาคบรรยายและโปสเตอร์) 1000 บาท")
st.markdown(":tiger: อาจารย์และบุคคลทั่วไปเข้าร่วมประชุม 1000 บาท")
st.markdown(":dog: นักศึกษาเข้าร่วมประชุม 200 บาท")
st.markdown("ชำระเงินค่าลงทะเบียนโดยการโอนเงินเข้าบัญชีธนาคารไทยพาณิชย์ จำกัด (มหาชน) สาขากำแพงแสน (มหาวิทยาลัยเกษตรศาสตร์) ชื่อบัญชี สุกัญญา วิชชุกิจ และ วันวิสาข์ ใจตรง เลขที่ 769-280259-3")
#link = '[Click เพื่อลงทะเบียน](https://forms.gle/JZ48pfoQLuLkxr6eA)'
link = '[Click เพื่อลงทะเบียน](google.form1)'
st.markdown(link, unsafe_allow_html=True)
st.image('./asset/QR1.svg', width=200, caption="Scan เพื่อลงทะเบียน")

st.header(':blue[ส่งบทความ]')
st.markdown("กำหนดส่งบทความฉบับเต็มภายใน :rainbow[วันที่ 7 กุมภาพันธ์ 2568]")
st.markdown("การตอบรับบทความฉบับเต็มภายใน :rainbow[วันที่ 10 กุมภาพันธ์ 2568]")

#link = '[Click เพื่อส่งบทคัดย่อ/บทความฉบับเต็ม/ไฟล์นำเสนอภาคบรรยาย กรุณาส่งทีละไฟล์](https://forms.gle/V1Bi3LRVwn4p4ReQ9)'
link = '[Click เพื่อส่งบทคัดย่อ/บทความฉบับเต็ม/ไฟล์นำเสนอภาคบรรยาย กรุณาส่งทีละไฟล์](google.form2)'
st.markdown(link, unsafe_allow_html=True)
st.image('./asset/QR2.svg', width=200, caption="Scan เพื่อส่งบทความ")

#st.header(':blue[การประเมินบทความทางวิชาการ]')
#link = '[Click ผู้ทรงคุณวุฒิสามารถเลือกสาขาเชี่ยวชาญเพื่อประเมินบทความ](https://forms.gle/oJ5K4fqfkEKtFUTC9)'
#st.markdown(link, unsafe_allow_html=True)
#st.image('./asset/form1.svg', width=200, caption="Scan เพื่อเลือกสาขาเชี่ยวชาญ")

st.header(':blue[ดาวน์โหลดเอกสาร]')
#path = os.getcwd() + '//documents//'
path = './documents/'
files = os.listdir(path)
file_name = []
file_ext = []
for f in files:
    split_up = os.path.splitext(f)
    file_name.append(split_up[0])
    file_ext.append(split_up[1])

opt = st.selectbox("", file_name, label_visibility="collapsed", key='select_document')
selected_index = file_name.index(opt)

file = files[selected_index]
#path = os.getcwd() + '//info//' + file
path = './documents/' + file
#st.write(path)
if opt is not None:
    with open(path, "rb") as f:
        st.download_button(
            label="Download",
            data=f,
            file_name=file,
        )

st.divider()

st.header(':blue[บทความประชุมวิชาการฉบับสมบูรณ์]')
page_number = st.number_input(label='', min_value=1, label_visibility="collapsed", key='input_page_number')
with st.container(border=True):
    pdf_viewer('./documents/บทความประชุมวิชาการฉบับสมบูรณ์.pdf', pages_to_render=[page_number])

st.header(':blue[บรรยากาศงานประชุมวิชาการวิศวกรรมอาหารแห่งชาติ ครั้งที่ 6]')

with st.container(border=True):
    image_index = st.slider(":blue[รูปภาพกิจกรรม]", 1, 12, 1,)
    image_file = './photos/photo' + str(image_index) + '.jpg'
    st.image(image_file)

#image_items = []
#numOfImage = 12
#for k in range(numOfImage):
#    image_file = './photos/photo' + str(k+1) + '.jpg'
    #st.write(image_file)
#    image_items.append(
#        dict(
#            title="",
#            text="",
#            img=image_file,
#        ),
#    )
#carousel(items=image_items, width=1)

#st.divider()

cols_2 = st.columns(2)
cols_2[0].subheader('สอบถามข้อมูลเพิ่มเติม')
cols_2[0].markdown("คุณวริศรา สมตน เจ้าหน้าที่ประสานงานประชุมวิชาการฯ")
cols_2[0].markdown("ภาควิชาวิศวกรรมการอาหาร คณะวิศวกรรมศาสตร์ กำแพงแสน มหาวิทยาลัยเกษตรศาสตร์ วิทยาเขตกำแพงแสน")
cols_2[0].markdown("1 หมู่ 6 ถ.มาลัยแมน ต.กำแพงแสน อ.กำแพงแสน จ.นครปฐม 73140")
cols_2[0].markdown("โทรศัพท์: 082-2376747 E-mail: fengwaso@ku.ac.th")

cols_2[1].subheader('การจองห้องพัก')

st.write('')
st.subheader('ผู้สนับสนุนการประชุมวิชาการ')
cols_3 = st.columns(2)
cols_3[0].image('./asset/suport1.jpg')
cols_3[1].image('./asset/suport2.jpg')

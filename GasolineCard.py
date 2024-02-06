import datetime
import streamlit as st
import pandas as pd
import gspread
import numpy as np
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
credentials_json = {
        "type": "service_account",
        "project_id": "noted-handler-379714",
        "private_key_id": "61988f9740276e066ac2fe2aeaac3fa4b6ff527c",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCPWdjJpLudGk7S\ngaV1l/RVUevfJTyrZmKfdMbSkjnpNG4wOGF69rs3h++8luanYcOt+TW87WiAVZum\nUqawNu1GYyh6CyoDxX4lR2/jAZWb/xJ7tgdW7t+rKv1hKTljke8F6kecPSznge/W\npUtegmMFaYTaZJNDuq29A5yT/zo5YWqoxpV0fxpOOlPMvoACelFNcvKsKLnOjaGN\nbjQqFpC+7Sl+LHGaqcO00mTYwbo7Ijj5i+BlYZAwDanN3XSd6Wwl3wnUnGNaWn+6\nVwHyQebXgmICq1iEHNBaoUbEdHDuPXepExoekvSNwx9Ng2vTNCRfzEQVL+3vYSjL\npqo86L9xAgMBAAECggEABQeMl/+N/xQ3F4LptpthHNS52zuL2kIme+x9lNIBUuWu\nZ4X04prxROChuErNlyoSkuIrYOBuAhGu2zorY8ObldSBDS4i2FzHoSB1ZCAwOvfL\nMti3P3U0VwW0O+JVw4DxY1Jd1pUdZBZ+nxfv0eYuefhCq2Rrt8y/D4KGzfj+lph/\nUZvOKQcu9MguBIJAx5xBTtNjeMjhJCdu1OdwyW5MO0irvLmqIQDIphuRvDvXbS93\nSg9zQFxuzLJMKe3jL0zgbkHBjABVnRFycDUWKLgRAmCjoGfY367k800/YNduBqQy\nVBHAQqL9Uuj9S3o5VtZ6uqtjHkhJcDhxnAH7B2G2wQKBgQDGM4fGuMiVTw0rfxSC\npV28y1r5p9tD6uJjTWbqqp0IpX3mjDgZwL0ig5U+3JBBU4n0Ix4WeDjq6/Wy6Tcn\n5Oo9eRwVOsCttl807/sKGBmZV5dRDdbD7NKLBI2sxtbLu1POisK+Si2fJV03mmE6\nm+3Y4DaJ/StovuTuEMIZBKFAoQKBgQC5J4itC5XJ9WCzKIupIF/uxxJGg6TofZvM\nDYkmzb9ZIoh9iFnB5InmlG14ngmRnjINeTqjN4YQtBJNSpk7p1Ra/C2Q+Do/Zm9G\nNWQKd3nYBSQxwNqd97CgzbmtxT8GkSWIvwCtD45oFNkrU0W6eH6/fhGjXNjPj2Ig\nYIHIFNV80QKBgQDALUzUcW0D4M97Qk/n0WHPYjoG4ivnccMq1+0XUnDK5nPp7EGl\nLs30vjMi7Yft34tergJJdS5zEnF8lUbGpt481sZVC0+x36f2003NXsrLdTOiAtIf\nzOvkoXihc3bnue4r0T28dn4/1mHJPSZTRsfbRqN7LoA9owKklpks2uFjoQKBgE0F\n7C6Idjx4jkyZXlfx9tZ/C9Q3qV9p+WjObLKuvp4W5o7KLQSizNcWAeA+Zh6kn4/J\nUaJaU7QZJM/wa4RMXKQo6c+344tCUqHzTfWotBAwO1lTL96tDlYmnspyFoDl2qZj\nRqW3pfcYTStfzc7/l0KT8ER0OGFH9XsginywZgsxAoGAUXm9ge4vbPqKcHNWPYmn\nM/zJ4zkIP57mmRHZBbukLlfXW3/tLHiSZWyotjjDBmcw1yZCoZhTvJcoxeH153V6\nXraQTIW17zjatG22e8E817VKMg/dvHz6KHDHM+DRRxhmGojVsBcUhzPYv/llFoGC\nNYyRe2J3ggufJ0lqCoQNxhg=\n-----END PRIVATE KEY-----\n",
        "client_email": "demo-867@noted-handler-379714.iam.gserviceaccount.com",
        "client_id": "108019621957189237850",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/demo-867%40noted-handler-379714.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_json, ['https://spreadsheets.google.com/feeds'])
gc = gspread.authorize(credentials)
area=['Sharkya AG','Asyut AG','Cairo AG','Giza AG','BeniSuef AG','Alexandria AG','Ismailia AG','Tanta AG','HUB','HQ']
google_sheet_url ='https://docs.google.com/spreadsheets/d/1pTPzvbCXpn8wlYcAymYRB7irmA3pAVWiFhtyVJJp1_s/edit#gid=0'
sh = gc.open_by_url(google_sheet_url)
worksheet= sh.get_worksheet(0)
st.markdown("<h1 style='text-align: center;'>طلب استبدال الكروت</h1>", unsafe_allow_html=True)
area = st.selectbox(
   "",
   ('Sharkya AG','Asyut AG','Cairo AG','Giza AG','BeniSuef AG','Alexandria AG','Ismailia AG','Tanta AG','HUB','HQ'),
   index=None,
   placeholder="اختار المنطقة",
)
vendor = st.selectbox(
   "",
   ('Total','Petro App','Octain','CPC'),
   index=None,
   placeholder="اختار الشركة",
)


# إضافة واجهة المستخدم باستخدام st.text_input
user_input_letter = st.text_input('حروف المعدة')

# التحقق من صحة المدخلات باستخدام الدالة المخصص


# إضافة واجهة المستخدم باستخدام st.text_input
user_input_number = st.text_input('ارقام المعدة')

# التحقق من صحة المدخلات باستخدام الدالة المخصصة



reason=st.text_area('ادخل السبب')
insert=st.button('حفظ')
row=[area,user_input_letter,user_input_number,vendor,reason]
if insert:
    worksheet.append_row(row)
    st.write('تم حفظ الطلب')
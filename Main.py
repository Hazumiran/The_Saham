import streamlit as st
from streamlit_option_menu import option_menu
# from fer.classes import Video
# from fer import FER
# import os
# import tempfile

page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://images.pexels.com/photos/2749481/pexels-photo-2749481.jpeg");
backround-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar
selected = option_menu(
    menu_title="TUGAS BESAR PENGOLAHAN CITRA DIGITAL - Kelompok 5 - The Saham",
    options=["Mochamad Hafidh Dwyanto - 211511043","Muchamad Diaz Adhari - 211511044", "Uqyanzie Bintang KFF - 211511062"],
    icons=["user", "user", "user"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Menambahkan judul dan deskripsi
st.title("Antarmuka Pengenalan Ekspresi Wajah dengan Deep Neural Network")

uploaded_file = st.file_uploader(
    "Silahkan Upload Video disini", type=["mp4", "mkv", "mov"], accept_multiple_files=False)

st.video(uploaded_file)

if uploaded_file is None:
    st.warning("Please upload a video file.")
else:
    with st.spinner('Wait for it...'):

        # detector = FER(mtcnn=True)
        # with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        #     tmp_file.write(uploaded_file.read())
        #     video_path = tmp_file.name
        #     video = Video(video_path)
        # if not os.path.exists(video_path):
        #     st.warning("Video file not found.")
        # else:
        #     raw_data = video.analyze(detector, display=False)
        #     # continue with analysis
        # os.unlink(video_path)  # delete temporary file
        st.success("Done!")
    # df = video.to_pandas(raw_data)
    # df = video.get_first_face(df)
    # df = video.get_emotions(df)

    # st.image(fig)
    # st.write(df)
    # st.line_chart(df)

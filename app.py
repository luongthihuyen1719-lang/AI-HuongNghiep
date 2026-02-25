import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ứng Dụng Hướng Nghiệp Cho Học Sinh", layout="wide")

st.title("🎓 ỨNG DỤNG HƯỚNG NGHIỆP THÔNG MINH 4.0")
st.markdown("### Ứng dụng phân tích sở thích & cơ hội việc làm")

# =========================
# DANH SÁCH MÔN HỌC
# =========================

mon_hoc = [
    "Toán","Ngữ văn","Tiếng Anh",
    "Vật lý","Hóa học","Sinh học",
    "Tin học","Lịch sử","Địa lý"
]

mon_chon = st.multiselect("📚 Chọn môn bạn yêu thích:", mon_hoc)

# =========================
# ĐỌC FILE NGÀNH NGHỀ
# =========================

try:
    df_nganh = pd.read_csv("nganh_nghe.csv", encoding="utf-8")
except:
    st.error("❌ Không tìm thấy file nganh_nghe.csv")
    st.stop()

# =========================
# PHÂN TÍCH
# =========================

if st.button("🚀 Phân tích ngành phù hợp"):

    if not mon_chon:
        st.warning("Vui lòng chọn ít nhất 1 môn học.")
    else:

        ket_qua = []

        for _, row in df_nganh.iterrows():

            # Tách nhóm môn của ngành
            mon_nganh = str(row["Nhom_mon"]).split("|")

            # Tính mức độ phù hợp
            match = len(set(mon_chon) & set(mon_nganh))
            phu_hop = (match / len(mon_nganh)) * 100

            # Điểm tổng hợp
            diem_tong = phu_hop * 0.6 + row["Co_hoi_viec_lam"] * 0.4

            ket_qua.append({
                "Ngành": row["Ten_nganh"],
                "Phù hợp (%)": round(phu_hop,1),
                "Cơ hội việc làm (%)": row["Co_hoi_viec_lam"],
                "Điểm tổng": round(diem_tong,1),
                "Mô tả": row["Mo_ta"]
            })

        df_kq = pd.DataFrame(ket_qua)
        df_kq = df_kq.sort_values(by="Điểm tổng", ascending=False)

        # =========================
        # NGÀNH TỐT NHẤT
        # =========================

        st.success("🎯 Ngành có tiềm năng cao nhất:")

        st.subheader(df_kq.iloc[0]["Ngành"])
        st.write("📌 Mô tả:", df_kq.iloc[0]["Mô tả"])
        st.write("📊 Điểm tổng:", df_kq.iloc[0]["Điểm tổng"])

        # =========================
        # TOP 10
        # =========================

        st.markdown("## 📊 Top 10 ngành tiềm năng nhất")
        st.dataframe(df_kq.head(10)[
            ["Ngành","Phù hợp (%)","Cơ hội việc làm (%)","Điểm tổng"]
        ])

        st.bar_chart(df_kq.head(10).set_index("Ngành")["Điểm tổng"])
        st.caption("© 2026 NHÓM 1 - LỚP 10A2 - TRƯỜNG THPT ĐÌNH LẬP")


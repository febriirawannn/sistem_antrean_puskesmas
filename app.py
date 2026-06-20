import streamlit as st
from collections import deque
from datetime import datetime

# =====================================
# CONFIG
# =====================================
st.set_page_config(
    page_title="Sistem Antrean Puskesmas",
    page_icon="🏥",
    layout="wide"
)

# =====================================
# SESSION STATE
# =====================================
if "antrian_normal" not in st.session_state:
    st.session_state.antrian_normal = deque()

if "antrian_darurat" not in st.session_state:
    st.session_state.antrian_darurat = deque()

if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

if "nomor_normal" not in st.session_state:
    st.session_state.nomor_normal = 1

if "nomor_darurat" not in st.session_state:
    st.session_state.nomor_darurat = 1

# =====================================
# HEADER
# =====================================
st.title("🏥 Sistem Antrean Puskesmas")
st.caption("Tugas Projek Struktur Data")

# =====================================
# MENU
# =====================================
menu = st.sidebar.selectbox(
    "Menu",
    [
        "Dashboard",
        "Tambah Pasien",
        "Panggil Pasien",
        "Cari Pasien",
        "Riwayat Pasien",
        "Reset Data"
    ]
)

# =====================================
# DASHBOARD
# =====================================
if menu == "Dashboard":

    st.header("Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Antrean Normal",
        len(st.session_state.antrian_normal)
    )

    col2.metric(
        "Antrean Darurat",
        len(st.session_state.antrian_darurat)
    )

    col3.metric(
        "Pasien Dilayani",
        len(st.session_state.riwayat)
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📋 Antrean Normal")

        if len(st.session_state.antrian_normal) > 0:

            for pasien in st.session_state.antrian_normal:

                st.write(
                    f"{pasien['nomor']} - {pasien['nama']}"
                )

        else:

            st.info("Belum ada antrean normal")

    with col2:

        st.subheader("🚨 Antrean Darurat")

        if len(st.session_state.antrian_darurat) > 0:

            for pasien in st.session_state.antrian_darurat:

                st.write(
                    f"{pasien['nomor']} - {pasien['nama']}"
                )

        else:

            st.info("Belum ada antrean darurat")

# =====================================
# TAMBAH PASIEN
# =====================================
elif menu == "Tambah Pasien":

    st.header("Tambah Pasien")

    with st.form("form_pasien"):

        nama = st.text_input("Nama Pasien")
        keluhan = st.text_area("Keluhan")

        jenis = st.radio(
            "Jenis Pasien",
            ["Normal", "Darurat"]
        )

        submit = st.form_submit_button(
            "Tambah Antrean"
        )

    if submit:

        if nama.strip() == "":
            st.warning(
                "Nama pasien wajib diisi"
            )

        else:

            if jenis == "Normal":

                nomor = (
                    f"N{st.session_state.nomor_normal:03d}"
                )

                pasien = {
                    "nomor": nomor,
                    "nama": nama,
                    "keluhan": keluhan,
                    "jenis": jenis,
                    "waktu": datetime.now().strftime(
                        "%d-%m-%Y %H:%M:%S"
                    )
                }

                st.session_state.antrian_normal.append(
                    pasien
                )

                st.session_state.nomor_normal += 1

            else:

                nomor = (
                    f"D{st.session_state.nomor_darurat:03d}"
                )

                pasien = {
                    "nomor": nomor,
                    "nama": nama,
                    "keluhan": keluhan,
                    "jenis": jenis,
                    "waktu": datetime.now().strftime(
                        "%d-%m-%Y %H:%M:%S"
                    )
                }

                st.session_state.antrian_darurat.append(
                    pasien
                )

                st.session_state.nomor_darurat += 1

            st.success(
                f"Pasien {nama} berhasil ditambahkan dengan nomor {nomor}"
            )

# =====================================
# PANGGIL PASIEN
# =====================================
elif menu == "Panggil Pasien":

    st.header("Panggil Pasien")

    sekarang = None
    berikutnya = None
    tipe = None

    if len(st.session_state.antrian_darurat) > 0:

        sekarang = (
            st.session_state.antrian_darurat[0]
        )

        tipe = "darurat"

        if len(
            st.session_state.antrian_darurat
        ) > 1:

            berikutnya = (
                st.session_state.antrian_darurat[1]
            )

        elif len(
            st.session_state.antrian_normal
        ) > 0:

            berikutnya = (
                st.session_state.antrian_normal[0]
            )

    elif len(
        st.session_state.antrian_normal
    ) > 0:

        sekarang = (
            st.session_state.antrian_normal[0]
        )

        tipe = "normal"

        if len(
            st.session_state.antrian_normal
        ) > 1:

            berikutnya = (
                st.session_state.antrian_normal[1]
            )

    if sekarang:

        st.subheader(
            "🔔 Pasien Dipanggil"
        )

        st.success(
            f"{sekarang['nomor']} - {sekarang['nama']}"
        )

        st.subheader(
            "⏭ Pasien Berikutnya"
        )

        if berikutnya:

            st.info(
                f"{berikutnya['nomor']} - {berikutnya['nama']}"
            )

        else:

            st.info(
                "Belum ada antrean berikutnya"
            )

        if st.button(
            "Panggil Pasien"
        ):

            if tipe == "darurat":

                pasien = (
                    st.session_state
                    .antrian_darurat
                    .popleft()
                )

            else:

                pasien = (
                    st.session_state
                    .antrian_normal
                    .popleft()
                )

            st.session_state.riwayat.append(
                pasien
            )

            st.rerun()

    else:

        st.warning(
            "Tidak ada antrean"
        )

# =====================================
# CARI PASIEN
# =====================================
elif menu == "Cari Pasien":

    st.header("Cari Pasien")

    keyword = st.text_input(
        "Masukkan nama atau nomor antrean"
    )

    if keyword:

        hasil = []

        semua_pasien = (
            list(
                st.session_state.antrian_normal
            )
            +
            list(
                st.session_state.antrian_darurat
            )
        )

        for pasien in semua_pasien:

            if (
                keyword.lower()
                in pasien["nama"].lower()
                or
                keyword.lower()
                in pasien["nomor"].lower()
            ):

                hasil.append(
                    pasien
                )

        if hasil:

            for pasien in hasil:

                st.success(
                    f"{pasien['nomor']} - "
                    f"{pasien['nama']} "
                    f"({pasien['jenis']})"
                )

        else:

            st.error(
                "Pasien tidak ditemukan"
            )

# =====================================
# RIWAYAT
# =====================================
elif menu == "Riwayat Pasien":

    st.header(
        "Riwayat Pasien Dilayani"
    )

    if len(
        st.session_state.riwayat
    ) > 0:

        for pasien in (
            st.session_state.riwayat
        ):

            st.write(
                f"{pasien['nomor']} - "
                f"{pasien['nama']} - "
                f"{pasien['jenis']} - "
                f"{pasien['waktu']}"
            )

    else:

        st.info(
            "Belum ada pasien yang dilayani"
        )

# =====================================
# RESET DATA
# =====================================
elif menu == "Reset Data":

    st.header(
        "Reset Sistem"
    )

    st.warning(
        "Semua antrean dan riwayat akan dihapus."
    )

    if st.button(
        "Hapus Semua Data"
    ):

        st.session_state.antrian_normal.clear()
        st.session_state.antrian_darurat.clear()
        st.session_state.riwayat.clear()

        st.session_state.nomor_normal = 1
        st.session_state.nomor_darurat = 1

        st.success(
            "Semua data berhasil dihapus."
        )
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# =========================================================
# DATA SEMENTARA
# =========================================================

data_mobil_list = [
    ["M001", "Mobil A", 500000, "Tersedia"],
    ["M002", "Mobil B", 300000, "Tersedia"],
    ["M003", "Mobil C", 200000, "Tersedia"]
]

data_penyewa_list = [
    ["P001", "Andi", "327001", "08123456789", "Jakarta"]
]

data_transaksi = []


# =========================================================
# DATA MOBIL
# =========================================================

def data_mobil(parent):

    window = tk.Toplevel(parent)
    window.title("Data Mobil")
    window.geometry("750x550")

    tk.Label(
        window,
        text="DATA MOBIL",
        font=("Arial", 20)
    ).pack(pady=15)

    form = tk.Frame(window)
    form.pack()

    tk.Label(form, text="Kode Mobil").grid(
        row=0, column=0, padx=10, pady=5
    )

    kode = tk.Entry(form)
    kode.grid(row=0, column=1)

    tk.Label(form, text="Nama Mobil").grid(
        row=1, column=0, padx=10, pady=5
    )

    nama = tk.Entry(form)
    nama.grid(row=1, column=1)

    tk.Label(form, text="Harga / Hari").grid(
        row=2, column=0, padx=10, pady=5
    )

    harga = tk.Entry(form)
    harga.grid(row=2, column=1)

    tk.Label(form, text="Status").grid(
        row=3, column=0, padx=10, pady=5
    )

    status = ttk.Combobox(
        form,
        values=["Tersedia", "Disewa"],
        state="readonly"
    )

    status.grid(row=3, column=1)
    status.set("Tersedia")

    tabel = ttk.Treeview(
        window,
        columns=("Kode", "Nama", "Harga", "Status"),
        show="headings"
    )

    tabel.heading("Kode", text="Kode")
    tabel.heading("Nama", text="Nama Mobil")
    tabel.heading("Harga", text="Harga / Hari")
    tabel.heading("Status", text="Status")

    tabel.pack(
        padx=20,
        pady=20,
        fill="both",
        expand=True
    )

    def tampilkan():

        for item in tabel.get_children():
            tabel.delete(item)

        for mobil in data_mobil_list:

            tabel.insert(
                "",
                tk.END,
                values=(
                    mobil[0],
                    mobil[1],
                    "Rp " + f"{int(mobil[2]):,}",
                    mobil[3]
                )
            )

    def tambah():

        if kode.get() == "" or nama.get() == "" or harga.get() == "":
            messagebox.showwarning(
                "Peringatan",
                "Data belum lengkap!"
            )
            return

        try:
            harga_mobil = int(harga.get())
        except:
            messagebox.showwarning(
                "Peringatan",
                "Harga harus berupa angka!"
            )
            return

        data_mobil_list.append([
            kode.get(),
            nama.get(),
            harga_mobil,
            status.get()
        ])

        messagebox.showinfo(
            "Berhasil",
            "Data mobil berhasil ditambahkan!"
        )

        kode.delete(0, tk.END)
        nama.delete(0, tk.END)
        harga.delete(0, tk.END)

        tampilkan()

    def hapus():

        pilihan = tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data yang ingin dihapus!"
            )
            return

        item = tabel.item(pilihan[0])
        kode_hapus = item["values"][0]

        for mobil in data_mobil_list:

            if mobil[0] == kode_hapus:
                data_mobil_list.remove(mobil)
                break

        tampilkan()

        messagebox.showinfo(
            "Berhasil",
            "Data berhasil dihapus!"
        )

    tombol = tk.Frame(window)
    tombol.pack(pady=10)

    tk.Button(
        tombol,
        text="TAMBAH",
        width=12,
        command=tambah
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        tombol,
        text="HAPUS",
        width=12,
        command=hapus
    ).grid(row=0, column=1, padx=5)

    tampilkan()


# =========================================================
# DATA PENYEWA
# =========================================================

def data_penyewa(parent):

    window = tk.Toplevel(parent)
    window.title("Data Penyewa")
    window.geometry("800x550")

    tk.Label(
        window,
        text="DATA PENYEWA",
        font=("Arial", 20)
    ).pack(pady=15)

    form = tk.Frame(window)
    form.pack()

    tk.Label(form, text="ID Penyewa").grid(
        row=0, column=0, padx=10, pady=5
    )

    id_penyewa = tk.Entry(form)
    id_penyewa.grid(row=0, column=1)

    tk.Label(form, text="Nama").grid(
        row=1, column=0, padx=10, pady=5
    )

    nama = tk.Entry(form)
    nama.grid(row=1, column=1)

    tk.Label(form, text="No KTP").grid(
        row=2, column=0, padx=10, pady=5
    )

    ktp = tk.Entry(form)
    ktp.grid(row=2, column=1)

    tk.Label(form, text="No HP").grid(
        row=3, column=0, padx=10, pady=5
    )

    hp = tk.Entry(form)
    hp.grid(row=3, column=1)

    tk.Label(form, text="Alamat").grid(
        row=4, column=0, padx=10, pady=5
    )

    alamat = tk.Entry(form)
    alamat.grid(row=4, column=1)

    tabel = ttk.Treeview(
        window,
        columns=("ID", "Nama", "KTP", "HP", "Alamat"),
        show="headings"
    )

    tabel.heading("ID", text="ID")
    tabel.heading("Nama", text="Nama")
    tabel.heading("KTP", text="No KTP")
    tabel.heading("HP", text="No HP")
    tabel.heading("Alamat", text="Alamat")

    tabel.pack(
        padx=20,
        pady=20,
        fill="both",
        expand=True
    )

    def tampilkan():

        for item in tabel.get_children():
            tabel.delete(item)

        for penyewa in data_penyewa_list:

            tabel.insert(
                "",
                tk.END,
                values=(
                    penyewa[0],
                    penyewa[1],
                    penyewa[2],
                    penyewa[3],
                    penyewa[4]
                )
            )

    def tambah():

        if (
            id_penyewa.get() == ""
            or nama.get() == ""
            or ktp.get() == ""
            or hp.get() == ""
            or alamat.get() == ""
        ):
            messagebox.showwarning(
                "Peringatan",
                "Data belum lengkap!"
            )
            return

        data_penyewa_list.append([
            id_penyewa.get(),
            nama.get(),
            ktp.get(),
            hp.get(),
            alamat.get()
        ])

        messagebox.showinfo(
            "Berhasil",
            "Data penyewa berhasil ditambahkan!"
        )

        id_penyewa.delete(0, tk.END)
        nama.delete(0, tk.END)
        ktp.delete(0, tk.END)
        hp.delete(0, tk.END)
        alamat.delete(0, tk.END)

        tampilkan()

    def hapus():

        pilihan = tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih data yang ingin dihapus!"
            )
            return

        item = tabel.item(pilihan[0])
        id_hapus = item["values"][0]

        for penyewa in data_penyewa_list:

            if penyewa[0] == id_hapus:
                data_penyewa_list.remove(penyewa)
                break

        tampilkan()

    tombol = tk.Frame(window)
    tombol.pack(pady=10)

    tk.Button(
        tombol,
        text="TAMBAH",
        width=12,
        command=tambah
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        tombol,
        text="HAPUS",
        width=12,
        command=hapus
    ).grid(row=0, column=1, padx=5)

    tampilkan()


# =========================================================
# TRANSAKSI RENTAL
# =========================================================

def transaksi_rental(parent):

    window = tk.Toplevel(parent)
    window.title("Transaksi Rental")
    window.geometry("900x600")

    tk.Label(
        window,
        text="TRANSAKSI RENTAL",
        font=("Arial", 20)
    ).pack(pady=15)

    form = tk.Frame(window)
    form.pack()

    tk.Label(form, text="No Rental").grid(
        row=0, column=0, padx=10, pady=7
    )

    nomor = tk.Entry(form)
    nomor.grid(row=0, column=1)

    tk.Label(form, text="Penyewa").grid(
        row=1, column=0, padx=10, pady=7
    )

    pilihan_penyewa = []

    for penyewa in data_penyewa_list:
        pilihan_penyewa.append(
            penyewa[0] + " - " + penyewa[1]
        )

    penyewa_combo = ttk.Combobox(
        form,
        values=pilihan_penyewa,
        state="readonly",
        width=30
    )

    penyewa_combo.grid(row=1, column=1)

    tk.Label(form, text="Mobil").grid(
        row=2, column=0, padx=10, pady=7
    )

    pilihan_mobil = []

    for mobil in data_mobil_list:

        if mobil[3] == "Tersedia":
            pilihan_mobil.append(
                mobil[0] + " - " + mobil[1]
            )

    mobil_combo = ttk.Combobox(
        form,
        values=pilihan_mobil,
        state="readonly",
        width=30
    )

    mobil_combo.grid(row=2, column=1)

    tk.Label(form, text="Harga / Hari").grid(
        row=3, column=0, padx=10, pady=7
    )

    harga = tk.Entry(form)
    harga.grid(row=3, column=1)

    tk.Label(form, text="Lama Sewa").grid(
        row=4, column=0, padx=10, pady=7
    )

    lama = tk.Entry(form)
    lama.grid(row=4, column=1)

    tk.Label(form, text="Total").grid(
        row=5, column=0, padx=10, pady=7
    )

    total = tk.Entry(form)
    total.grid(row=5, column=1)

    def pilih_mobil(event):

        pilihan = mobil_combo.get()

        if pilihan == "":
            return

        kode_mobil = pilihan.split(" - ")[0]

        for mobil in data_mobil_list:

            if mobil[0] == kode_mobil:

                harga.delete(0, tk.END)
                harga.insert(0, mobil[2])
                break

    mobil_combo.bind(
        "<<ComboboxSelected>>",
        pilih_mobil
    )

    def hitung_total():

        try:

            harga_hari = int(harga.get())
            jumlah_hari = int(lama.get())

            hasil = harga_hari * jumlah_hari

            total.delete(0, tk.END)
            total.insert(0, hasil)

        except:

            messagebox.showwarning(
                "Peringatan",
                "Masukkan angka yang benar!"
            )

    def tampilkan_transaksi():

        for item in tabel.get_children():
            tabel.delete(item)

        for transaksi in data_transaksi:

            tabel.insert(
                "",
                tk.END,
                values=(
                    transaksi[0],
                    transaksi[1],
                    transaksi[2],
                    transaksi[3],
                    "Rp " + f"{int(float(transaksi[4])):,}",
                    transaksi[5]
                )
            )

    def proses_rental():

        if (
            nomor.get() == ""
            or penyewa_combo.get() == ""
            or mobil_combo.get() == ""
            or lama.get() == ""
        ):
            messagebox.showwarning(
                "Peringatan",
                "Data transaksi belum lengkap!"
            )
            return

        try:

            jumlah_hari = int(lama.get())
            biaya = int(harga.get()) * jumlah_hari

        except:

            messagebox.showwarning(
                "Peringatan",
                "Lama sewa harus berupa angka!"
            )
            return

        mobil_dipilih = mobil_combo.get()
        kode_mobil = mobil_dipilih.split(" - ")[0]

        for mobil in data_mobil_list:

            if mobil[0] == kode_mobil:
                mobil[3] = "Disewa"
                break

        data_transaksi.append([
            nomor.get(),
            penyewa_combo.get(),
            mobil_combo.get(),
            jumlah_hari,
            biaya,
            "Disewa"
        ])

        messagebox.showinfo(
            "Berhasil",
            "Transaksi rental berhasil!"
        )

        tampilkan_transaksi()

        nomor.delete(0, tk.END)
        penyewa_combo.set("")
        mobil_combo.set("")
        harga.delete(0, tk.END)
        lama.delete(0, tk.END)
        total.delete(0, tk.END)

        pilihan_baru = []

        for mobil in data_mobil_list:

            if mobil[3] == "Tersedia":

                pilihan_baru.append(
                    mobil[0] + " - " + mobil[1]
                )

        mobil_combo["values"] = pilihan_baru

    tabel = ttk.Treeview(
        window,
        columns=("No", "Penyewa", "Mobil", "Lama", "Total", "Status"),
        show="headings"
    )

    tabel.heading("No", text="No Rental")
    tabel.heading("Penyewa", text="Penyewa")
    tabel.heading("Mobil", text="Mobil")
    tabel.heading("Lama", text="Lama")
    tabel.heading("Total", text="Total")
    tabel.heading("Status", text="Status")

    tabel.pack(
        padx=20,
        pady=20,
        fill="both",
        expand=True
    )

    tombol = tk.Frame(window)
    tombol.pack(pady=10)

    tk.Button(
        tombol,
        text="HITUNG TOTAL",
        width=15,
        command=hitung_total
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        tombol,
        text="PROSES RENTAL",
        width=15,
        command=proses_rental
    ).grid(row=0, column=1, padx=5)

    tampilkan_transaksi()


# =========================================================
# PENGEMBALIAN
# =========================================================

def pengembalian(parent):

    window = tk.Toplevel(parent)
    window.title("Pengembalian Mobil")
    window.geometry("850x550")

    tk.Label(
        window,
        text="PENGEMBALIAN MOBIL",
        font=("Arial", 20)
    ).pack(pady=15)

    form = tk.Frame(window)
    form.pack()

    tk.Label(form, text="Pilih Transaksi").grid(
        row=0, column=0, padx=10, pady=7
    )

    pilihan_transaksi = []

    for transaksi in data_transaksi:

        if transaksi[5] == "Disewa":

            pilihan_transaksi.append(
                transaksi[0] + " - " + transaksi[2]
            )

    transaksi_combo = ttk.Combobox(
        form,
        values=pilihan_transaksi,
        state="readonly",
        width=30
    )

    transaksi_combo.grid(row=0, column=1)

    tk.Label(form, text="Biaya Rental").grid(
        row=1, column=0, padx=10, pady=7
    )

    biaya = tk.Entry(form)
    biaya.grid(row=1, column=1)

    tk.Label(form, text="Terlambat (Hari)").grid(
        row=2, column=0, padx=10, pady=7
    )

    terlambat = tk.Entry(form)
    terlambat.grid(row=2, column=1)

    tk.Label(form, text="Denda").grid(
        row=3, column=0, padx=10, pady=7
    )

    denda = tk.Entry(form)
    denda.grid(row=3, column=1)

    tk.Label(form, text="Total Bayar").grid(
        row=4, column=0, padx=10, pady=7
    )

    total_bayar = tk.Entry(form)
    total_bayar.grid(row=4, column=1)

    def pilih_transaksi(event):

        pilihan = transaksi_combo.get()

        if pilihan == "":
            return

        nomor = pilihan.split(" - ")[0]

        for transaksi in data_transaksi:

            if transaksi[0] == nomor:

                biaya.delete(0, tk.END)
                biaya.insert(0, transaksi[4])
                break

    transaksi_combo.bind(
        "<<ComboboxSelected>>",
        pilih_transaksi
    )

    def hitung_denda():

        try:

            biaya_rental = int(biaya.get())
            jumlah_terlambat = int(terlambat.get())

            denda_hari = 100000

            hasil_denda = jumlah_terlambat * denda_hari

            hasil_total = biaya_rental + hasil_denda

            denda.delete(0, tk.END)
            denda.insert(0, hasil_denda)

            total_bayar.delete(0, tk.END)
            total_bayar.insert(0, hasil_total)

        except:

            messagebox.showwarning(
                "Peringatan",
                "Masukkan angka yang benar!"
            )

    def proses_pengembalian():

        pilihan = transaksi_combo.get()

        if pilihan == "":

            messagebox.showwarning(
                "Peringatan",
                "Pilih transaksi terlebih dahulu!"
            )

            return

        nomor = pilihan.split(" - ")[0]

        for transaksi in data_transaksi:

            if transaksi[0] == nomor:

                transaksi[5] = "Selesai"

                kode_mobil = transaksi[2].split(" - ")[0]

                for mobil in data_mobil_list:

                    if mobil[0] == kode_mobil:

                        mobil[3] = "Tersedia"
                        break

                break

        messagebox.showinfo(
            "Berhasil",
            "Mobil berhasil dikembalikan!"
        )

        transaksi_combo.set("")
        biaya.delete(0, tk.END)
        terlambat.delete(0, tk.END)
        denda.delete(0, tk.END)
        total_bayar.delete(0, tk.END)

        pilihan_baru = []

        for transaksi in data_transaksi:

            if transaksi[5] == "Disewa":

                pilihan_baru.append(
                    transaksi[0] + " - " + transaksi[2]
                )

        transaksi_combo["values"] = pilihan_baru

    tombol = tk.Frame(window)
    tombol.pack(pady=15)

    tk.Button(
        tombol,
        text="HITUNG DENDA",
        width=15,
        command=hitung_denda
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        tombol,
        text="KEMBALIKAN",
        width=15,
        command=proses_pengembalian
    ).grid(row=0, column=1, padx=5)


# =========================================================
# LAPORAN
# =========================================================

def laporan(parent):

    window = tk.Toplevel(parent)
    window.title("Laporan Rental Mobil")
    window.geometry("900x550")

    tk.Label(
        window,
        text="LAPORAN RENTAL MOBIL",
        font=("Arial", 20)
    ).pack(pady=15)

    tabel = ttk.Treeview(
        window,
        columns=("No", "Penyewa", "Mobil", "Lama", "Total", "Status"),
        show="headings"
    )

    tabel.heading("No", text="No Rental")
    tabel.heading("Penyewa", text="Penyewa")
    tabel.heading("Mobil", text="Mobil")
    tabel.heading("Lama", text="Lama")
    tabel.heading("Total", text="Total")
    tabel.heading("Status", text="Status")

    tabel.column("No", width=100)
    tabel.column("Penyewa", width=150)
    tabel.column("Mobil", width=180)
    tabel.column("Lama", width=80)
    tabel.column("Total", width=150)
    tabel.column("Status", width=100)

    tabel.pack(
        padx=20,
        pady=10,
        fill="both",
        expand=True
    )

    label_jumlah = tk.Label(
        window,
        text="Jumlah Transaksi : 0",
        font=("Arial", 12)
    )

    label_jumlah.pack()

    label_pendapatan = tk.Label(
        window,
        text="Total Pendapatan : Rp 0",
        font=("Arial", 12)
    )

    label_pendapatan.pack(pady=5)

    def tampilkan_laporan():

        for item in tabel.get_children():
            tabel.delete(item)

        jumlah = 0
        pendapatan = 0

        for transaksi in data_transaksi:

            tabel.insert(
                "",
                tk.END,
                values=(
                    transaksi[0],
                    transaksi[1],
                    transaksi[2],
                    str(transaksi[3]) + " Hari",
                    "Rp " + f"{int(float(transaksi[4])):,}",
                    transaksi[5]
                )
            )

            jumlah += 1
            pendapatan += int(float(transaksi[4]))

        label_jumlah.config(
            text="Jumlah Transaksi : " + str(jumlah)
        )

        label_pendapatan.config(
            text="Total Pendapatan : Rp " + f"{pendapatan:,}"
        )

    tk.Button(
        window,
        text="REFRESH LAPORAN",
        width=20,
        command=tampilkan_laporan
    ).pack(pady=10)

    tampilkan_laporan()


# =========================================================
# MENU UTAMA
# =========================================================

def menu_utama():

    menu_app = tk.Toplevel(root)
    menu_app.title("Menu Utama")
    menu_app.geometry("400x500")

    tk.Label(
        menu_app,
        text="SISTEM RENTAL MOBIL",
        font=("Arial", 20)
    ).pack(pady=25)

    tk.Button(
        menu_app,
        text="Data Mobil",
        width=20,
        command=lambda: data_mobil(menu_app)
    ).pack(pady=5)

    tk.Button(
        menu_app,
        text="Data Penyewa",
        width=20,
        command=lambda: data_penyewa(menu_app)
    ).pack(pady=5)

    tk.Button(
        menu_app,
        text="Transaksi Rental",
        width=20,
        command=lambda: transaksi_rental(menu_app)
    ).pack(pady=5)

    tk.Button(
        menu_app,
        text="Pengembalian",
        width=20,
        command=lambda: pengembalian(menu_app)
    ).pack(pady=5)

    tk.Button(
        menu_app,
        text="Laporan",
        width=20,
        command=lambda: laporan(menu_app)
    ).pack(pady=5)

    tk.Button(
        menu_app,
        text="Keluar",
        width=20,
        command=menu_app.destroy
    ).pack(pady=20)


# =========================================================
# LOGIN
# =========================================================

def login():

    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "12345":

        messagebox.showinfo(
            "Login",
            "Login berhasil!"
        )

        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

        menu_utama()

    else:

        messagebox.showerror(
            "Login Gagal",
            "Username atau password salah!"
        )


# =========================================================
# PROGRAM UTAMA
# =========================================================

root = tk.Tk()

root.title("Login Sistem Rental Mobil")
root.geometry("400x300")

tk.Label(
    root,
    text="LOGIN RENTAL MOBIL",
    font=("Arial", 20)
).pack(pady=25)

tk.Label(
    root,
    text="Username"
).pack()

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(
    root,
    text="Password"
).pack()

entry_password = tk.Entry(
    root,
    show="*"
)

entry_password.pack(pady=5)

tk.Button(
    root,
    text="LOGIN",
    width=15,
    command=login
).pack(pady=20)

root.mainloop()
## part 3
## IND-PS2-69-SAT-09


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QButtonGroup, QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QRadioButton
from random import shuffle, randint ## untuk acakacak


""" PEMBUATAN CLASS UNTUK SIMPAN PERTANYAAN """
class Question:
    def __init__(self, tanyaan, benar, salah1, salah2, salah3):
        self.tanyaan = tanyaan
        self.benar = benar
        self.salah1 = salah1
        self.salah2 = salah2
        self.salah3 = salah3


""" BUAT PERTANYAAN """
LIST_TANYA = list()
LIST_TANYA.append(Question("sudah makan belum?", "sudah", "belum 2 kali", "sudah 3 kali", "ngak makan"))
LIST_TANYA.append(Question("Gunanya tabir surya untuk...", "terlindung dari sinar matahari", "lamar kerja", "untuk dimakan", "obat mata"))
LIST_TANYA.append(Question("Kapan hari guru?", "25 November", "8 Juli", "4 September", "17 Agustus"))
LIST_TANYA.append(Question("8 - 1 = ?", "7", "4", "13", "9"))
LIST_TANYA.append(Question("Umumnya mandi berapa kali sehari?", "2 kali sehari", "3 kali sehari", "4 kali sehari", "1 kali sehari"))

""" APLIKASI DAN JENDELA """
aplikasi = QApplication([])
jendela = QWidget()
jendela.setWindowTitle("INI APLIKASI MEMORY CARD SAYA") ## JUDUL APLIKASI
jendela.resize(250, 150) ## ukuran jendela


""" WIDGET """
pertanyaan = QLabel("SUDAH MAKAN BELUM?")
tombol = QPushButton("JAWAB")
RadioGroupBox = QGroupBox("Pilihan jawaban")
AnswerGroupBox = QGroupBox("INI JAWABANNYA")
rbtn_1 = QRadioButton('Entsy')
rbtn_2 = QRadioButton('smurf')
rbtn_3 = QRadioButton('Chulymtsy')
rbtn_4 = QRadioButton('Aleut')
benar_salah = QLabel("BENAR / SALAH")
jawaban = QLabel("JAWABANNYA")


""" UNTUK GRUP BUTTONNYA RADIO """
RadioGroupButton = QButtonGroup()
RadioGroupButton.addButton(rbtn_1)
RadioGroupButton.addButton(rbtn_2)
RadioGroupButton.addButton(rbtn_3)
RadioGroupButton.addButton(rbtn_4)


""" TAMPILAN DALAM ANSWER GRUP BOX """
answer_Vline = QVBoxLayout()
answer_Vline.addWidget(benar_salah, alignment=Qt.AlignLeft)
answer_Vline.addWidget(jawaban, alignment=Qt.AlignHCenter)
AnswerGroupBox.setLayout(answer_Vline)


""" TAMPILAN DALAM RADIO GRUP BOX """
garisH = QHBoxLayout()
garisV1 = QVBoxLayout()
garisV2 = QVBoxLayout()
garisV1.addWidget(rbtn_1)
garisV1.addWidget(rbtn_2)
garisV2.addWidget(rbtn_3)
garisV2.addWidget(rbtn_4)
garisH.addLayout(garisV1)
garisH.addLayout(garisV2)
RadioGroupBox.setLayout(garisH)


""" MENAMPILKAN / MENYEMBUNYIKAN """
RadioGroupBox.show()
AnswerGroupBox.hide()


""" TAMPILAN UNTUK JENDELANYA """
V_utama = QVBoxLayout()
V_utama.addWidget(pertanyaan, alignment=Qt.AlignHCenter)
V_utama.addWidget(RadioGroupBox, alignment=Qt.AlignHCenter)
V_utama.addWidget(AnswerGroupBox)
V_utama.addWidget(tombol, alignment=Qt.AlignHCenter)
jendela.setLayout(V_utama)


""" KUMPULAN FUNGSI """
def tunjukkan_hasil():
    """ MENAMPILKAN / MENYEMBUNYIKAN """
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    tombol.setText("PERTANYAAN SELANJUTNYA")


def tunjukkan_pertanyaan():
    """ MENAMPILKAN / MENYEMBUNYIKAN """
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    tombol.setText("JAWAB")
    """ RESET TOMBOL RADIO """
    RadioGroupButton.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroupButton.setExclusive(True)


""" MENAMPILKAN PERTANYAAN """
LIST_TOMBOL = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def tanya(tanya):
    shuffle(LIST_TOMBOL) ## acak jawaban
    LIST_TOMBOL[0].setText(tanya.benar)
    LIST_TOMBOL[1].setText(tanya.salah1)
    LIST_TOMBOL[2].setText(tanya.salah2)
    LIST_TOMBOL[3].setText(tanya.salah3)
    pertanyaan.setText(tanya.tanyaan)
    jawaban.setText(tanya.benar)
    tunjukkan_pertanyaan()


""" MENAMPILKAN PERTANYAAN BERIKUTNYA """
#jendela.pertanyaan_sekarang = -1
jendela.total_pertanyaan = 0
jendela.total_benar = 0
def next_question():
    #jendela.pertanyaan_sekarang += 1
    #if jendela.pertanyaan_sekarang >= len(LIST_TANYA):
    #   jendela.pertanyaan_sekarang = 0
    jendela.total_pertanyaan += 1
    pertanyaan_sekarang = randint(0, len(LIST_TANYA) - 1)
    tanya(LIST_TANYA[pertanyaan_sekarang])


def tampil_hasil(hasil):
    benar_salah.setText(hasil)
    tunjukkan_hasil()

def periksa_jawaban():
    if LIST_TOMBOL[0].isChecked() :
        jendela.total_benar += 1
        tampil_hasil("BENAR")
    else:
        tampil_hasil("SALAH")
    print("total pertanyaan:", jendela.total_pertanyaan)
    print("total jawaban benar:", jendela.total_benar)
    print("rating:", round((jendela.total_benar/jendela.total_pertanyaan)*100, 2), "%")

def periksa_jawaban():
    if LIST_TOMBOL[0].isChecked() :
        tampil_hasil("BENAR")
    else:
        tampil_hasil("SALAH")


def klik_ok():
    if tombol.text() == "JAWAB":
        periksa_jawaban()
    else:
        next_question()
   
""" EVENT HANDLER """
next_question()
tombol.clicked.connect(klik_ok)


jendela.show()
aplikasi.exec()

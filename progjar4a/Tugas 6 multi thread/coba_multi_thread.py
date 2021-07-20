from file_client_cli import remote_get
import time
import datetime
import threading
import socket


def kirim_pokiii():
    texec = dict()
    file = 'pokijan.jpg'

    waktu_awal = datetime.datetime.now()

    for n in range(100):
        print(f"mengirim {n}")
        texec[n] = threading.Thread(target=remote_get, args=(file,))
        texec[n].start()

    for n in range(100):
        texec[n].join()

    waktu_akhir = datetime.datetime.now()

    selisih = waktu_akhir - waktu_awal
    print(
        f"Total waktu yang dibutuhkan adalah {selisih} detik. Dari {waktu_awal} sampai {waktu_akhir}")


if __name__ == '__main__':
    kirim_pokiii()

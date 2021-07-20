from library import download_gambar, get_url_list, kirim_gambar
import time
import datetime
import threading


def kirim_server():
    texec = dict()
    urls = get_url_list()
    temp = 0
    catat_mulai = datetime.datetime.now()
    for n in urls:
        download_gambar(urls[n], n)
        print(f"mendownload {urls[n]}")
        waktu = time.time()

        UDP_IP_ADDRESS = "192.168.122.145"
        UDP_IP_ADDRESS2 = "192.168.122.83"
        PORT = 321
        if temp == 0:
            texec[n] = threading.Thread(
                target=kirim_gambar, args=(UDP_IP_ADDRESS, PORT, f"{n}.jpg"))
            print('ke server a')
            temp = temp + 1
        elif temp == 1:
            print('ke server b')
            texec[n] = threading.Thread(target=kirim_gambar, args=(
                UDP_IP_ADDRESS2, PORT, f"{n}.jpg"))
        texec[n].start()

    # kembali ke main thread
    for n in urls:
        texec[n].join()

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_mulai
    print(
        f"Waktu total yang dibutuhkan adalah {selesai} detik, dari {catat_mulai} sampai {catat_akhir}")


# fungsi download_gambar dijalankan secara multithreading
if __name__ == '__main__':
    kirim_server()

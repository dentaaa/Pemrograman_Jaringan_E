from library import download_gambar, get_url_list, kirim_gambar
import time
import datetime
from multiprocessing import Process, Pool


def kirim_server():
    texec = dict()
    urls = get_url_list()
    temp = 0
    status_task = dict()
    task_pool = Pool(processes=15)
    catat_awal = datetime.datetime.now()
    for n in urls:
        download_gambar(urls[n], n)
        print(f"mendownload {urls[n]}")
        UDP_IP_ADDRESS = "192.168.122.145"
        UDP_IP_ADDRESS2 = "192.168.122.83"
        PORT = 321
        if temp == 0:
            texec[n] = task_pool.apply_async(
                func=kirim_gambar, args=(UDP_IP_ADDRESS, PORT, f"{n}.jpg"))
            print('ke server a')
            temp = temp + 1
        elif temp == 1:
            print('ke server b')
            texec[n] = task_pool.apply_async(
                func=kirim_gambar, args=(UDP_IP_ADDRESS2, PORT, f"{n}.jpg"))

    for n in urls:
        status_task[n] = texec[n].get(timeout=10)

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(
        f"Total waktu yang dibutuhkan adalah {selesai} detik, dari {catat_awal} sampai {catat_akhir}")
    print("status TASK")
    print(status_task)


# fungsi download_gambar dijalankan secara multi process
if __name__ == '__main__':
    kirim_server()

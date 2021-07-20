import logging
import requests
import socket
import os
import time
import datetime


def get_url_list():
    urls = dict()
    # urls['bumi']='https://idearocketanimation.com/wp-content/uploads/2017/04/foundergif.gif'
    urls['anya'] = 'https://cdn1-production-images-kly.akamaized.net/SMUXOy5X_uQ7UP8cZW8KpKu0LaE=/640x853/smart/filters:quality(75):strip_icc():format(jpeg)/kly-media-production/medias/3376741/original/017025200_1613355753-Anya_Geraldine_0.jpg'
    # urls['lucuu']='https://i.pinimg.com/originals/01/fb/2c/01fb2cb2cf0855514cf1df69f46acda8.gif'
    urls['uus'] = 'https://disk.mediaindonesia.com/thumbs/1800x1200/news/2020/09/053c9ca81f962980f0b888fc578737ed.JPG'
    return urls


def download_gambar(url=None, tuliskefile='image'):
    waktu_mulai = datetime.datetime.now()
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png'] = 'png'
    tipe['image/jpg'] = 'jpg'
    tipe['image/gif'] = 'gif'
    tipe['image/jpeg'] = 'jpg'
    tipe['application/zip'] = 'jpg'
    tipe['video/quicktime'] = 'mov'
    tipe['audio/mpeg'] = 'mp3'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        if (tuliskefile):
            fp = open(f"{tuliskefile}.{ekstensi}", "wb")
            fp.write(ff.content)
            fp.close()
        waktu_process = datetime.datetime.now() - waktu_mulai
        waktu_selesai = datetime.datetime.now()
        logging.warning(
            f"writing {tuliskefile}.{ekstensi} dalam waktu {waktu_process} {waktu_mulai} s/d {waktu_selesai}")
        return waktu_process
    else:
        return False


def kirim_gambar(IP_ADDRESS, PORT, filename):
    print(IP_ADDRESS, PORT, filename)
    ukuran = os.stat(filename).st_size
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    fp = open(filename, 'rb')
    i = fp.read()
    terkirim = 0
    for n in i:
        i_bytes = bytes([n])
        clientSock.sendto(i_bytes, (IP_ADDRESS, PORT))
        terkirim = terkirim+1


if __name__ == '__main__':
    # check fungsi
    k = download_gambar('https://cdn1-production-images-kly.akamaized.net/SMUXOy5X_uQ7UP8cZW8KpKu0LaE=/640x853/smart/filters:quality(75):strip_icc():format(jpeg)/kly-media-production/medias/3376741/original/017025200_1613355753-Anya_Geraldine_0.jpg')
    print(k)

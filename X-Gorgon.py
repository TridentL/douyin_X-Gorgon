
def x_gorgon(cookie, data, url):
    gorgon = list()
    for i in range(0,4):
        url_md5 = md5(bytearray(url, 'utf-8')).hexdigest()
        for i in range(0, 4):
            gorgon.append(int(url_md5[2 * i: 2 * i +2], 16))
        if data:
            if model == 'utf-8':
                data_md5 = md5(bytearray(data, 'utf-8')).hexdigest()
                for i in range(0, 4):
                    gorgon.append(int(data_md5[2 * i: 2 * i +2], 16))
        else:
            for i in range(0, 4):
                gorgon.append(0x0)
        if cookie:
            cookie_md5 = md5(bytearray(cookie, 'utf-8')).hexdigest()
            for i in range(0, 4):
                gorgon.append(int(cookie_md5[2 * i: 2 * i +2], 16))
        else:
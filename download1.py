### CMD: pip install requests
import requests
import re

link = 'http://www.cante.com.br/baixar.php?id='
path = '/Cante/musicas/'

######################################################
def get_filename_from_cd(cd):
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]
######################################################

for i in range(8600, 8610):
    try:
        url = link + str(i)
        request = requests.get(url)
        if request.status_code == 200:
            print("Download => " + url)
            r = requests.get(url, allow_redirects=True)
            filename = path + str(get_filename_from_cd(r.headers.get('content-disposition'))).replace('"','').replace('/','_')
            open(filename, 'wb').write(r.content)

        else:
            print("Url (" + url + ") returned response code: {code}".format(code=request.status_code))
    except ConnectionError:
        print('Url does not exist')

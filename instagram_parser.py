import pprint
import json
from bs4 import BeautifulSoup as bs
from selenium import webdriver

browser = webdriver.Chrome()
usernames = ['jojo_nicholas', 'synd.yhn_', 'dtya__', 'fwibisono87', 'keikoaaliya', 'budi1405', '_hadipratama768', 'funuralfahmi', 'k.i.r.e.b.y', 'tharrasabe', 'marta_dewi', 'alifyandra', 'ikmalmuhtadi', 'raihanmaulaya', 'uchiml', 'althof_rr', 'rafiisml_', 'riswandaali', 'astriddiany', 'raihan.r.r', 'aayafaizah', 'dennyoctavian1', 'eriiiikaa', 'nrhfztn_nisa', 'raihanandr', 'weninglc', 'krmh10_', 'rasyidmi', 'nabiel.mn', 'farhansbbs', 'dinarstyrn', 'aryaputra213', 'ryandamy', '_drakoz', 'achmad.afriza',
             'fadhilahumairah', 'fadlia68', 'aflah_alifu', 'gilangcy', 'marshaprwr', 'aimamf', 'cornelita_', 'aldinfitrah', 'jeremyanj', 'naltoon', 'faishol.ami27', 'karina.aulia', 'fauziridwan1709', 'aryaseputra', 'adimaspph', 'whoisthoriq', 'ferikahafshahz', 'husnafarah', 'rafliamardito', 'viviidoran', 'naufalpraam', 'mulatua_', 'prajnaprasetya', '_wuts', 'thyempress', 'ferdifdi', 'qonitaktshhn', 'marthindaniels', 'naufal_rizki', 'fiqar_aditya', 'cos.nol', 'natsyz', 'widyantonugroho', 'aditmk', 'stevensim226']
urls = ["http://www.instagram.com/"+username for username in usernames]


def total_followers(usernames):
    total = 0
    for url in urls:
        browser.get(url)
        # Pagelength = browser.execute_script(
        #     "window.scrollTo(0, document.body.scrollHeight);")
        data = bs(browser.page_source, 'html.parser')
        source = data.find('body').find('span').find('section').find(
            'main').find('div').find('ul').findAll('li')
        # , attrs={'class': 'g47SY lOXF2'}).text
        followers = int(source[1].text.split()[0].replace(',', ''))
        total += followers
    return total


print(total_followers(usernames))
browser.quit
# <span class="g47SY lOXF2" title="790">790</span>
# <a class = " _81NM2" href = "/jojo_nicholas/followers/" > <span class = "g47SY lOXF2" title = "790" > 790 < /span > followers < /a >

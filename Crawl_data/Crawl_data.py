from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
class Crawl_data:
    """"
        Class Crawl_data được xây dựng để crawl data với
        tham số đầu vào là các thư viện cần thiết  đường link dẫn và
        đầu ra là mảng data lưu trữ dữ liệu đã được crawl từ link dẫn

        Class bao gồm các hàm thành phần như set_link, access_link(truy cập link), get_source(lấy open source của page)
        và phần process_data(crawl data và lưu vào mảng kết quả )
    """
    def __init__(self,url=''):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.soup = BeautifulSoup()
        self.url = url
        self.data = []
    def set_url(self,url):
        self.url = url
    def access_link(self):
        self.driver.get(self.url)
    def get_sourcepage(self):
        self.access_link()
        self.soup = BeautifulSoup(self.driver.page_source)
    def process_data(self):

        #find link href
        self.get_sourcepage()
        #print(self.soup.prettify())
        link_new = self.soup.find_all('div', {"class": "ct_title"})
        list_new = []
        u = 'https://alonhadat.com.vn/'
        for link in link_new:
            if link.find('a',{"class":"vip"})!= None:
                list_new.append(u+link.find('a',{"class":"vip"}).get("href"))
            else:
                #print(link)
                list_new.append(u+link.find('a').get("href"))

        #crawl data
        for i in list_new:
            self.set_url()
            self.get_sourcepage()
            #print(self.soup.prettify())
            data_dic = {}
            x_1 = self.soup.find('div',{"class":"address"}).find('span',{"class":"value"}).get_text()
            x_1 = x_1.split(", ")
            data_dic['quan'] = x_1[len(x_1)-2]

            x_2 = self.soup.find('div',{"class":"infor"}).find_all('td')
            for id in range(len(x_2)):
                if (x_2[id].get_text()=='Loại BDS'):
                    data_dic['loai_bds'] = x_2[id+1].get_text()
                if (x_2[id].get_text()=='Pháp lý'):
                    data_dic['phap_ly'] = x_2[id+1].get_text()
                if (x_2[id].get_text()=='Số lầu'):
                    data_dic['so_lau'] = x_2[id+1].get_text()
                if (x_2[id].get_text()=='Số phòng ngủ'):
                    data_dic['so_phong'] = x_2[id+1].get_text()
                if (x_2[id].get_text()=='Chiều dài'):
                    data_dic['dai'] = x_2[id+1].get_text()
                if (x_2[id].get_text()=='Chiều ngang'):
                    data_dic['rong'] = x_2[id+1].get_text()

            x_3 = self.soup.find('span',{"class":"price"}).find('span',{"class":"value"})
            data_dic['gia']=x_3.get_text()

            x_4 = self.soup.find('span', {"class": "square"}).find('span', {"class": "value"})
            data_dic['dien_tich'] = x_4.get_text()
            self.data.append(data_dic)
        #print(len(self.da))









from Crawl_data import Crawl_data
from Database import Database

def main():
    crawl = Crawl_data()
    #return
    ur = 'https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/2/ho-chi-minh/'
    crawl.set_url('https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/2/ho-chi-minh.html')
    crawl.process_data()
    for i in range(501,1001):
     print(i)
     url = ur+'trang--'+str(i)+'.html'
     crawl.set_url(url)
     crawl.process_data()

    data = crawl.data
    database = Database()
    database.creat_table()
    database.set_data(data)
    database.excute()
if __name__ == '__main__':
    main()

import mysql.connector

class Database:
    """
        Class Database có chức năng chính là lưu trữ xuống MySql với inout đầu vào là thư viện kết nối python với hệ thống MySql của mình
        và dữ liệu cần lưu trữ.
        Class bao gồm các hàm gồm thành phần như set_data,creat_table(tạo bảng dữ liệu trong MySql),
        insert_data(chèn dữ liệu vào bảng), process(thực thi việc lưu trữ)
    """
    def __init__(self,data = []):
        self.db = mysql.connector.connect(user='root', password='kimthoa165', host='127.0.0.1', database='DBLP')
        self.data = data
    def creat_table(self):
        code_1 = "CREATE TABLE `DBLP`.`House_price` (`Quận` VARCHAR(500) NULL," \
                 "`Loại_BDS` VARCHAR(100) NULL, " \
                 "`Pháp_lý` VARCHAR(100) NULL, " \
                 "`Số_tầng` VARCHAR(5) NULL, " \
                 "`Số_phòng` VARCHAR(5) NULL," \
                 "`Diện_tích` VARCHAR(20) NULL, " \
                 "`Dài` VARCHAR(20) NULL, " \
                 "`Rộng` VARCHAR(20), " \
                 "`Giá` VARCHAR(20) NOT NULL)"
        mycursor = self.db.cursor()
        mycursor.execute(code_1)
    def insert_data(self,quan,loai_bds,phap_ly,so_lau,so_phong,dien_tich,dai,rong,gia):
        sql = "INSERT INTO House_Price(Quận,Loại_BDS,Pháp_lý,Số_tầng,Số_phòng,Diện_tích,Dài,Rộng,Giá)" \
              " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (quan,loai_bds,phap_ly,so_lau,so_phong,dien_tich,dai,rong,gia)

        #print(val)
        cursor = self.db.cursor()
        cursor.execute(sql, val)
        self.db.commit()
    def set_data(self,data):
        self.data = data
    def excute(self):
        print(len(self.data))
        for item in self.data:
            self.insert_data(item['quan'],item['loai_bds'],item['phap_ly'],item['so_lau'],item['so_phong'],item['dien_tich'],item['dai'],item['rong'],item['gia'])

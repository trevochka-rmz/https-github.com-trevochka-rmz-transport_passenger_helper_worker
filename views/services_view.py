import flet as ft
from data import dataUsers
import pymysql
from my_config import host, user, password, db_name,id

count_podushka = 0
count_plaits = 0
count_fork = 0
count_soud= 0
count_telephone = 0
count_provodnik = 0
def ServicesView(router):
    order = []
    try:
        connection = pymysql.connect(
            host=host, 
            user = user,
            password=password,
            database= db_name,
            cursorclass=pymysql.cursors.DictCursor)
        print("connect successfully")
    except Exception as ex:
        print("Connection refused...")
        print(ex)
    try:           
        with connection.cursor() as cursor:
            create_table_quare = f"SELECT order_services.id_user, services.name, services.price, order_services.counts FROM `order_services` INNER JOIN `services` ON order_services.id_services = services.id_services; " 
            cursor.execute(create_table_quare)
            row = cursor.fetchall()
            for i in row:
                order.append(i)
            print(order)
            print("#"*20)
    finally:
        connection.commit()
        connection.close()
    def items():
        item = []
        for i in order:
            item.append(     
                ft.Row(
                [   
                    ft.Text(f"ID пользователя - {i['id_user']},", size=20), 
                    ft.Text(f"Название - {i['name']},", size=20), 
                    ft.Text(f"Цена - {i['price']},", size=20), 
                    ft.Text(f"Количество - {i['counts']},", size=20), 
                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ))
        return item
    content = ft.Column(          
            [
                ft.Row(
                [
                    ft.Text("Дополнительные услуги", size=30), 
                    ft.IconButton( icon = ft.icons.ROOM_SERVICE,icon_size=30),
                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Column(controls=items(), alignment=ft.MainAxisAlignment.CENTER)  

            ]
        )
    
    
    
    
    
    
    
    
    
    return content
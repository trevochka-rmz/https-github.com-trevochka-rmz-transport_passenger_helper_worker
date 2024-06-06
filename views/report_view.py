import flet as ft
from data import dataUsers
import pymysql
from my_config import host, user, password, db_name,id

def ReportView(router):
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
            create_table_quare = f"SELECT * FROM `user_helper`; " 
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
                    ft.Text(f"Отзыв - {i['report']},", size=20),  
                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ))
        return item
    content = ft.Column(          
            [
                ft.Row(
                [
                    ft.Text("Оставить отзыв/Пожаловаться", size=30), 
                    ft.IconButton( icon = ft.icons.REPORT,icon_size=30),
                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
                ft.Column(controls=items(), alignment=ft.MainAxisAlignment.CENTER)  
            ],alignment=ft.MainAxisAlignment.CENTER
        )
    
    
    
    
    
    
    
    
    
    return content
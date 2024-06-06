import flet as ft
from data import dataUsers
import pymysql
from my_config import host, user, password, db_name,id

def ReportView(router):
    report = ft.TextField(label="Здесь вы можете написать отзыв или пожаловаться, после можете отправить для руководителей", min_lines=10, max_lines=10,width=800)
    
    def get_report(e):
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
                create_table_quare = f"UPDATE `user_helper` SET report = '{report.value}'  WHERE id_user = {id};"
                cursor.execute(create_table_quare)
                print("ok")
        finally:
            connection.commit()
            connection.close()
        dataUsers["report"].append(report.value)
    send_button = ft.ElevatedButton("Отправить")
    send_button.on_click = get_report
    content = ft.Column(          
            [
                ft.Row(
                [
                    ft.Text("Оставить отзыв/Пожаловаться", size=30), 
                    ft.IconButton( icon = ft.icons.REPORT,icon_size=30),
                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
                ft.Row(
                    [
                        report
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        send_button
                    ],alignment=ft.MainAxisAlignment.CENTER
                ),

            ],alignment=ft.MainAxisAlignment.CENTER
        )
    
    
    
    
    
    
    
    
    
    return content
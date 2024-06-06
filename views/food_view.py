
import flet as ft
import sqlite3
from data import dataUsers
import pymysql
from my_config import host, user, password, db_name,id

count_tea = 0
count_cola = 0
count_mors = 0
count_salat = 0
count_soup = 0
count_sandwich = 0
def FoodView(router):
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
            create_table_quare = f"SELECT order_food.id_user, food_drinks.name,food_drinks.price, order_food.counts FROM `order_food` INNER JOIN `food_drinks` ON order_food.id_food = food_drinks.id_food; " 
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
                    ft.Text("Еда и напитки", size=30), 
                    ft.IconButton( icon = ft.icons.FOOD_BANK,icon_size=30),
                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Column(controls=items(), alignment=ft.MainAxisAlignment.CENTER)            

            ]
        )
    

    
    return content

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
    def food1(e):
        global count_tea
        count_tea+=1
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
                create_table_quare = f"INSERT INTO `order_food` (id_food,id_user,counts) VALUES (0,{id},{count_tea});" 
                cursor.execute(create_table_quare)
                print("ok")
        finally:
            connection.commit()
            connection.close()
        dataUsers["food_drinks"]["Чай"]["count"] = count_tea

    def food2(e):
        global count_cola
        count_cola+=1
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
                create_table_quare = f"INSERT INTO `order_food` (id_food,id_user,counts) VALUES (1,{id},{count_cola});" 
                cursor.execute(create_table_quare)
                print("ok")
        finally:
            connection.commit()
            connection.close()
        dataUsers["food_drinks"]["Кола"]["count"] = count_cola
        

    def food3(e):
        global count_mors
        count_mors+=1
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
                create_table_quare = f"INSERT INTO `order_food` (id_food,id_user,counts) VALUES (2,{id},{count_mors});" 
                cursor.execute(create_table_quare)
        finally:
            connection.commit()
            connection.close()
        dataUsers["food_drinks"]["Морс"]["count"] = count_mors

    def food4(e):
        global count_sandwich
        count_sandwich+=1
        try:
            connection = pymysql.connect(
                host=host, 
                user = user,
                password=password,
                database= db_name,
                cursorclass=pymysql.cursors.DictCursor)

        except Exception as ex:
            print("Connection refused...")
            print(ex)
        try:
            
            with connection.cursor() as cursor:
                create_table_quare = f"INSERT INTO `order_food` (id_food,id_user,counts) VALUES (5,{id},{count_sandwich});" 
                cursor.execute(create_table_quare)
        finally:
            connection.commit()
            connection.close()
        dataUsers["food_drinks"]["Сэндвич"]["count"] = count_sandwich

    def food5(e):
        global count_soup
        count_soup+=1
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
                create_table_quare = f"INSERT INTO `order_food` (id_food,id_user,counts) VALUES (4,{id},{count_soup});" 
                cursor.execute(create_table_quare)
        finally:
            connection.commit()
            connection.close()
        dataUsers["food_drinks"]["Суп"]["count"] = count_soup

    def food6(e):
        global count_salat
        count_salat+=1
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
                create_table_quare = f"INSERT INTO `order_food` (id_food,id_user,counts) VALUES (3,{id},{count_salat});" 
                cursor.execute(create_table_quare)
        finally:
            connection.commit()
            connection.close()
        dataUsers["food_drinks"]["Салат"]["count"] = count_salat

        
    send_button = ft.ElevatedButton("Заказать")
    send_button2 = ft.ElevatedButton("Заказать")
    send_button3 = ft.ElevatedButton("Заказать")
    send_button4 = ft.ElevatedButton("Заказать")
    send_button5 = ft.ElevatedButton("Заказать")
    send_button6 = ft.ElevatedButton("Заказать")
    send_button.on_click = food1
    send_button2.on_click = food2
    send_button3.on_click = food3
    send_button4.on_click = food4
    send_button5.on_click = food5
    send_button6.on_click = food6
    content = ft.Column(          
            [
                ft.Row(
                [
                    ft.Text("Еда и напитки", size=30), 
                    ft.IconButton( icon = ft.icons.FOOD_BANK,icon_size=30),
                    ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),
                ft.Row([
                    ft.Column(
                    [
                        ft.Image(src=f"/tea.jpg", width=200, border_radius=100),
                        ft.Text("Чай"),
                        ft.Text("Цена: 50рублей"),
                        send_button

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Column(
                    [
                        ft.Image(src=f"/cola.jpg", width=200, border_radius=100),
                        ft.Text("Кола"),
                        ft.Text("Цена: 150рублей"),
                        send_button2

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Column(
                    [
                        ft.Image(src=f"/mors.jpg", width=200, border_radius=100),
                        ft.Text("Морс"),
                        ft.Text("Цена: 50рублей"),
                        send_button3

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing = 70

                ) ,
            
                ft.Row([
                    ft.Column(
                    [
                        ft.Image(src=f"/sandwich.jpg", width=200, border_radius=100),
                        ft.Text("Сэндвич"),
                        ft.Text("Цена: 150рублей"),
                        send_button4

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Column(
                    [
                        ft.Image(src=f"/soup.jpg", width=200, border_radius=100),
                        ft.Text("Суп"),
                        ft.Text("Цена: 250рублей"),
                        send_button5

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Column(
                    [
                        ft.Image(src=f"/salat.jpg", width=200, border_radius=100),
                        ft.Text("Салат"),
                        ft.Text("Цена: 250рублей"),
                        send_button6

                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                ], alignment=ft.MainAxisAlignment.CENTER, spacing = 70

                ) ,

            ]
        )
    

    
    return content
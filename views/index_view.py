from typing import Union
import flet as ft
from views.Router import Router, DataStrategyEnum
# from State import global_state, State
import sqlite3
import random

def IndexView(router_data: Union[Router, str, None] = None):
    id = random.randint(1,100) 
    def food_go(e: ft.ControlEvent):
        e.page.go('/food')
    def services_go(e: ft.ControlEvent):
        e.page.go('/services')
        e.page.go('/schedule')
    def report_go(e: ft.ControlEvent):
        e.page.go('/report')


    food_drinks_button = ft.IconButton( icon = ft.icons.FOOD_BANK,icon_size=170)
    services_button = ft.IconButton( icon = ft.icons.ROOM_SERVICE,icon_size=170)
    report_button = ft.IconButton( icon = ft.icons.REPORT,icon_size=170)


    
    food_drinks_button.on_click = food_go
    services_button.on_click = services_go
    report_button.on_click = report_go


    content = ft.Column(
            [
                ft.Row(
                [
                    ft.Text(
                        "Просмотр заказов, услугов и отзывов",
                        size=30),
                ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),

            
            ft.Row(
            [
                food_drinks_button,
                services_button,
                report_button
            ],
            alignment=ft.MainAxisAlignment.CENTER, spacing = 70,height=350
            ),
            
        ]
        )
    
    return content



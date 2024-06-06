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
    def schedule_go(e: ft.ControlEvent):
        e.page.go('/schedule')
    def report_go(e: ft.ControlEvent):
        e.page.go('/report')
    def weather_go(e: ft.ControlEvent):
        e.page.go('/weather')
    def setup_go(e: ft.ControlEvent):
        e.page.go('/settings')


    text_field = ft.TextField()
    food_drinks_button = ft.IconButton( icon = ft.icons.FOOD_BANK,icon_size=170)
    services_button = ft.IconButton( icon = ft.icons.ROOM_SERVICE,icon_size=170)
    schedule_button = ft.IconButton( icon = ft.icons.SCHEDULE,icon_size=170)
    report_button = ft.IconButton( icon = ft.icons.REPORT,icon_size=170)
    weather_button = ft.IconButton( icon = ft.icons.CLOUD,icon_size=170)
    setup_button = ft.IconButton( icon = ft.icons.SETTINGS,icon_size=170)

    
    food_drinks_button.on_click = food_go
    services_button.on_click = services_go
    schedule_button.on_click = schedule_go
    report_button.on_click = report_go
    weather_button.on_click = weather_go
    setup_button.on_click = setup_go

    content = ft.Column(
            [
                ft.Row(
                [
                    ft.Text(
                        "Здесь вы можете выбрать любую услугу и мы сразу уведомим работника",
                        size=30),
                ], 
                alignment=ft.MainAxisAlignment.CENTER
            ),

            
            ft.Row(
            [
                food_drinks_button,
                services_button,
                schedule_button
            ],
            alignment=ft.MainAxisAlignment.CENTER, spacing = 70
            ),
            ft.Row(
            [
                report_button,
                weather_button,
                setup_button
            ],
            alignment=ft.MainAxisAlignment.CENTER , spacing = 70
            )
            
        ]
        )
    
    return content



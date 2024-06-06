import flet as ft
import pymysql.cursors
from views.routes import router
from user_controls.app_bar import NavBar
# import sqlite3
import pymysql
from my_config import host, user, password, db_name,id


def main(page: ft.Page):
    
    page.theme_mode = "dark"
    page.appbar = NavBar(page)
    page.on_route_change = router.route_change
    router.page = page
    page.add(
        router.body
    )
    page.go('/')

ft.app(target=main, assets_dir="assets")
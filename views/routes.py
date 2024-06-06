from views.Router import Router, DataStrategyEnum
from views.index_view import IndexView
from views.settings_view import SettingsView
# from views.data_view import DataView
from views.food_view import FoodView
from views.services_view import ServicesView
from views.report_view import ReportView


router = Router(DataStrategyEnum.QUERY)

router.routes = {
  "/": IndexView,
  "/settings": SettingsView,
  "/food": FoodView,
  "/services": ServicesView,
  "/report": ReportView,

}
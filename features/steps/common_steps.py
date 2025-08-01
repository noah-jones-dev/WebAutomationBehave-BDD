from behave import given, when, then
from framework.helpers.waits import Waits

@given("Open crayola main page")
def open_main_page(context):
    context.app.home_page.open()
    Waits.wait_for_ads(context.driver, 10) 
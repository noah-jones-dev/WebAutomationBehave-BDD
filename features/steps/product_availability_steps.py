from behave import given, when, then

@when("Navigate to the Crayola product page")
def navigate_to_crayola_product_page(context):
    context.app.home_page.menu_NV.navigate_to(["Products", "Crayons"])
    
@when("Select a product")
def select_product(context):
    context.app.crayons_page.products_section_LS.select_item("Retired Crayons")
    
@then("Verify product availability status is displayed")
def verify_product_availability(context):
    context.app.product_detail_page.where_to_buy_BTN.click()
    context.app.product_detail_page.modal_product_title_ST.verify.text_contains("Retired Crayons")
    context.app.product_detail_page.modal_product_availability_LS.verify.size_is_greater(0)
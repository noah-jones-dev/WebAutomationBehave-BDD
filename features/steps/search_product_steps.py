from behave import given, when, then

@when("Crayola search for {product}")
def search_for_product(context, product):
    context.app.home_page.search_TB.enter(product)

@then("Displays search results for {product}")
def verify_search_results(context, product):
    context.app.product_listing_page.search_results_TB.verify.text_contains(product)
    
@when("Select a {product} from the search results")
def select_product_from_results(context, product):
    context.app.product_listing_page.products_section_LS.select_item(product)
    
@then("Verify {product} detail displays")
def verify_product_detail(context, product):
    context.app.product_detail_page.product_title_ST.verify.text_contains(product)
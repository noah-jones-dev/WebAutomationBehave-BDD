from behave import given, when, then

@when("Select language {language}")
def select_language(context, language):
    context.app.home_page.language_selector_LS.select_item(language)

@then("Verify text is translated to {language}")
def verify_language_translated(context, language):
    if (language == "English (United Kingdom)"):
        context.app.home_page.main_header_tag_ST.verify.text_is("Creativity Starts Here")
        context.app.home_page.main_header_ST.verify.text_is("A New Creative Experience is Coming!")
        context.app.home_page.main_header_description_ST.verify.text_is("More inspiration is coming soon—now with an easier way to explore it all! Get ready for more free colouring pages, new craft ideas, and engaging activities, all in one convenient place. Stay tuned!")
    elif (language == "English (Australia)"):
        context.app.home_page.main_header_tag_ST.verify.text_is("Creativity Starts Here")
        context.app.home_page.main_header_ST.verify.text_is("Art Supplies & Toys")
        context.app.home_page.main_header_description_ST.verify.text_is("Browse creative innovation with Crayola, where every product sparks imagination and creative moments.")
    elif (language == "English (United States)"):
        context.app.home_page.main_header_tag_ST.verify.text_is("Explore Our New Website")
        context.app.home_page.main_header_ST.verify.text_is("The Crayola You Love, Now Easier to Explore!")
        context.app.home_page.main_header_description_ST.verify.text_is("Discover more inspiration than ever. Explore an expanded collection of Crayola classics and new favorites. Enjoy a simple way to browse it all!")
    elif (language == "Spanish (Mexico)"):
        context.app.home_page.main_header_tag_ST.verify.text_is("Lápices de color")
        context.app.home_page.main_header_ST.verify.text_is("Diseñados para Crear")
        context.app.home_page.main_header_description_ST.verify.text_is("Con textura cremosa, puntas fuertes y una amplia gama de colores.")
    elif (language == "Italian (Italy)"):
        context.app.home_page.main_header_tag_ST.verify.text_is("La creatività inizia da qui!")
        context.app.home_page.main_header_ST.verify.text_is("Una nuova esperienza creativa è in arrivo!")
        context.app.home_page.main_header_description_ST.verify.text_is("Sta per arrivare una nuova impostazione creativa per ispirarti e darti gli strumenti per esprimere al meglio la tua creatività! Pagine da colorare gratuite, nuove idee per lavoretti creativi e attività coinvolgenti, tutto raccolto in un unico spazio intuitivo. Resta sintonizzato!")
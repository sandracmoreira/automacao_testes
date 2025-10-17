from pages.highlights_page import HighlightsPage

def test_highlights_page_load_and_has_items(driver):
    page = HighlightsPage(driver)
    page.open()
    assert "Destaques" in page.page_title()
    assert page.has_highlights(), "Nenhum destaque foi encontrado na página."
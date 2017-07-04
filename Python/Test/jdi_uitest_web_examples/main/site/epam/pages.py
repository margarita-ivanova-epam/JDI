from JDI.web.selenium.elements.api_interact.find_element_by import By
from JDI.web.selenium.elements.base.element import Element
from JDI.web.selenium.elements.common.label import Label
from JDI.web.selenium.elements.composite.web_page import WebPage
from Test.jdi_uitest_web_examples.main.site.epam.add_cv_form import AddCVForm


class CareerPage(WebPage):
    def __init__(self, url, title):
        super(CareerPage, self).__init__(url=url, title=title)

    job_filter = JobFilter(By.css(".job-search-form-ui"))
    list_menu = JDIElements(By.css(".tile-menu>li>a"), Label)


class HomePage(WebPage):
    def __init__(self, url, title):
        super(HomePage, self).__init__(url=url, title=title)


class JobDescriptionPage(WebPage):
    def __init__(self, url, title):
        super(JobDescriptionPage, self).__init__(url=url, title=title)

    add_cv_form = AddCVForm(By.css(".form-constructor"))
    captcha = Element(By.id("captcha-input"))


class JobListingPage(WebPage):
    def __init__(self, url, title):
        super(JobListingPage, self).__init__(url=url, title=title)

        jobs_list = Table(root=By.css(".search-result-list"),
                          row=By.xpath(".//li[%s]//div"),
                          column=By.xpath(".//li//div[%s]"),
                          header={"name", "category", "location", "apply"})

        jods_list_entity = EntityTable(root=By.css(".search-result-list"),
                                       row=By.xpath(".//li[%s]//div"),
                                       column=By.xpath(".//li//div[%s]"),
                                       header={"name", "category", "location", "apply"},
                                       entity_class=JobRecord)


class ProductDevelopmentPage(WebPage):
    def __init__(self, url, title):
        super(ProductDevelopmentPage, self).__init__(url=url, title=title)

from page.commoditymanagement.main import Main


class TestCateGory:
    def setup(self):
        self.main=Main()
    def test_category_add(self):
        self.main.category.category_add()
from seleniumbase import BaseCase

class TestExample(BaseCase):

    def test_example(self):
        self.open('https://www.google.com')
        self.update_text('input[name=q]', 'SeleniumBase')
        self.click('input[name=btnI]')
        #self.assert_element("input[name='query'].md-search__input")
        self.assert_element("//div[@class='md-search' and @data-md-component='search']")


        # self.assert_text('SeleniumBase', "//div[@class='md-search' and @data-md-component='search']")
        # self.take_screenshot()

if __name__ == '__main__':
    TestExample.run_class_wide_tests()

# coding=utf-8
import os
from bs4 import BeautifulSoup


class HtmlCleaner:
    def __init__(self, soup):
        self.soup = soup

    def remove_all_attrs(self):
        # remove all attributes
        for tag in self.soup.find_all(True):
            tag.attrs = {}
        return self

    def remove_all_attrs_except(self):
        # remove all attributes except some tags
        whitelist = ['a', 'img']
        for tag in self.soup.find_all(True):
            if tag.name not in whitelist:
                tag.attrs = {}
        return self

    def remove_all_attrs_except_saving(self):
        # remove all attributes except some tags(only saving ['href','src'] attr)
        whitelist = ['a', 'img']
        for tag in self.soup.find_all(True):
            if tag.name not in whitelist:
                tag.attrs = {}
            else:
                attrs = dict(tag.attrs)
                for attr in attrs:
                    if attr not in ['src', 'href']:
                        del tag.attrs[attr]
        return self

    def unwrap_tagname(self):
        blacklist = ['basefont', 'font', 'span', 'b']
        for blacklisttag in blacklist:
            for tag in self.soup.find_all(blacklisttag):
                tag.unwrap()
        return self

    def remove_whitespace(self):
        soup_str = str(self.soup.currentTag)
        soup_str = soup_str.replace("\n", "")
        self.soup = BeautifulSoup(soup_str, "html.parser")
        return self

    def remove_empty_div(self):
        empty_tags = self.soup.find_all(lambda tag: tag.name == 'div' and not tag.contents and (
            tag.string is None or not tag.string.strip()))
        for empty_tag in empty_tags:
            empty_tag.extract()
        return self

    def merge_template(self):
        template_soup = BeautifulSoup(open("template.html", "r", encoding='utf8'),
                                      "html.parser", from_encoding='utf-8')
        src_body = self.soup.find('body')
        # print("src_body", src_body)
        # print("template_soup.body", template_soup.body)
        template_soup.body.replace_with(src_body)
        self.soup = template_soup
        # print("self.soup", self.soup)
        return self

    def remove_special_tag(self):
        special_tags = self.soup.find_all(
            lambda tag: tag.name.__contains__(':'))
        for special_tag in special_tags:
            special_tag.extract()
        return self


directory = os.listdir('./src')
# os.chdir('./docx2html')


# print(directory)
for file in directory:
    # print(os.getcwd())
    # print(file)

    src_file = os.path.join("./src/", file)
    # print(os.getcwd())  # 현재 디렉토리의
    # print(src_file)
    if os.path.isfile(src_file) and src_file.endswith(".htm"):
        soup = BeautifulSoup(open(src_file, "r", encoding='utf8'),
                             "html.parser", from_encoding='utf-8')

        clean_soup = HtmlCleaner(soup)
        clean_soup                              \
            .remove_all_attrs_except_saving()   \
            .unwrap_tagname()                   \
            .remove_whitespace()                \
            .remove_empty_div()                 \
            .merge_template()

        # clean_soup = _merge_template(_remove_empty_div(_remove_whitespace(_upwrap_tagname(
        #  _remove_all_attrs_except_saving(soup)))))

        dst_file = os.path.join("./dst/", file)
        print("변경파일", dst_file)
        with open(dst_file, "w", encoding='utf8') as file:
            file.write(clean_soup.soup.prettify())

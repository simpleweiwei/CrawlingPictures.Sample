import os
import xml.etree.ElementTree as ET  # Python 3.3以后，ElementTree 模块会自动寻找可用的 C 库来加快速度


# 处理XML应首选ElementTree：xml.etree.ElementTree模块提供了一个轻量级、Pythonic的API，同时还有一个高效的C加速器，因此与DOM方式相比，ET的速度更快，API使用更直接、方便，占用内存更小
"""
students.xml：
<students class="G2016">
    <student no="2009081097">
        <name>Hongten</name>
        <gender>M</gender>
        <age>22</age>
        <score subject="math">97</score>
        <score subject="chinese">90</score>
    </student>
    <student no="2009081098">
        <name>DuDu</name>
        <gender>W</gender>
        <age>23</age>
        <score subject="math">87</score>
        <score subject="chinese">96</score>
    </student>
    <student no="2009081099">
        <name>Sum</name>
        <gender>M</gender>
        <age>21</age>
        <score subject="math">64</score>
        <score subject="chinese">98</score>
    </student>
</students>
"""

def get_root(path):
    if os.path.exists(path):
        tree = ET.parse(path)
        return tree.getroot()
    else:
        print('the path [{}] dose not exist!'.format(path))


def get_element_tag(element):
    """return the element tag if the element is not None."""
    if element is not None:
        return element.tag
    else:
        print('the element is None!')


def get_element_attrib(element):
    """return the element attrib if the element is not None."""
    if element is not None:
        return element.attrib
    else:
        print('the element is None!')


def get_element_text(element):
    """return the text of the element."""
    if element is not None:
        return element.text
    else:
        print('the element is None!')


def get_element_children(element):
    """return the element children if the element is not None."""
    if element is not None:
        return [c for c in element]
    else:
        print('the element is None!')


def get_elements_tag(elements):
    """return the list of tags of element's tag"""
    if elements is not None:
        tags = []
        for e in elements:
            tags.append(e.tag)
        return tags
    else:
        print('the elements is None!')


def get_elements_attrib(elements):
    """return the list of attribs of element's attrib"""
    if elements is not None:
        attribs = []
        for a in elements:
            attribs.append(a.attrib)
        return attribs
    else:
        print('the elements is None!')


def get_elements_text(elements):
    """return the dict of element"""
    if elements is not None:
        text = []
        for t in elements:
            text.append(t.text)
        return dict(zip(get_elements_tag(elements), text))
    else:
        print('the elements is None!')


# 新建xml文件
def buildXmlFile():
    # 设置一个新节点，并设置其标签为root
    root = ET.Element("root")

    # 在root下新建两个子节点,设置其名称分别为sina和chinabyte
    sina = ET.SubElement(root, "sina")
    chinabyte = ET.SubElement(root, "chinabyte")

    # 在sina下新建两个子节点，设置其节点名称分别为number和first
    sina_number = ET.SubElement(sina, "number")
    sina_number.text = "1"
    sina_first = ET.SubElement(sina, "first")
    sina_first.text = "http://roll.tech.sina.com.cn/internet_all/index_1.shtml"

    # 在chinabyte下新建两个子节点，设置其节点名称为number和first
    chinabyte_number = ET.SubElement(chinabyte, "number")
    chinabyte_number.text = "1"
    chinabyte_first = ET.SubElement(chinabyte, "first")
    chinabyte_first.text = "http://www.chinabyte.com/more/124566.shtml"

    # 将节点数信息保存在ElementTree中，并且保存为XML格式文件
    tree = ET.ElementTree(root)
    tree.write(r"d:\urlfile.xml")


# 读取xml文件
def readXmlFile(xml):
    # root
    root = get_root(xml)
    root_tag = get_element_tag(root)
    print(root_tag)  # 返回"students"

    root_attrib = get_element_attrib(root)
    print(root_attrib)  # 返回字典数据{'class': 'G2016'}

    # children
    children = get_element_children(root)
    print(
        children)  # [<Element 'student' at 0x000000000079EBD8>, <Element 'student' at 0x00000000007B4598>, <Element 'student' at 0x00000000007B4778>]

    children_tags = get_elements_tag(children)
    print(children_tags)

    children_attribs = get_elements_attrib(children)
    print(children_attribs)

    # 获取二级元素的每一个子节点的名称和值
    for c in children:
        c_children = get_element_children(c)
        dict_text = get_elements_text(c_children)
        print(dict_text)  # 返回字典 {'gender': 'M', 'score': '90', 'age': '21', 'name': 'Hongten'}


# 修改xml文件
def editXmlFile(xml):
    tree = ET.parse(xml)
    for age in tree.iter('age'):
        new_age = int(age.text)-10
        age.text = str(new_age)
        age.set('updated', 'yes')
        tree.write(xml)


def main():
    # 创建新的xml文件
    buildXmlFile()
    # 读取xml文件
    readXmlFile(r"d:\students.xml")
    # 修改xml文件
    editXmlFile(r"d:\students.xml")

if __name__ == '__main__':
    main()

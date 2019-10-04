#!usr/bin/python3
from typing import NamedTuple, List
from dataclasses import dataclass

class User(NamedTuple):
    name: str

class TextLang(NamedTuple):
    text: str
    langTag: str

class Category(NamedTuple):
    alias: str
    title: str

@dataclass
class Es6Data:
    textLang: TextLang
    categories: List[Category]
    def add(self, cat):
        self.categories.append(cat)

class MyStruct(NamedTuple):
    foo: str
    bar: int
    baz: list
    qux: User

my_item = MyStruct('foo', 0, ['baz'], User('peter'))

my_text = TextLang(text="sword", langTag="en")
my_cat = Category(alias="fight", title="sword fight")
my_cat2 = Category(alias="got", title="game of thrones")
es6_data = Es6Data(textLang=my_text, categories=[])
boo = False
if not es6_data.categories:
    boo = True

print(boo)
es6_data.add(my_cat)
es6_data.add(my_cat2)

print(my_text)
print(my_cat)
print(es6_data)
print(es6_data.categories)
print(es6_data.categories[0])

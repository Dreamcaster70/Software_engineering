from pprint import pprint

my_dict = {'first': 'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)
dict_maker(a=1, b=2, c=3, d=4)
dict_maker(x=10, y=20, z=30)
pprint(my_dict)
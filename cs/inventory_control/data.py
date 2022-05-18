import os
import json

#全局变量
_products = {} #保存产品信息的字典：sku_id:sku_name
_locations = {} #保存货架位置的字典：loc_id:loc_name
_items = [] #保存商品库存的列表，元素为元组(sku_id,loc_id)

def init():
    """从磁盘JSON格式文件中读取数据"""
    global _products, _locations, _items
    if os.path.exists("products.json"):
        f = open("products.json", "r", encoding='utf-8')
        _products = json.loads(f.read())
        f.close()
    if os.path.exists("locations.json"):
        f = open("locations.json", "r", encoding='utf-8')
        _locations = json.loads(f.read())
        f.close()
    if os.path.exists("items.json"):
        f = open("items.json", "r", encoding='utf-8')
        _items = json.loads(f.read())
        f.close()
        
def _save_products():
    """ 把产品信息数据_products以JSON格式保存到磁盘文件"""
    global _products
    f = open("products.json", "w", encoding='utf-8')
    f.write(json.dumps(_products, ensure_ascii=False))
    f.close()

def _save_locations():
    """ 把货架位置数据_locations以JSON格式保存到磁盘文件"""
    global _locations
    f = open("locations.json", "w", encoding='utf-8')
    f.write(json.dumps(_locations))
    f.close()

def _save_items():
    """ 把商品库存数据_items以JSON格式保存到磁盘文件"""
    global _items
    f = open("items.json", "w", encoding='utf-8')
    f.write(json.dumps(_items))
    f.close()
    
def get_products():
    """ 返回产品信息 """
    global _products
    return _products

def get_locations():
    """ 返回货架位置信息 """
    global _locations
    return _locations

def get_items():
    """ 返回货架位置信息 """
    global _items
    return _items

def add_product(sku_id, sku_name):
    """ 增加一个产品sku_id、sku_name """
    global _products
    _products[sku_id] = sku_name
    _save_products()

def add_location(loc_id, loc_name):
    """ 增加一个货架位置loc_id、loc_name """
    global _locations
    _locations[loc_id] = loc_name
    _save_locations()

def add_item(sku_id, loc_id):
    """ 入库一件商品：商品sku_id、货架sku_id """
    global _items
    _items.append((sku_id, loc_id))
    _save_items()

def remove_item(sku_id, loc_id):
    """ 出库一件商品：商品sku_id、货架sku_id,返回True； 如果不存在，返回False  """
    global _items
    for i in range(len(_items)):
        if sku_id == _items[i][0] and loc_id == _items[i][1]:
            del _items[i]
            _save_items()
            return True
    return False

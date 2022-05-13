import data


def prompt_for_action():
    # 提示功能菜单，返回用户输入选择
    while True:
        print('---------------库存管理系统-------------')
        print('|1:增加产品信息          |')
        print('|2:产品信息报表          |')
        print('|3:增加货架位置          |')
        print('|4:货架位置报表          |')
        print('|5:商品入库管理          |')
        print('|6:商品出库管理          |')
        print('|7:商品库存信息报表          |')
        print('|0:退出              |')
        print('----------------------------------------')

        choice = input('请输入功能菜单(0-7):')
        if choice == '0':
            return 'QUIT'
        elif choice == '1':
            return 'ADD_PRODUCT'
        elif choice == '2':
            return 'REPORT_PRODUCTS'
        elif choice == '3':
            return 'ADD_LOCATION'
        elif choice == '4':
            return 'REPORT_LOCATIONS'
        elif choice == '5':
            return 'ADD_ITEM'
        elif choice == '6':
            return 'REMOVR_ITEM'
        elif choice == '7':
            return 'REPORT_ITEMS'


def prompt_for_old_sku_id():
    # 提示用户输入有效的产品sku_id并返回有效产品ID，或者返回None
    while True:
        sku_id = input('请输入产品ID:')
        if sku_id == '':
            return None
        elif sku_id not in data.get_products():
            print('该产品不存在，请重新输入')
        else:
            return sku_id


def prompt_for_new_sku_id():
    # 提示用户输入新的产品sku_id并返回新产品ID，或者返回None
    while True:
        sku_id = input('请输入新产品的ID:')
        if sku_id == '':
            return None
        elif sku_id in data.get_products():
            print('该产品已经存在,请重新输入')
        else:
            return sku_id


def prompt_for_old_loc_id():
    # 提示用户输入有效的货架位置loc_id并返回有效位置ID，或者返回None
    while True:
        loc_id = input('请输入货架位置ID:')
        if loc_id == '':
            return None
        elif loc_id not in data.get_locations():
            print('该货架位置不存在,请重新输入')
        else:
            return loc_id


def prompt_for_new_loc_id():
    # 提示用户输入新的货架位置loc_id并返回，或者返回None
    while True:
        loc_id = input('请输入新的货架位置ID:')
        if loc_id == '':
            return None
        elif loc_id in data.get_locations():
            print('该货架位置已经存在,请重新输入')
        else:
            return loc_id


def prompt_for_sku_name():
    # 提示用户输入产品名称sku_name并返回产品名称，或者返回None
    while True:
        sku_name = input('请输入产品名称:')
        if sku_name == '':
            return None
        else:
            return sku_name


def prompt_for_loc_name():
    # 提示用户输入货架名称loc_name并返回货架位置名称，或者返回None
    while True:
        loc_name = input('请输入货架位置名称:')
        if loc_name == '':
            return None
        else:
            return loc_name


def report_products():
    # 产品信息报表
    for (k, v) in data.get_products().items():
        print('{0:8} {1}'.format(k, v))


def report_locations():
    # 货架位置报表
    for (k, v) in data.get_locations().items():
        print('{0:8} {1}'.format(k, v))


def report_items():
    # 库存信息报表
    for (k, v) in data.get_items():
        sku_name = data.get_products()[k]
        loc_name = data.get_locations()[v]
        print('{0:8} {1}:  {2:8}{3}'.format(k, sku_name, v, loc_name))

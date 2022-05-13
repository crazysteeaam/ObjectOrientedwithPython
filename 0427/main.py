import data
import ui


def main():
    data.init()
    while True:
        action = ui.prompt_for_action()
        if action == 'QUIT':
            break
        elif action == 'ADD_PRODUCT':
            sku_id = ui.prompt_for_new_sku_id()
            if sku_id is not None:
                sku_name = ui.prompt_for_sku_name()
                if sku_name is not None:
                    data.add_product(sku_id, sku_name)
        elif action == 'REPORT_PRODUCTS':
            ui.report_products()
        elif action == 'ADD_LOCATION':
            loc_id = ui.prompt_for_new_loc_id()
            if loc_id is not None:
                loc_name = ui.prompt_for_loc_name()
                if loc_name is not None:
                    data.add_location(loc_id, loc_name)
        elif action == 'REPORT_LOCATION':
            ui.report_locations()
        elif action == 'ADD_ITEM':
            sku_id = ui.prompt_for_old_sku_id()
            if sku_id is not None:
                loc_id = ui.prompt_for_old_loc_id()
                if loc_id is not None:
                    data.add_item(sku_id, loc_id)
        elif action == 'REMOVE_ITEM':
            sku_id = ui.prompt_for_old_sku_id()
            if sku_id is not None:
                # 如果在_products里找不到输入的产品ID，打印产品不存在
                loc_id = ui.prompt_for_old_loc_id()
                if loc_id is not None:
                    # 如果在_locations里找不到输入的货架位置id，打印货架位置不存在
                    if not data.remove_item(sku_id, loc_id):
                        # 若在_items中找不到对应的sku和loc元组，打印该库不存在
                        print('该库不存在！')
        elif action == 'REPORT_ITEMS':
            ui.report_items()


if __name__ == "__main__":
    main()

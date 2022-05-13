#库存管理系统：基于JSON
import data
import ui

def main():
    data.init()
    while True:
        action=ui.prompt_for_action()
        if action=='QUIT':
            break
        elif action=='ADD_PRODUCT':
            sku_id=ui.prompt_for_new_sku_id()
            if sku_id!=None:
                sku_name=ui.prompt_for_sku_name()
                if sku_name!=None:
                    data.add_product(sku_id,sku_name)
        elif action=='REPORT_PRODUCTS':
            ui.report_products()
        elif action=='ADD_LOCATION':
            loc_id=ui.prompt_for_new_loc_id()
            if loc_id!=None:
                loc_name=ui.prompt_for_loc_name()
                if loc_name!=None:
                    data.add_location(loc_id,loc_name)
        elif action=='REPORT_LOCATIONS':
            ui.report_locations()
        elif action=='ADD_ITEM':
            sku_id=ui.prompt_for_old_sku_id()
            if sku_id!=None:
                loc_id=ui.prompt_for_old_loc_id()
                if loc_id!=None:
                    data.add_item(sku_id,loc_id)
        elif action=='REMOVE_ITEM':
            sku_id=ui.prompt_for_old_sku_id()
            if sku_id!=None:
                loc_id=ui.prompt_for_old_loc_id()
                if loc_id!=None:
                    if not data.remove_item(sku_id,loc_id):
                        print('该库存不存在')
        elif action=='REPORT_ITEMS':
            ui.report_items()
if __name__=='__main__':
    main()

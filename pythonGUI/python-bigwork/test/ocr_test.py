from paddleocr import PaddleOCR
import re
import warnings
import datetime


def ocr_check(img_path) -> int:
    # 目前支持的多语言语种可以通过修改lang参数进行切换# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    try:
        result = ocr.ocr(img_path, cls=True)
        pattern = re.compile("\('(.+?)'", re.S)
        resultlist = []
        for line in result:
            resultlist.append(re.findall(pattern, str(line))[0])
        print(resultlist)
        i = 0
        while i < len(resultlist):
            if resultlist[i] == '检测结果【阴性】':
                i += 1
                while i < len(resultlist) and resultlist[i] != '检测结果【阴性】':
                    if resultlist[i] == '姓名':
                        name = list(resultlist[i + 1])
                        if '徐' not in name:
                            print("识别错误，姓名不对")
                            return 0
                        else:
                            i += 1
                            while i < len(resultlist) and resultlist[i] != '检测结果【阴性】':
                                if resultlist[i] == '采样时间':
                                    resultlist[i + 1] += ":00"
                                    ocr_time = datetime.datetime.strptime(resultlist[i + 1], "%Y-%m-%d %H:%M:%S")
                                    ocr_time =ocr_time.strftime("%Y-%m-%d")
                                    current_time = datetime.datetime.now().strftime("%Y-%m-%d")
                                    if ocr_time != current_time:
                                        print("识别错误，时间不对")
                                        return 0
                                    else:
                                        print("时间正确，识别成功")
                                        return 1
                                i += 1
                    i += 1
            i += 1
    except Exception as e:
        print(e)
        print('识别失败')
    finally:
        print("识别程序结束")


if __name__ == "__main__":
    ocr_check('D:\\20212022s\\objectoriented2022\\ObjectOrientedwithPython\\pythonGUI\\python-bigwork\\images\\test_2.png')

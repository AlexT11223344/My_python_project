# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import eel
@eel.expose
def test_print(str_1):
    print("进来了",str_1)
    test_process(str_1)

def test_process(str_2):
    str_2 = str_2 + "已经处理"
    eel.system_sends_message(str_2)

if __name__ == '__main__':
    eel.init()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

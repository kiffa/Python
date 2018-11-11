import json

file_name = 'number.json'

def write_load_number():
    while True:
        try: 
            num = input("请输入您喜欢的数字：")
            if num == 'q':
                print("退出")
                break
            num = int(num)
            with open(file_name) as read_object:
                contents = read_object.read()
                if str(num) in contents:
                    print("数字已经存在")
                    continue
                else:
                    with open("number.json", 'a') as file_object:
                        json.dump(num,file_object)
                        print("添加ok")

            
        except ValueError:
            print("请输入数字。")
        
        except FileNotFoundError:
            with open("number.json", 'w') as file_object:
                json.dump(num,file_object)
                print("will create it")
        
        
    
    
write_load_number()


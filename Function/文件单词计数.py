def words_count(file_name):
    #该函数用来统计文件内单词数量
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        error_message = "未找到目标文件，请重新核实。"
        print(error_message)
    else:
        words = contents.split()
        words_num = len(words)
        print("文件包含" + str(words_num) + "个单词。")


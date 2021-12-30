import os

def isbinod(filename):
    with open(filename,"r")as f:
        file_content = f.read()
    if 'json' in file_content.lower():
        return True
    else:
        return False

if __name__ == '__main__':

    dir_content = os.listdir()
    #print(dir_content)
    json_count = 0
    for item in dir_content:
        if item.endswith('txt'):
            print(f"detected the json {item}")
            flag = isbinod(item)
            if(flag):
                print(f"********** json is found ********** {item}")
                json_count += 1
            else:
                print(f"json is not found {item}")
    print()
    print("!!!!!!!!! json detect summary !!!!!!!!!")
    print(f"{json_count} files found with json hidden into them")
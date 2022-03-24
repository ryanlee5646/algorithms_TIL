# test1
# directory = ["/", "/hello", "/hello/tmp", "/root", "/root/abcd", "/root/abcd/etc", "/root/abcd/hello"]
# command = ["mkdir /root/tmp", "cp /hello /root/tmp", "rm /hello"]

# test2
directory = ["/"]
command = ["mkdir /a", "mkdir /a/b", "mkdir /a/b/c", "cp /a/b /", "rm /a/b/c"]


# for i in directory:
#     if i not in dic:
#         dic[i] = 1

for i in command:
    cmd_path = i.split(' ')
    if cmd_path[0] == 'mkdir':
        end_path = cmd_path[1] # 생성할 폴더 /root/tmp => /root , /root/tmp 생성
        pathes = end_path[1:].split('/')
        tmp = ''
        for path in pathes:
            tmp += f'/{path}'
            if tmp not in directory:
                directory.append(tmp)
                
    elif cmd_path[0] == 'cp':
        copy = cmd_path[1] # 복사할 폴더 /a/b (/a/b or /a/b/c)
        path = cmd_path[2] # 복사 경로 /
        a = copy.split("/")
        b = '' # 앞에 중복 경로를 제외한 마지막 디렉토리부터 하위 폴더 경로를 뽑기위함 
        for i in a[1:-1]:
            b += "/"+i 
        tmp_list = []
        for i in directory:
            tmp = ''
            if i[:(len(copy))] == copy: # /a/b에 해당하는 경로
                if path == '/':
                    tmp += '/'+i.strip(b)
                    tmp_list.append(tmp)
                else:
                    tmp = path + i.strip(b)
                    tmp_list.append(tmp)
        for i in tmp_list:
            directory.append(i)

    else: # 삭제
        path = cmd_path[1] # 삭제경로, /hello가 포함된 모든 경로 삭제
        tmp_list = []
        for i in directory:
            if i[:(len(path))] == path:
                tmp_list.append(i)
        directory = list(set(directory) - set(tmp_list))
        
for i in sorted(directory):
    print(i)
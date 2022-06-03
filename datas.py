import json


class MyDatabass:
    def __init__(self):
        # 用户信息
        with open('userdatas.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.users = json.loads(text)
        # 通讯录人员信息
        with open('contant.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        self.data = json.loads(text)

    def all(self):
        return self.data

    def all_User(self):
        return self.users

    def Insert(self, data):
        self.data.append(data)

    def Delete_data(self, name):
        for s in self.data:
            if s['name'] == name:
                self.data.remove(s)  # 当删除执行后，在查询列表中未显示删除时的补充逻辑代码
                return f'{name}  成功删除'  # f-Strings：一种改进Python格式字符串的新方法
        return f'{name}  联系人不存在'

    def find_data_name(self, datas):
        i = []
        for s in self.data:
            if s['name'] == datas:
                i.append(s)
                continue
            if s['tel'] == datas:
                i.append(s)
                continue
            if s['address'] == datas:
                i.append(s)
                continue
            if s['email'] == datas:
                i.append(s)
                continue
            if s['InstantMessaging'] == datas:
                i.append(s)
                continue
            if s['sex'] == datas:
                i.append(s)
                continue
        else:
            return True, i

    def Updata(self, datas):
        index = 0
        for s in self.data:
            if s['tel'] == datas['tel']:
                self.data[index] = datas
                return f'{datas["tel"]}  数据编辑成功'
            index += 1
        return f'{datas["name"]}  数据编辑失败，用户不存在'

    def check_login(self, username, password):
        for user in self.users:
            if username == user['username']:
                if password == user['password']:
                    return True, '登录成功'
                else:
                    return False, '登录失败,密码错误'
        return False, '登录失败,用户不存在'


dd = MyDatabass()

if __name__ == '__main__':
    print(dd.check_login('wang', '123456'))

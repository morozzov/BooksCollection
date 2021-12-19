import json

class DB:

    path1 = '/Users/RMG/Desktop/CollectionData/db/users.json'
    path2 = '/Users/RMG/Desktop/CollectionData/db/books.json'
    dataUsers = {}
    dataUsers['Users'] = []
    dataFilms = {}
    dataFilms['Books'] = []

    def GetUser(self, login, password):

        with open(self.path1, 'r') as file:
            data = json.load(file)

        for i in data['Users']:
            if (i['login'] == login)and(i['password'] == password):
                flag = True

        return flag



    def WriteUser(self, user):

        with open(self.path1, 'r') as file:
            data = json.load(file)

        self.dataUsers['Users'] = data['Users']

        self.dataUsers['Users'].append(
            {
                'name' : user.Name,
                'login' : user.Login,
                'password' : user.Password
            })

        with open(self.path1, 'w') as file:
            json.dump(self.dataUsers, file)

        pass

    def WriteBook(self, film):

        with open(self.path2, 'r') as file:
            data = json.load(file)

        self.dataFilms['Books'] = data['Books']

        self.dataFilms['Books'].append(
            {
                'name' : film.Name,
                'author' : film.Author,
                'year' : film.Year
            })

        with  open(self.path2, 'w') as file:
            json.dump(self.dataFilms, file)

        pass

    def GetAllEmployees(self):

        with open(self.path2, 'r') as file:
            data = json.load(file)

        return data
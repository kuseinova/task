# 1) 


# class ContactList(list):

#     def search_by_name(self, name):
#         all_list = []
#         for n in self:
#             if n == name:
#                 all_list.append(n)
#             else:
#                 continue
#             return all_list



# all_contacts = ContactList(['Azat', 'Rinat', 'Argen'])

# a = all_contacts.search_by_name('Argen')

# print(a)



# 2)


# class User:

#     first_name = 'Aizhan'
#     second_name = "Imangazieva"
#     age = "17"
#     password = "1111"
#     img = "haha"
    
#     def describe_user(self):
#         self.first_name
#         self.second_name
#         self.age
#         self.password
#         self.img

# #     def greet_user(self):
#         print(f'Hello mister {self.first_name} {self.second_name}')


# class Admin(User):
#     privileges = ["разрешено добавлять сообщения", "разрешено удалятьпользователей", "разрешено банить пользователей"]

#     def show_privileges(self):
#         print(Admin.dict)



# a1 = User()
# a1.describe_user()
# a1.greet_user()
# admin = Admin()
# admin.show_privileges()
# admin.first_name = 'Admin'
# admin.describe_user()
# admin.greet_user()





#3)

# class House:
#     type_house = 'Дома 2 этажный'
#     house_are = 30
#     remaining_area = 0
#     furniture_list = {"кровать": 4, "шкаф-купе": 2, "стол": 1.5}

#     area = 0
#     for a in furniture_list.values():
#         area += a
        
#     remaining_area = house_are - area

#     def info_hause(self):
#         print(f"Тип {self.type_house}"  )
#         print(f"Общая площадь дома {self.house_are} км2")
#         print(f"Оставщая площадь дома {self.remaining_area} ")
#         print(f"Мебель в доме {self.furniture_list} ")
    

# house1 = House()
# house1.info_hause()


# task#4
# def funnyString(s):
    
#     r = s[::-1]
    
#     for i in range(0, len(s)):
#         if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
#             return "Not Funny"
    
#     return "Funny"

# print(funnyString("acxz"))
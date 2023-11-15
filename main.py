#
# a = {'an': ['jojo', 'hgh', 'fjf'],
# #       'age': (16,22,13,24),
# #       'job': 'none'}
# #
# # print(a['an'][1], a['job'][-1])
# nums = [i for i in range(11)]
# result = [f'{num}-четное' if num % 2==0 else f'{num}-нечетное' for num in nums]
# print(result)
# class Tank:
#     def __init__(self, typeq, weight, max_speed):
#      self.typeq = typeq
#      self.weight = weight
#      self.max_speed = max_speed
#
# tank = Tank('T-90', 65, 90)
# tank2 = Tank('Leopard', 89, 78)
# print(tank.typeq, tank.weight)
# print(tank2.typeq, tank2.weight)

# class Username:
#     def __init__(self, comm, like, dislike):
#         self.comm = comm
#         self.like = like
#         self.dislike = dislike
#
# username = Username('с', 5, 324)
# print(username.comm, username.like, username.dislike)
# class BankAccount:
#     def __init__(self, name, balace=0):
#           self.name = name
#           self.balance = balace
#     def deposit(self, money):
#           self.balance = self.balance + money
#     def cash(self, money):
#         self.balance = self.balance - money
#     def show_balace(self):
#           return self.balance
#
#
#
# while True:
#     name = input('Добро пожаловать! Введите имя: ')
#     client1 = BankAccount(name)
#     choice = input('1-депосит,2-снять деньги,3-баланс: ')
#     if choice == 1:
#        amount = int(input('Сколько хотите добавить на депосит?'))
#        client1.deposit(amount)
#     elif choice == 2:
#         amount = int(input('Сколько хотите снять?'))
#         client1.cash(amount)
#     elif choice == 3:
#          print(client1.show_balace())
#     else:
#         print('НЕ ПОНЯЛ')
#
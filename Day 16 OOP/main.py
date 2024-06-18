# import test_module

# test_module.printString("Alam")

# from turtle import Turtle, Screen

# timmy = Turtle()
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.forward(100)

# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pickachu", "Sqiurtle", "Charmander"])
print(table)

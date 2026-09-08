python
from circle import Circle
from rectangle import Rectangle

def main():
  print("Выберите фигуру")
  print("1.Круг")
  print("2.Прямоугольник")
  choice = input("Введите номер")
  if (choice == "1"):
    r = float(input("Введите радиус"))
    shape = Circle(r)
    print(f"Площадь круга :{shape.area():.2f}")
  elif(choice == "2"):
    w = float(input("Введи ширину"))
    h = float(input("Введи высоту"))
    shape = Rectangle(w, h)
    print(f"Площадь прямоуглльника :{shape.area():.2f}")
  else:
    print("Неверный выбор")

if __name__ == "__main__":
  main()

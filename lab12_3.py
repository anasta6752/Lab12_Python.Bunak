
import triangle_module


a = float(input("Введіть першу сторону трикутника: "))
b = float(input("Введіть другу сторону трикутника: "))
c = float(input("Введіть третю сторону трикутника: "))

if a + b > c and a + c > b and b + c > a:
    R = triangle_module.circumscribed_radius(a, b, c)
    r = triangle_module.inscribed_radius(a, b, c)

    print("Радіус описаного кола:", round(R, 2))
    print("Радіус вписаного кола:", round(r, 2))
else:
    print("Трикутник із такими сторонами не існує.")

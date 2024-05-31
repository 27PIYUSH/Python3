class circle(object):
    def __init__(self,radius):
        self.radius=radius
    def __str__(self):
        return "THIS IS A CLASS WHICH TAKES RADIUS AS ARGUMENT"

c=circle(5)
print(c)
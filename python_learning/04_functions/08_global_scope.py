chai_type = "Plain"

def front_desk():
    def kitchen():
        # nonlocal chai_type
        #  people mostly avoid using 'global inside function block'
        global chai_type
        chai_type = "Irani"
    kitchen()

front_desk()
print("Final global chai: ", chai_type)

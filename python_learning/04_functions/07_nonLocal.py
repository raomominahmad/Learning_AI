
chai_type = "ginger"

def update_order():
    chai_type = "Elaichi"
    def kitchen():
        # it refers to a variable that belongs to an enclosing (outer) function.
        # nonlocal chai_type
        global chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update" ,chai_type)


update_order()
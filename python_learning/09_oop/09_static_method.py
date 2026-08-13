
class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [ item.strip() for item in text.split(",")]     

    # when there is object
    # def clean_ingredients(self, text):
    #     return [ item.strip() for item in text.split(",")] 





raw = " water , milk , ginger , honey"

print(ChaiUtils.clean_ingredients(raw))
# obj = ChaiUtils() 
# print(obj.clean_ingredients(raw))


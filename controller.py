from model import Model, DecodeError
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        try:
            self.model = Model()
        except DecodeError as e:
            self.view.__throw_an_error__(e)

    def run(self):
        query = None
        while query != 'Выход':
            query = self.view.wait_user_answer()
            self.check_user_answer(query)

    def check_user_answer(self, query):
        if query == '1':
            recept_data = self.view.add_new_recept()
            self.model.add_new_recept(recept_data)
        elif query == '2':
            all_recepts = self.model.recepts
            self.view.print_recepts(all_recepts)
        elif query == '3':
            criteria = self.view.find_recepts()
            recepts = self.model.find_recepts(criteria)
            self.view.print_recepts(recepts)
        elif query == '4':
            recept_name = self.view.get_recept_name()
            recepts = self.model.find_recepts([recept_name])
            result = self.model.delete_recept(recepts)
            if result == 'Слишком много рецептов':
                self.view.print_recepts(recepts)
                number = self.view.get_deletion_context()
                result = self.model.delete_recept([recepts[number - 1]])
            self.view.return_delete_result(result)
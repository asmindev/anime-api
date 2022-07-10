class FieldIsRequired(Exception):
    def __init__(self, field):
        self.field = field

    def __str__(self):
        return "Field {} is required".format(self.field)


errors = {"FieldIsRequired": {"message": "Field is required", "status": 400}}

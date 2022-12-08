from dataclasses import dataclass


@dataclass
class RedoOperation:
    target_object: object
    handler: object
    args: tuple


class RedoManager:
    __redo_operations = []

    @staticmethod
    def register_operation(target_object, handler, *args):
        RedoManager.__redo_operations.append(RedoOperation(target_object, handler, args))

    @staticmethod
    def redo():
        redo_operation = RedoManager.__redo_operations.pop()
        redo_operation.handler(redo_operation.target_object, *redo_operation.args)

    @staticmethod
    def get_first_argument():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].args[0]

    @staticmethod
    def get_second_argument():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].args[1]

    @staticmethod
    def get_third_argument():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].args[2]

    @staticmethod
    def get_handler():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].handler

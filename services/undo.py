from dataclasses import dataclass


@dataclass
class UndoOperation:
    target_object: object
    handler: object
    args: tuple


class UndoManager:
    __undo_operations = []

    @staticmethod
    def register_operation(target_object, handler, *args):
        UndoManager.__undo_operations.append(UndoOperation(target_object, handler, args))

    @staticmethod
    def undo():
        undo_operation = UndoManager.__undo_operations.pop()
        undo_operation.handler(undo_operation.target_object, *undo_operation.args)

    @staticmethod
    def get_first_argument():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations) - 1].args[0]

    @staticmethod
    def get_second_argument():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations) - 1].args[1]

    @staticmethod
    def get_third_argument():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations) - 1].args[2]

    @staticmethod
    def get_handler():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations) - 1].handler

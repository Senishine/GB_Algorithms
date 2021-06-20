"""
Задание 2.
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""

class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if self.root >= new_node:
                # если у узла нет левого потомка
                if self.left_child == None:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.left_child = BinaryTree(new_node)
                # если у узла есть левый потомок
                else:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
            else:
                raise Exception('Incorrect path to insert node')
        except Exception as e:
            print(e)


    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root <= new_node:
                # если у узла нет правого потомка
                if self.right_child == None:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.right_child = BinaryTree(new_node)
                # если у узла есть правый потомок
                else:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
            else:
                raise Exception('Incorrect path to insert node')
        except Exception as e:
            print(e)

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def __str__(self):
        result = ''
        if self.left_child is not None:
            result += str(self.left_child) + ' '
        if self.root is not None:
            result += str(self.root) + ' '
        if self.right_child is not None:
            result += str(self.right_child) + ' '
        return result



r = BinaryTree(20)
print(f'The root: {r.get_root_val()}')
print(f'Left child: {r.get_left_child()}')
print(f'Right child: {r.get_right_child()}')
r.insert_left(5)
print(f'Left child {r.get_left_child()}')
print(f'The root of left child: {r.get_left_child().get_root_val()}')
r.insert_right(22)
print(f'Right child: {r.get_right_child()}')
print(f'The root of right child: {r.get_right_child().get_root_val()}')
print(r.get_right_child().get_root_val())
r.insert_left(10)
print(f'Left child {r.get_left_child()}')
print(f'The root of left child: {r.get_left_child().get_root_val()}')
print(f'Tree: {r}')

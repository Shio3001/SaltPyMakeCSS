import color
import abc
import copy


# specific_classと似た役割をするが、こちらは構文丸ごと返す

class TemplateClassBase(object, metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def set_syntax_fluctuation(self):
        pass

    @abc.abstractmethod
    def set_syntax_fixed(self):
        pass

    @abc.abstractmethod
    def get_syntax_block(self):
        pass

    @abc.abstractmethod
    def get_syntax_animation(self):
        pass

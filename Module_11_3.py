def introspection_info(obj):
    info = {}
    info["Тип объекта"] = type(obj).__name__
    attributes = dir(obj)
    methods = []
    other_attributes = []
    for attribute in attributes:
        if callable(getattr(obj, attribute)):
            methods.append(attribute)
        else:
            other_attributes.append(attribute)
    info["Атрибуты объекта"] = other_attributes
    info["Методы объекта"] = methods
    info["Модуль"] = __name__

    return info


number_info = introspection_info(42)
print(number_info)

from rest_framework import routers, serializers


class ChoicesSerializerField(serializers.SerializerMethodField):
    """
    A read-only field that return the representation of a model field with choices.
    """

    def to_representation(self, value):
        # sample: 'get_XXXX_display'
        method_name = 'get_{field_name}_display'.format(field_name=self.field_name)
        # retrieve instance method
        method = getattr(value, method_name)
    
        # retrieve instance method
        method_id = getattr(value, self.field_name)
        # finally use instance method to return result of get_XXXX_display()
        #return method()
        return {'value': method(), 'id': method_id}        
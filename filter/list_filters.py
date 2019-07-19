#!/usr/bin/python

def get_keys_of_dict_in_list(a):
    result = []
    for item in a:
        result.extend(list(item.keys()))
    return list(set(result))

def combine_dict_in_list(a):
    result = {}
    for item in a:
        result.update(item)
    return result

class FilterModule(object):
    ''' Ansible jinja2 filters '''

    def filters(self):
        filters = {
            'get_keys_of_dict_in_list': get_keys_of_dict_in_list,
            'combine_dict_in_list': combine_dict_in_list,
        }
        return filters

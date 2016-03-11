import re
import json

first_cap_re = re.compile('(.)([A-Z][a-z]+)')
all_cap_re = re.compile('([a-z0-9])([A-Z])')


def _convert(name):
    """
    Convert camel to snake case

    :param name:
    :type name: str
    :return:
    :rtype: str
    """
    s1 = first_cap_re.sub(r'\1_\2', name)
    return all_cap_re.sub(r'\1_\2', s1).lower()


def _replace_builtin(name):
    name = _convert(name)

    if name in ('all', 'type', 'list', 'dict', 'next'):
        name += '_'

    return name


def _fix_list(input_list):
    """
    helper for _fix_dict

    :param input_list:
    :return:
    :rtype: list
    """
    return [_fix_dict(l) for l in input_list]


def _fix_tuple(input_tuple):
    """
    helper for fix_dict

    :param input_tuple:
    :return:
    :rtype: tuple
    """
    return [_fix_dict(l) for l in input_tuple]


def _fix_dict(input_dict):
    """
    helper to replace caps with underscores

    :param input_dict:
    :type: dict
    :return:
    :rtype: dict
    """
    output_dict = dict()

    for k in input_dict.keys():
        if isinstance(input_dict[k], dict):
            output_dict[_replace_builtin(k)] = _fix_dict(input_dict[k])
        elif isinstance(input_dict[k], list):
            output_dict[_replace_builtin(k)] = _fix_list(input_dict[k])
        elif isinstance(input_dict[k], tuple):
            output_dict[_replace_builtin(k)] = _fix_tuple(input_dict[k])
        else:
            output_dict[_replace_builtin(k)] = input_dict[k]

    return output_dict


def _gen_class_stub(input_thing):
    print(_gen_class_inner(input_thing) + '\n\n' + json.dumps(input_thing, indent=4, sort_keys=True))


def _gen_class_inner(input_thing):
    """
    for dev purposes to generate the response objects from the dict

    :param input_thing:
    :type input_thing: dict|list
    :return:
    """
    out = ''

    if isinstance(input_thing, list):
        out += _gen_class_inner(input_thing[0])
    elif isinstance(input_thing, dict):
        keys = []
        for k, v in input_thing.items():
            keys.append(k)

            if isinstance(v, (list, dict)):
                out += _gen_class_inner(v)

        keys.sort()

        key_none = [k + '=None' for k in keys]

        attr_list = []

        for k in keys:
            if isinstance(input_thing[k], list):
                attr_list.append('self.{0} = []'.format(k))
            elif isinstance(input_thing[k], dict):
                attr_list.append('self.{0} = SOMEOBJECT'.format(k))
            else:
                attr_list.append('self.{0} = {0}'.format(k))

        out += '\n'
        out += 'class SomeClass:\n\n'
        out += '\tdef __init__(self, {0}):\n\n'.format(', '.join(key_none))
        for a in attr_list:
            out += '\t\t' + a + '\n'




    return out


class ResponseBase:
    """
    Base class for all response objects
    """
    def __init__(self, input_dict):
        """

        :param input_dict: input dictionary
        :type input_dict: dict
        :return:
        """
        input_dict = _fix_dict(input_dict)

        top_keys = [k for k in input_dict.keys()]

        if len(top_keys) > 1:
            raise Exception('too many top keys')

        self.response_type = top_keys[0]

        self._inner_dict = input_dict[self.response_type]

    def _wrap_dict_in_list(self, key):
        """
        helper to wrap single items in a list

        helps for uniform responses, example one quote vs several

        :param key: the key to wrap
        :type key: str
        """
        if isinstance(self._inner_dict[key], dict):
            self._inner_dict[key] = [self._inner_dict[key]]

    def _gen_class(self):
        """
        just for dev to write out class stubs from responses

        :return:
        """
        _gen_class_stub(self._inner_dict)

import os
import sys

dirname = os.path.dirname(__file__)
module_path = os.path.join(dirname, "..")
sys.path.append(module_path)

from AbstractTest2 import AbstractTest2, RunCode, process, wrapper

CORRECT_CODE = r"""
def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[value if hash(value) else str(value)] = key
    return result
"""

CORRECT_CODE_LANGUAGE = "Python"


class Tests(AbstractTest2):
    def test_1(self):
        class_name = ""
        class_args = ""
        method_name = "key_params"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = False
        add_before = ""
        add_after = """
        params = key_params(a=1, b='hello', c=[1, 2, 3], d={})]
        print(params)
        """

        arguments = {}

        fake_arguments = {}

        self.default_test(
            class_name=class_name,
            class_args=class_args,
            method_name=method_name,
            attr_name=attr_name,
            need_to_eval=need_to_eval,
            arguments=arguments,
            fake_arguments=fake_arguments,
            correct_code=CORRECT_CODE,
            correct_code_language=CORRECT_CODE_LANGUAGE,
            var_name=var_name,
            formulation=formulation,
            need_print=need_print,
            add_before=add_before,
            add_after=add_after,
        )

    def test_2(self):
        class_name = ""
        class_args = ""
        method_name = "key_params"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = False
        add_before = ""
        add_after = """
        params = key_params(a=42, b='hello', c=3.14, d='world')
        print(params)
        """

        arguments = {}

        fake_arguments = {}

        self.default_test(
            class_name=class_name,
            class_args=class_args,
            method_name=method_name,
            attr_name=attr_name,
            need_to_eval=need_to_eval,
            arguments=arguments,
            fake_arguments=fake_arguments,
            correct_code=CORRECT_CODE,
            correct_code_language=CORRECT_CODE_LANGUAGE,
            var_name=var_name,
            formulation=formulation,
            need_print=need_print,
            add_before=add_before,
            add_after=add_after,
        )
    def test_3(self):
        class_name = ""
        class_args = ""
        method_name = "key_params"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = False
        add_before = ""
        add_after = """
        params = key_params(a=None, b='', c=[], d={})
        print(params)
        """

        arguments = {}

        fake_arguments = {}

        self.default_test(
            class_name=class_name,
            class_args=class_args,
            method_name=method_name,
            attr_name=attr_name,
            need_to_eval=need_to_eval,
            arguments=arguments,
            fake_arguments=fake_arguments,
            correct_code=CORRECT_CODE,
            correct_code_language=CORRECT_CODE_LANGUAGE,
            var_name=var_name,
            formulation=formulation,
            need_print=need_print,
            add_before=add_before,
            add_after=add_after,
        )
    def test_4(self):
        class_name = ""
        class_args = ""
        method_name = "key_params"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = False
        add_before = """
        
        """
        add_after = """
        params = key_params(a=42, b='hello', c=3.14, d='world')
        print(params)
        """

        arguments = {}

        fake_arguments = {}

        self.default_test(
            class_name=class_name,
            class_args=class_args,
            method_name=method_name,
            attr_name=attr_name,
            need_to_eval=need_to_eval,
            arguments=arguments,
            fake_arguments=fake_arguments,
            correct_code=CORRECT_CODE,
            correct_code_language=CORRECT_CODE_LANGUAGE,
            var_name=var_name,
            formulation=formulation,
            need_print=need_print,
            add_before=add_before,
            add_after=add_after,
        )
    def test_5(self):
        class_name = ""
        class_args = ""
        method_name = "key_params"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = False
        add_before = ""
        add_after = """
        params = key_params(a=True, b=False, c=True, d=False)
        print(params)
        """

        arguments = {}

        fake_arguments = {}

        self.default_test(
            class_name=class_name,
            class_args=class_args,
            method_name=method_name,
            attr_name=attr_name,
            need_to_eval=need_to_eval,
            arguments=arguments,
            fake_arguments=fake_arguments,
            correct_code=CORRECT_CODE,
            correct_code_language=CORRECT_CODE_LANGUAGE,
            var_name=var_name,
            formulation=formulation,
            need_print=need_print,
            add_before=add_before,
            add_after=add_after,
        )
    def test_6(self):
        class_name = ""
        class_args = ""
        method_name = "key_params"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = False
        add_before = ""
        add_after = """
        params = key_params(name='Alice', age=30, scores=[85, 90, 78], info={'city': 'New York', 'email': 'alice@example.com'})
        print(params)
        """

        arguments = {}

        fake_arguments = {}

        self.default_test(
            class_name=class_name,
            class_args=class_args,
            method_name=method_name,
            attr_name=attr_name,
            need_to_eval=need_to_eval,
            arguments=arguments,
            fake_arguments=fake_arguments,
            correct_code=CORRECT_CODE,
            correct_code_language=CORRECT_CODE_LANGUAGE,
            var_name=var_name,
            formulation=formulation,
            need_print=need_print,
            add_before=add_before,
            add_after=add_after,
        )
    
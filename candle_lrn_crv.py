from main_lrn_crv import parse_args, run as lrn_crv_run


class ArgumentStruct:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def initialize_parameters():
    parsed_args = parse_args([])
    params = vars(parsed_args)
    return params


def run(params):
    print("run with", params)
    val = lrn_crv_run(params)
    history_dict = {'history': {'val_loss': [val]}}
    history = ArgumentStruct(**history_dict)
    return history

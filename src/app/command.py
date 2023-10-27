from types import MethodType
from .actuators import Actuator


def translate_command(tokens: list[str], ai_name: str, ai_actions: list[dict[str, object]]):
    valid_command = False
    item, method = None, None

    if (len(tokens) >= 3) and (ai_name == tokens[0]):
        action, item = tokens[1], tokens[2]

        for ai_action in ai_actions:
            if (action in ai_action.get('names')) and (item == ai_action.get('item')):
                method = ai_action.get('method')
                valid_command = True
                break

    if not valid_command:
        raise Exception('Invalid command.')

    return (item, method)


def execute_command(item: str, method: str, actuators: tuple[Actuator, ...]):
    msg, cat = None, None

    for actuator in actuators:
        if not item in actuator.item_names:
            continue

        if hasattr(actuator, method):
            actuator_method = getattr(actuator, method)

            if isinstance(actuator_method, MethodType):
                msg, cat = actuator_method()
                break

    return (msg, cat)

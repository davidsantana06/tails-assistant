from types import MethodType
from .actuators import Actuator


def validate_command(tokens: list[str], ai_name: str, actions: list[dict[str, object]]):
    valid_command = False
    action, item, method = None, None, None

    if (len(tokens) >= 3) and (ai_name == tokens[0]):
        action, item = tokens[1], tokens[2]

        for action_entry in actions:
            if (action in action_entry.get('names')) and (item == action_entry.get('item')):
                method = action_entry.get('method')
                valid_command = True
                break

    return (valid_command, item, method)


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

def validate_command(tokens: list[str], ai_name: str, actions: list[dict[str, object]]):
    valid_command = False
    action, obj = None, None

    if (len(tokens) >= 3) and (ai_name == tokens[0]):
        action, obj = tokens[1], tokens[2]

        for action_entry in actions:
            if (action == action_entry.get('name')) and (obj in action_entry.get('objects')):
                valid_command = True
                break

    return (valid_command, action, obj)


def execute_command(action: str, obj: str):
    pass

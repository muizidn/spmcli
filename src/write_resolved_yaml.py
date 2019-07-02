import os
import yaml
from .find_config import find_config
from .global_variable import supported_commands, supported_platforms

__RESOLVED_CONFIG__ = 'SPMCLI.resolved'

def write_resolved_config_yaml(config):
    root_config_path = find_config()
    root_dir = os.path.dirname(root_config_path)

    resolved_config = {}
    # """
    # platform:
    #     subcommands:
    #         options: (dict|list)
    # """
    for platform in supported_platforms:
        if not config.get(platform):
            continue
        subcommand_configs = config[platform]
        for command in supported_commands:
            if not subcommand_configs.get(command):
                continue
            options = subcommand_configs[command]
            for option in options:
                value = options[option]
                option_values = []
                if type(value) is dict:
                    for (k, v) in value.items():
                        option_values.append(k)
                        if v:
                            option_values.append(v)
                elif type(value) is list:
                    for v in value:
                        option_values.append(v)
                else:
                    assert not value is None
                    option_values.append(value)
                options[option] = option_values
            subcommand_configs[command] = options
        resolved_config[platform] = subcommand_configs

    with open(f"{root_dir}/{__RESOLVED_CONFIG__}", 'w') as f:
        print("Writing resolved config.")
        yaml.dump(resolved_config, f)
    return resolved_config
from dataclasses import dataclass, field, fields, asdict


@dataclass(slots=True)
class Constants:
    """ Class for 'global' variables to be used across files. Feed variables using dict unpacking from config.toml. """
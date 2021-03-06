import sys
from _typeshed import StrPath, SupportsWrite
from typing import IO, Any, Mapping, MutableMapping, Text, Union

if sys.version_info >= (3, 6):
    _PathLike = StrPath
elif sys.version_info >= (3, 4):
    import pathlib

    _PathLike = Union[StrPath, pathlib.PurePath]
else:
    _PathLike = StrPath

class TomlDecodeError(Exception): ...

def load(f: _PathLike | list[Text] | IO[str], _dict: type[MutableMapping[str, Any]] = ...) -> MutableMapping[str, Any]: ...
def loads(s: Text, _dict: type[MutableMapping[str, Any]] = ...) -> MutableMapping[str, Any]: ...
def dump(o: Mapping[str, Any], f: SupportsWrite[str]) -> str: ...
def dumps(o: Mapping[str, Any]) -> str: ...

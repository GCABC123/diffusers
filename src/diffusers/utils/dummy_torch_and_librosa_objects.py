# This file is autogenerated by the command `make fix-copies`, do not edit.
from ..utils import DummyObject, requires_backends


class AudioDiffusionPipeline(metaclass=DummyObject):
    _backends = ["torch", "librosa"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["torch", "librosa"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["torch", "librosa"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["torch", "librosa"])


class Mel(metaclass=DummyObject):
    _backends = ["torch", "librosa"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["torch", "librosa"])

    @classmethod
    def from_config(cls, *args, **kwargs):
        requires_backends(cls, ["torch", "librosa"])

    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        requires_backends(cls, ["torch", "librosa"])
#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.

from typing import Tuple, Dict

from augly.video.augmenters.ffmpeg import BaseFFMPEGAugmenter
from ffmpeg.nodes import FilterableStream


class VideoAugmenterByContrast(BaseFFMPEGAugmenter):
    def __init__(self, level: float):
        assert (
            -1000.0 <= level <= 1000.0
        ), "Level must be a value in the range [-1000, 1000]"
        self.level = level

    def add_augmenter(
        self, in_stream: FilterableStream, **kwargs
    ) -> Tuple[FilterableStream, Dict]:
        """
        Changes the contrast level of the video

        @param in_stream: the FFMPEG object of the video

        @returns: a tuple containing the FFMPEG object with the augmentation
            applied and a dictionary with any output arguments as necessary
        """
        return in_stream.video.filter("eq", **{"contrast": self.level}), {}

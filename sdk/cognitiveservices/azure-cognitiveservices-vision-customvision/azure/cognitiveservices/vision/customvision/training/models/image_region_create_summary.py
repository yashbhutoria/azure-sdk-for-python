# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ImageRegionCreateSummary(Model):
    """ImageRegionCreateSummary.

    :param created:
    :type created:
     list[~azure.cognitiveservices.vision.customvision.training.models.ImageRegionCreateResult]
    :param duplicated:
    :type duplicated:
     list[~azure.cognitiveservices.vision.customvision.training.models.ImageRegionCreateEntry]
    :param exceeded:
    :type exceeded:
     list[~azure.cognitiveservices.vision.customvision.training.models.ImageRegionCreateEntry]
    """

    _attribute_map = {
        'created': {'key': 'created', 'type': '[ImageRegionCreateResult]'},
        'duplicated': {'key': 'duplicated', 'type': '[ImageRegionCreateEntry]'},
        'exceeded': {'key': 'exceeded', 'type': '[ImageRegionCreateEntry]'},
    }

    def __init__(self, **kwargs):
        super(ImageRegionCreateSummary, self).__init__(**kwargs)
        self.created = kwargs.get('created', None)
        self.duplicated = kwargs.get('duplicated', None)
        self.exceeded = kwargs.get('exceeded', None)
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


class DataLakeAnalyticsCatalogCredentialUpdateParameters(Model):
    """Data Lake Analytics catalog credential update parameters.

    :param password: the current password for the credential and user with
     access to the data source. This is required if the requester is not the
     account owner.
    :type password: str
    :param new_password: the new password for the credential and user with
     access to the data source.
    :type new_password: str
    :param uri: the URI identifier for the data source this credential can
     connect to in the format <hostname>:<port>
    :type uri: str
    :param user_id: the object identifier for the user associated with this
     credential with access to the data source.
    :type user_id: str
    """

    _attribute_map = {
        'password': {'key': 'password', 'type': 'str'},
        'new_password': {'key': 'newPassword', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DataLakeAnalyticsCatalogCredentialUpdateParameters, self).__init__(**kwargs)
        self.password = kwargs.get('password', None)
        self.new_password = kwargs.get('new_password', None)
        self.uri = kwargs.get('uri', None)
        self.user_id = kwargs.get('user_id', None)
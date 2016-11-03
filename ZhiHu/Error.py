#    Copyright 2016 WiseDoge

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""
异常类集合。
"""

class NoFolloweeError(Exception):
    """
    异常类，如果一个用户没有关注人，则抛出此异常。
    """

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr("This followees list is none")


class MongoClientError(Exception):
    """
    如果无法连接至MongoDB，则抛出此异常。
    """

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr("Can not client to MongoDB")


class WebError(Exception):
    """
    410错误，抛出此异常。
    该异常会直接让当前线程退出。
    """

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr("410 Error")

class SettingError(Exception):
    """
    setting.json设置错误，抛出此异常。
    """
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return repr(self.info)
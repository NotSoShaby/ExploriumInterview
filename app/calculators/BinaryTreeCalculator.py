
""""""
import json
from queue import Queue

from app.infra.Utils import Utils


class BinaryTreeCalculator(object):
    """
    A class to provide calculation functions on a binary tree in the format of Json.
    """
    logger = Utils.get_main_app_logger()

    @classmethod
    def get_initiated_que(cls, json_path):
        """ Open the json file and load the tree to the que. """

        cls.logger.debug("Initiating que with json tree from: {}".format(json_path))

        que = Queue()
        with open(json_path) as json_file:
            tree = json.load(json_file)
        que.put(tree)
        return que

    @classmethod
    def get_nodes_sum(cls, json_path):
        """ Run on all nodes in the tree and calculate their sum. This is done by taking the root node from the queue
        and re-populating the queue with more nodes as much as necessary while adding each node to the result.

        :param json_path: path to the json file, holding the binary tree"""

        que = cls.get_initiated_que(json_path)

        cls.logger.debug("Starting calculation on tree")

        res = 0
        while not que.empty():
            curr_node = que.get()
            for k, v in curr_node.items():
                res += int(k)
                if v[0]:
                    que.put(v[0])
                if v[1]:
                    que.put(v[1])

        cls.logger.debug("For json tree at: {0}, got: {1} as the sum".format(json_path, str(res)))

        return res

import datetime


class QueryHelper:
    """ A class to help with querying the database """
    # TODO - have this class holding the engine and use SQLalchemy for all requests

    @staticmethod
    def get_query_by_sum(nodes_sum):
        return """
                    SELECT * FROM tree_sum_table
                    WHERE nodes_sum={}
               """.format(str(nodes_sum))

    @staticmethod
    def insert_tree_sum_query(nodes_sum):
        return """
                    INSERT INTO tree_sum_table
                    (nodes_sum, date_inserted) VALUES ({0}, '{1}')
               """.format(str(nodes_sum), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

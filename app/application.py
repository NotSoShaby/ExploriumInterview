import os

import time
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker
from app.calculators.BinaryTreeCalculator import BinaryTreeCalculator
from app.db_helper.QueryHelper import QueryHelper
from app.db_helper.tables.TreeSum import Base, TreeSum
from app.infra.Utils import Utils


class App:
    """ A class to run all the app's functions """

    def __init__(self):

        self.logger = Utils.get_main_app_logger()
        self.logger.info("Initiating app")
        self.engine = create_engine('postgres+psycopg2://postgres:postgres@db:5432', echo=True)
        Base.metadata.create_all(self.engine)
        self.session_maker = sessionmaker(bind=self.engine)

    def run_app_on_multiple_trees(self):
        """
        main app function, will collect all the trees from the data folder, calculate their sum, and try to enter
        it to the db.
        """
        for tree_json_path in Utils.get_all_files_from_data_folder():

            tree_name = os.path.basename(tree_json_path)
            self.logger.info("*" * 15 + "Starting tree: {}".format(tree_name) + "*" * 15)

            # Create session
            session = self.session_maker()

            # calculate the sum of the tree
            tree_sum = BinaryTreeCalculator().get_nodes_sum(tree_json_path)

            db_sum_query = QueryHelper().get_query_by_sum(tree_sum)

            # check if that sum is already in the db
            self.logger.info("Checking if sum: {} is already in the db".format(tree_sum))

            result = self.engine.execute(db_sum_query)

            if len(result.fetchall()):

                # if sum is in the db, get the whole row and log the date that it was inserted to the db at
                db_obj = session.query(TreeSum).filter_by(nodes_sum=tree_sum).first()
                self.logger.debug("The sum -{0}- is already in the system! It was entered at: {1}".format(
                    db_obj.nodes_sum, db_obj.date_inserted))

            else:

                # if sum not in db add it with the current datetime
                self.logger.info("Adding sum: {} to the db".format(tree_sum))
                insert_query = QueryHelper().insert_tree_sum_query(tree_sum)

                self.engine.execute(insert_query)
                self.logger.info("Sum {} was added to the db successfully!".format(tree_sum))

            self.logger.info("-" * 15 + "Finished tree {}".format(tree_name) + "-" * 15)


if __name__ == '__main__':

    while True:
        ans = input("Run App? (if no, quit) [y,n]")
        if ans.lower()=="y":
            App().run_app_on_multiple_trees()
        elif ans.lower()=="n":
            exit()
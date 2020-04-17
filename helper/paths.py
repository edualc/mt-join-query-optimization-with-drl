import os
import os.path as path

import agents.queries.path_helper as queries_helper

def join(base, *args):
    for arg in args:
        base = path.join(base, arg)

    return base

def get_queries(*args):
  return join(queries_helper.get_queries_path(), *args)

# # query_parser_joinonly.py
# # ===================================================================================================================================================
# # 
# "~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_label.txt"
# "~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_labled.txt"

# # cm1_postgres_card_env_job.py
# # ===================================================================================================================================================
# # 
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval/job_queries_simple_test_7400.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval/job_queries_simple_rejoin_test.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval/job_queries_simple_crossval_7400_3_test.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval/job_queries_simple_crossval_7400_0_train.txt'

# # cm1_postgres_card_env_job_crossval_0.py
# # ===================================================================================================================================================
# # 
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_test_7400.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_rejoin_test.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval_sens/job_queries_simple_crossval_0_test.txt'

# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_train_7400.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_sipmle_rejoin_train.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval/job_queries_simple_crossval_7400_0_train_sort_a.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval_sens/job_queries_simple_crossval_0_train.txt'

# # cm1_postgres_card_env_job_crossval_1.py
# # ===================================================================================================================================================
# # 
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_test_7400.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_rejoin_test.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval_sens/job_queries_simple_crossval_1_test.txt'

# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_train_7400.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_rejoin_train.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval/job_queries_simple_crossval_7400_0_train_sort_a.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval_sens/job_queries_simple_crossval_1_train.txt'

# # cm1_postgres_card_env_job_crossval_2.py
# # ===================================================================================================================================================
# # 
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_test_7400.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_rejoin_test.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval_sens/job_queries_simple_crossval_2_test.txt'

# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_train_7400.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_rejoin_train.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval/job_queries_simple_crossval_7400_0_train_sort_a.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval_sens/job_queries_simple_crossval_2_train.txt'

# # cm1_postgres_card_env_job_crossval_3.py
# # ===================================================================================================================================================
# # 
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_test_7400.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_rejoin_test.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval_sens/job_queries_simple_crossval_3_test.txt'

# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_train_7400.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/job_queries_simple_rejoin_train.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval/job_queries_simple_crossval_7400_0_train_sort_a.txt'
# '~//PycharmProjects/mt-join-queryoptimization-with-drl/agents/queries/crossval_sens/job_queries_simple_crossval_3_train.txt'

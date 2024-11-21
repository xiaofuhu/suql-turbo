from suql.sql_free_text_support.execute_free_text_sql import suql_execute
import json
# import litellm
# litellm.set_verbose = True

table_w_ids = {"log_records_small": "record_id"}
database = "postgres"

def find_relevant_entries(text, num=5):
  suql = "SELECT content FROM log_records_small WHERE is_relevant(content, '{}') LIMIT {};".format(text, num)
  answer = suql_execute(suql, table_w_ids, database)
  print(json.dumps(answer[0], indent=2))
  return answer[0]


# Find last appearance that is an error
# Summarize the error entry
# Find all entries in the DB related to the summary

ans = find_relevant_entries("Instance 2e8c8c4a-823f-4d79-bb72-996b528cbca4?")

# Now getting:
# 
# Original:
#  SELECT content
# FROM log_records_small
# WHERE is_relevant(content, 'Instance 2e8c8c4a-823f-4d79-bb72-996b528cbca4?')
# LIMIT 5
# Converted 1 is_relevant() function calls to answer()
# Processed:
#  SELECT content
# FROM log_records_small
# WHERE answer(content, 'Does the log text mention the instance ID 2e8c8c4a-823f-4d79-bb72-996b528cbca4?') = 'Yes'
#    OR answer(content, 'Is there any reference to actions or events related to Instance 2e8c8c4a-823f-4d79-bb72-996b528cbca4 in the log?') = 'Yes'
#    OR answer(content, 'Does the log show any errors or warnings associated with Instance 2e8c8c4a-823f-4d79-bb72-996b528cbca4?') = 'Yes'
# LIMIT 5
# [
#   [
#     "[instance: 2e8c8c4a-823f-4d79-bb72-996b528cbca4] Instance destroyed successfully."
#   ],
#   [
#     "[instance: 2e8c8c4a-823f-4d79-bb72-996b528cbca4] Instance spawned successfully."
#   ],
#   [
#     "[instance: 2e8c8c4a-823f-4d79-bb72-996b528cbca4] Instance destroyed successfully."
#   ],
#   [
#     "[instance: 2e8c8c4a-823f-4d79-bb72-996b528cbca4] Instance spawned successfully."
#   ]
# ]
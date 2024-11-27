from suql.sql_free_text_support.execute_free_text_sql import suql_execute
import litellm

# litellm.set_verbose = True

# suql = "SELECT * FROM log_normal WHERE answer(content, 'Does the log mention any system crashes or failures?') = 'Yes'"
# suql = "SELECT * FROM log_normal WHERE answer(content, 'Is there an error?') = 'Yes' or answer(content, 'Is the error serious?') = 'Yes' or answer(content, 'Is the error big?') = 'Yes'"
# suql = "SELECT * FROM log_normal WHERE is_relevant(content, 'What is happening?') OR is_relevant(content, 'What was wrong with the system?') OR answer(content, 'Is this line of log interesting?') = 'Yes'"
# suql = "SELECT * FROM log_normal WHERE is_relevant(content, 'What was wrong with the system?')"
# suql = "SELECT * FROM log_records LIMIT 5"
# suql = "SELECT level, content FROM log_records WHERE answer(content, 'Does this line of log contain an HTTP code?') = 'Yes' LIMIT 3"
# suql = "SELECT content FROM log_records WHERE answer(content, 'Is it related to resource managers?') = 'YES' ORDER BY log_date, log_time DESC LIMIT 1;"
# suql = "SELECT content FROM log_records WHERE answer(content, 'Is it related to HTTP GET requests?') = 'YES' LIMIT 10;"
suql = "SELECT DISTINCT component FROM log_records WHERE level IN ('ERROR', 'WARNING', 'CRITICAL') LIMIT 300;"
# suql = "SELECT * FROM log_records WHERE log_date='2017-5-17' AND log_time<='6:25:3.46' ORDER BY log_date ASC, log_time ASC LIMIT 30;"
suql = "SELECT * FROM log_records WHERE component='keystonemiddleware.auth_token' ORDER BY log_date ASC, log_time ASC LIMIT 30;"
# suql = "SELECT summary('sky is blue');"

# suql = "SELECT answer('There is a component in the system: nova.compute.manager', 'Does \"compute manager of the nova system\" refer to the component? Answer with YES or NO');" # YES is answered
# suql = "SELECT answer('Here are the components in the system: nova.compute.manager, compiler.manager', 'Which component does \"manager of the compiler\" refers to? Answer with a component name or NONE if it does not refer to any component');"
suql = """SELECT *
FROM log_records
WHERE (answer(content, 'Is it related to Unable to validate token: Failed to fetch token data from identity server?') = 'YES' OR component = 'keystonemiddleware.auth_token')
  AND level IN ('WARNING', 'ERROR', 'CRITICAL')
  AND (log_date < '2017-05-17'
    OR (log_date = '2017-05-17'
    AND log_time <= '06:25:03.046000'))
ORDER BY log_date DESC
       , log_time DESC
LIMIT 20
"""
# suql = "SELECT * FROM log_records WHERE is_relevant(content, 'What was wrong with the system?') LIMIT 1"

table_w_ids = {"log_records_small": "record_id"}
database = "postgres"
# Try better: llm_model_name="gpt-4o-mini"
answer = suql_execute(suql, table_w_ids, database, llm_model_name='gpt-4o-mini')
for r in answer[0]:
  print(r)
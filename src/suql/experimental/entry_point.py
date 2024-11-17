from suql.sql_free_text_support.execute_free_text_sql import suql_execute
import litellm

# litellm.set_verbose = True

# suql = "SELECT * FROM log_normal WHERE answer(content, 'Does the log mention any system crashes or failures?') = 'Yes'"
# suql = "SELECT * FROM log_normal WHERE answer(content, 'Is there an error?') = 'Yes' or answer(content, 'Is the error serious?') = 'Yes' or answer(content, 'Is the error big?') = 'Yes'"
# suql = "SELECT * FROM log_normal WHERE is_relevant(content, 'What is happening?') OR is_relevant(content, 'What was wrong with the system?') OR answer(content, 'Is this line of log interesting?') = 'Yes'"
# suql = "SELECT * FROM log_normal WHERE is_relevant(content, 'What was wrong with the system?')"
# suql = "SELECT * FROM log_records LIMIT 5"
# suql = "SELECT level, content FROM log_records WHERE answer(content, 'Does this line of log contain an HTTP code?') = 'Yes' LIMIT 3"
suql = "SELECT line_id, level, content FROM log_records WHERE answer(content, 'Does this line of log contain an HTTP code?') = 'Yes' AND level = 'ERROR' LIMIT 3"

table_w_ids = {"log_records": "p_key"}
database = "postgres"
# Try better: llm_model_name="gpt-4o-mini"
answer = suql_execute(suql, table_w_ids, database)
print(answer)

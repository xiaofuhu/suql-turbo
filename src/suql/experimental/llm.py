from suql.free_text_fcns_server import start_free_text_fncs_server

host = "127.0.0.1"
port = 8500
llm_engine = "gpt-4o-mini"
# llm_engine = "gpt-3.5-turbo-0125"
start_free_text_fncs_server(host=host, port=port, engine=llm_engine)

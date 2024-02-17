from autogen import config_list_from_json, UserProxyAgent, AssistantAgent

config_list = config_list_from_json(
    env_or_file='OAI_CONFIG_LIST',
)

llm_config={"config_list": config_list}

# User Proxy Agent
user_proxy_agent = UserProxyAgent(
    name = "User_Proxy_Agent",
    code_execution_config={"work_dir": "coding", "use_docker": False},
)

# Assistant Agent
assistant_agent = AssistantAgent(
    name = "Assistant_Agent",
    llm_config=llm_config
)

user_proxy_agent.initiate_chat(assistant_agent, message="write a python code to add two numbers")
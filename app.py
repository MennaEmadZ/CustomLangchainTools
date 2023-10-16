import os
import faiss
from typing import Type
from pydantic import BaseModel, Field
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain_experimental.autonomous_agents import AutoGPT
from langchain.tools.file_management.write import WriteFileTool
from langchain.tools.file_management.read import ReadFileTool
from langchain.tools.gmail.send_message import GmailSendMessage

from outlook.GetRecentMailsSubjects import RecentMailSubjectForOutlook 

os.environ["OPENAI_API_KEY"] = "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"

tools = [RecentMailSubjectForOutlook(), WriteFileTool(), ReadFileTool(), GmailSendMessage()]
# llm = ChatOpenAI(model="gpt-3.5-turbo-0613", temperature=0)


# agent = initialize_agent(tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
# agent.run("show me the subject of my recent outlook mail and mail id ")

# agent.run("Could you search in my drafts, for the latest email")



# Define your embedding model
# embeddings_model = OpenAIEmbeddings()
# embedding_size = 1536
# index = faiss.IndexFlatL2(embedding_size)
# vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})
# # max_iterations: Optional[int] = 3
llm = ChatOpenAI(model_name="gpt-4", temperature=0)
# llm=ChatOpenAI( model='gpt-3.5-turbo',temperature=0)
# llm = ChatOpenAI(model="gpt-3.5-turbo-0613", temperature=0)

# agent = initialize_agent(
#     # ai_name="Tom",
#     # ai_role="Assistant",
#     tools=tools,
#     verbose = True,
#     llm=llm,
#     agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
#     # memory=vectorstore.as_retriever(),
#     # memory=vectorstore.as_retriever(search_kwargs={"k": 8}),
#     # human_in_the_loop=True, # Set to True if you want to add feedback at each step.
#     # chat_history_memory=FileChatMessageHistory("chat_history.txt"),
# )
agent = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True)
# agent.chain.verbose = True
# agent.run("write a weather report for Cairo today")
# agent.run(["write a weather report for Cairo today, and send the report as text in the mail body with Subject Weather Report From Hamza to mohamed.hamza@smarttechsys.com through gmail"])
# agent.run(["search for the last email from store-news@amazon.eg, and save it in a file with subjhect name of the email sender"])
# agent.run("What is the current price of Facebook stock? How it has performed over past 12 months?, write a report file, and create proper formatted email with the full content of the report and send it to `mohamed.hamza@smarttechsys.com`")
agent.run("show me the subject of my recent outlook mails and write a report of the results ")



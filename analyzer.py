import panel as pn
from langchain_community.llms import OpenAI
from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
import warnings
import io
import os

warnings.filterwarnings("ignore")
pn.extension('plotly', 'tabulator', comms="vscode")
load_dotenv()
print(os.environ["OPENAI_API_KEY"])

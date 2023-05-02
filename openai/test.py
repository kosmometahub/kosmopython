import os
import openai
openai.organization = "org-N0T6j4Xdm7qpHpOFfAyzBssD"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

import re
from io import BytesIO
from typing import Any, Dict, List

import openai
from openai.error import AuthenticationError

openai.api_type = "azure"
openai.api_base = "https://openaipractice.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "4587162fb26b4f1185f0fa46ebec945d"

# @st.cache_data
def get_answer(engine: str, 
               prompt: str, 
               temperature: float, 
               max_tokens: int
              ) -> Dict[str, Any]:


    # Get the answer
    
    if (engine in ["gpt-35-turbo", "code-davinci-002"]) :
        response = openai.Completion.create(engine=engine, prompt=prompt,temperature=temperature, max_tokens=max_tokens, stop=["#",";"])


    return response


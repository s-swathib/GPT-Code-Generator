import re
from io import BytesIO
from typing import Any, Dict, List

import openai
from openai.error import AuthenticationError

# @st.cache_data
def get_answer(engine: str, 
               prompt_text: str, 
               temperature: float, 
               max_tokens: int
              ) -> Dict[str, Any]:


    # Get the answer
    
    if (engine in ["gpt-35-turbo", "code-davinci-002"]) :
        response = openai.Completion.create(engine=engine, prompt=prompt_text, top_p=1, frequency_penalty=0, presence_penalty=0,
                                            stop=["#",";"],temperature=temperature, max_tokens=max_tokens)


    return response


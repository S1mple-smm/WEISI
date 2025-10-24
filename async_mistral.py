import os
from mistralai import Mistral

KEY = "KEjzHJnEaFKktg6234vhcr1keVO0K0TA"
async def main_mistral(content):
    Mistrall = Mistral(api_key=KEY)


    res = await Mistrall.chat.complete_async(
        model = "mistral-small-latest",
        messages=[
            {
                "content": content,
                "role": "user",
            },
        ],
        stream= False
    )
    return res.choices[0].message.content
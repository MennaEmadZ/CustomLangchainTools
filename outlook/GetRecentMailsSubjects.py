
from langchain.tools import BaseTool
import requests


def get_recent_mail_subject_outlook():
    """Method to get recent mail subject and id  in in outlook"""

    token ="EwCYA8l6BAAUAOyDv0l6PcCVu89kmzvqZmkWABkAAUJsl4wfAyrmCygZoC9CZuqfPaDC5TkqvaMRtowX0U7G/4o5C5JiVQAiNwqKSeHO2gAY6kvUNFkIzhsT9VmyHs5EGPvCPL8fY8wrieVo9HHIJBseKqXJ7PFvTTDWQbMl0GZX9GdK65O/njqdKGHuDunOo7sOLCp/10Q0hROkLsegSDsotJJIJbcLl7XwDN3IWlRBFS6baS0f0oC4WXTceQt1kgKpgiabJTWwm6okvwHOpDEOFWED3bCsMqQpQhkJ8wPzhgvjWS+rt12MCDNrg9H3jxp8AtPxV3kbn4aKJ98cDb+KRv+mXucKEt08kEBe65aMq+6OvM2HbMaNOyIlR78DZgAACDuHbu21t8UtaAICT6FZ7IfPrtV2wxxdMWBopgv1QYb2SPUTE178W2fS1p9sn+8cc+Nld4adJNwcVG7YS713IQVgnycVe5iNVbM1aVMk4p5whehTKEV8qSW9rQHXIGL3kIuS4GHQEIXlf0Jsmh4zZ0AGi2rTeSFaaAtGXfbhJ3JQ93bsp8SVaSWYLlyTV5a21D2ukVFHLwfI2SYKraVRgkvdQEV2I4am9bH3mwmlW70QhCQAiaaDV/1dnhT4zA1KyoLkC40ayG0fabwvV/ZjtgpGg8x85IsjvRSKE1vnp+/ewDukPVrKgcUsPyAWjMjh/RWCJ3Y6wQoVGlAIsINHVlDzdJb6bJrCoMUCTQDJp+nTZXq/XZzcN0uPaGA0q+nLvqBPPWyP5i4RUsQCu4fFI3ht9iINZ0fA5jmrRyfZ3Tj+/cx66x0gHishhkRet7K5IcEWnQN17Y/U8Af5+g95G+VOlkOeFha7Gcch3c3pzuAikCW9/2lOqK6ffMoiKNtfBdjUqIFDo+661sD1QesXdqoKxTGlDhBT7PNK4X10SWzrBDZqr8QDXHHYDdjm65UYr75ajZlUp5ct8fN8N0GC/jmXvnLi6bUMbrq7u9Rv9Lpkd86FEUwshm3Ddiy1VhQuRGn8gI6h47QBf1Er8ECFfx39w0eLajHcul1nb3RR/LzEJiZwSTUM/d+vFrs6gYKlLVrZy932q0uZEVu/0/cayt0kWr+mQPxnnOJmn4Cjn9qqvu1xnxU4Fk5a2gXmjlwR27OQ2+LWVP/O6EjlnXcjLbwpysADtkg1bM51EXt+MIUY2zkVo6dBXdrUinKhSPXpYAWKqQI="
    
    graph_data = requests.get(  # Use token to call downstream service
        "https://graph.microsoft.com/v1.0/me/messages?$select=subject",
        headers={'Authorization': 'Bearer ' + token},
        ).json()

    try:
      if graph_data["error"]:
        return "there is a problem accured please try again some other time"  
    except:
      result =[]
      for i in graph_data["value"]:
         result.append(i["subject"])
      return graph_data
    

class RecentMailSubjectForOutlook(BaseTool):
    name = "get_recent_mail_subject_outlook"
    description = """
        Useful when you want to get your recent mail subject and id that is sent to your outlook account
        """
    def _run(self, query: str) -> str:
        response = get_recent_mail_subject_outlook()
        return response


    def _arun(self, query: str):
        raise NotImplementedError("get_recent_mail_subject_outlook does not support async")


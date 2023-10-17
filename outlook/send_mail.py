import requests
import json
from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool


def send_mail_outlook(subject, body, to_recipient):
    """Method to send mail using outlook"""

    token ="EwCgA8l6BAAUAOyDv0l6PcCVu89kmzvqZmkWABkAAbuqYU5c62raYzxigEiZ+tcH5zACfv/iMk2Epjg/JE6M9nblSyl0rac2V+BqgQSNyCLv5MeRI8A79LjWzZ1vedDwZdUM4YxNhlg4kz9tpcBd6qQE7rvoBcJG6ebod/uQmgkCQKDAfWC7cHeS2tYfKhfUq/G5xT00H6TTISsdRKZp6ibfmUT2VjKCsUD9bRKtzRbjcs/JZ4OxOAS8MnI8zh8C94HM3zJkarGvS6OEkjrgQD7B9UHrK9aHvoDfrA4j49IA9bEE7C3BQQHzkt0vpDy6yfnuUduvXLcxoyY63EqWYbGww1673q7x3JzMzgfNmhWFP4rNxbsfzpb/G7PgNq0DZgAACA39ZTVAlp5QcAIujRc1YJoP+eD6FI9DM0bZe7Co2cHVSJB3nEHUN6r6bZ9FQR8KwRPHRep6hAUlEc0S9fAK2Puiw1D60Lgi4w6mWkjdccFBFyinQA4iwCQLSBtAwsLkT8olPeqgnlhnFdAQwXSpVOj0TrTa7bwdHoxIUyEbRBPeITnNnoOqlQWsezrxITH1aaCzxx+xnXwLihZ9iZvoEt20gKqqotjDy3vtnc9ZiCU/nneIznikZ7AWHqRiLFX8lRSO+PDOZIGDYEohxkae2/6gzmUkL/tlmDuYBxXTkwqH5P8XiaVR6v7T490E7A4airMt3l89UtFbRdJB6ksh/21DavolfKo/jGXwmxbEz966EY0VjkWKepMs/NkkxceesaH6YErYobZeLSQJHNgSfmv4RpNc1N74xpv2jv58BkC60ccaCsqA4YkiKUZ/4Q1YQ4bfQmXW3Fa8dgAewE4MXqNABCuVVDTEU48zK9SZp+nfNzeUn6aRM2Go096ZRFPUMnFKv1IJcLx6ody919TCxyldnnoBLVsZEHEd6lohFUqKnaj+lgnZb3mcPBkKx7V89RIBU22GdlE8LCuAIgnnHcsFK2ARDbtAgMKTPTv5wdoIUY9q9ZlMQKuwfu9WgYh/ipCJXA9g6CId/kNKoSoyANxktCj499KE8ESGn6n77Ueau1yVvlqooSwE7oELG14HEfk8ByuKbr+ZI8XkyQKPFO5gV1ioQYuDlvWNS1L5jXm3prHaPTqezmh7l6B9xbK1zZyTr/wxkzdC6OMBxPHErl8Gu6Lkzol6/A84v/nKZAlklXWtMDCCizoDcDfFLXVvZQvIRr4XVpgYMk2rAg=="
    data = {
        "message": {
            "subject": subject,
            "body": {
            "contentType": "Text",
            "content": body
            },
            "toRecipients": [
            {
                "emailAddress": {
                "address": to_recipient
                }
            }
            ],
             "attachments": [
            {
                "@odata.type": "#microsoft.graph.fileAttachment",
                "name": "attachment.txt",
                "contentType": "text/plain",
                "contentBytes": "SGVsbG8gV29ybGQh"
            }
            ]   
            # "ccRecipients": [
            # {
            #     "emailAddress": {
            #     "address": "menna.emad@smarttechsys.com"
            #     }
            # }
            # ]
        }
        }
    
    graph_data = requests.post(  # Use token to call downstream service
        "https://graph.microsoft.com/v1.0/me/sendMail",
        headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token,
            },
        data=json.dumps(data),
        )

    try:
      if graph_data["error"]:
        return "there is a problem accured please try again some other time"  
    except:
        return graph_data

 
class SendOutlookMailInput(BaseModel):
    """Inputs for send_mail_outlook"""

    subject: str = Field(description="the subject of outlook mail")
    body: str = Field(description="the body of outlook mail")
    to_recipient: str = Field(description="the recipient mail to send the mail to ")


  

class SendOutlookMail(BaseTool):
    name = "send_outlook_mail"
    description = """
        Useful when you want to send a mail to someone using your outlook account
        """
    args_schema: Type[BaseModel] = SendOutlookMailInput
    def _run(self, subject: str, body: str, to_recipient: str) -> str:
        response = send_mail_outlook(subject, body, to_recipient)
        return response


    def _arun(self, subject: str, body: str, to_recipient: str):
        raise NotImplementedError("send_mail_outlook does not support async")


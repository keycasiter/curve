import os
import json
import http.client
from dataclasses import asdict
from typing import Dict, List, Optional, Union
import requests
from camel.toolkits import BaseToolkit, FunctionTool


class SerperToolkit(BaseToolkit):
    """A toolkit for performing Google searches and web scraping using Serper.dev API."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the SerperToolkit.

        Args:
            api_key (Optional[str]): The Serper.dev API key. If not provided, will try to get from environment variable SERPER_API_KEY.
        """
        self.api_key = api_key or os.getenv("SERPER_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Serper API key is required. Please provide it or set SERPER_API_KEY environment variable.")

        self.scrape_url = "scrape.serper.dev"

    def scrape(self, url: str) -> Union[str, Dict]:
        """Scrape content from a URL using Serper.dev API.

        Args:
            url (str): The URL to scrape.

        Returns:
            Union[str, Dict]: The scraped content. If the response is JSON, returns the parsed JSON.
            If the response contains a 'text' field, returns that text content.
        """
        conn = http.client.HTTPSConnection(self.scrape_url)
        payload = json.dumps({
            "url": url
        })
        headers = {
            'X-API-KEY': self.api_key,
            'Content-Type': 'application/json'
        }

        conn.request("POST", "/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        response_text = data.decode("utf-8")

        try:
            # 尝试解析 JSON 响应
            response_json = json.loads(response_text)
            # 如果存在 text 字段，返回 text 内容
            if isinstance(response_json, dict) and 'text' in response_json:
                return response_json['text']
            return response_json
        except json.JSONDecodeError:
            # 如果不是 JSON，返回原始文本
            print(f"Serper Tool Warning:Not JSON response: {response_text}")
            return response_text

    def get_tools(self) -> List[FunctionTool]:
        """Get the list of tools provided by this toolkit.

        Returns:
            List[FunctionTool]: List of tools.
        """
        return [
            FunctionTool(
                self.scrape,
            )
        ]


def test_serper_toolkit():
    toolkit = SerperToolkit(api_key="79379409d5d16b33a3433bfabe8272f7e8f28e5e")
    resp = toolkit.scrape("www.gauthmath.com")
    print(f"resp:{resp}")

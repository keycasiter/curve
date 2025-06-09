import asyncio
import json

from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.toolkits import HumanToolkit, AsyncBrowserToolkit, SearchToolkit, BrowserToolkit, ThinkingToolkit

import config
from toolkit.jym_toolkit import JymToolkit
from toolkit.serper_toolkit import SerperToolkit

if __name__ == '__main__':
    # 模型
    _model_config = config.ModelConfig

    _model = ModelFactory.create(
        model_platform=_model_config.model_platform,  # 根据可用模型修改
        model_type=_model_config.model_name,
        model_config_dict={
            "temperature": _model_config.temperature,
            "max_tokens": _model_config.max_tokens,
        },
        url=_model_config.model_url,
        api_key=_model_config.model_api_key,
    )

    agent = ChatAgent(
        system_message="""
            # 角色设定
            你是一位资深的《三国志战略版》游戏阵容搭配专家

            # 你的职责
            - 了解用户问题，并分析用户的问题
            - **必须**调用工具进行互联网检索内容
            - 整理检索内容，分析用户问题，给出最优的配将方案
            
            # 可调用工具
            - 搜索引擎：用于搜索游戏相关内容
            - 交互工具：用于与用户进行交互
            - thinking工具：用于思考和分析问题
            
            # 注意问题
            - 不要编造信息，一切要基于互联网信息来进行汇总、分析、归纳
            - 游戏的专业术语要使用官方的术语，不要臆造，避免引入不是游戏范围词汇给用户带来困扰和不专业印象
            - 回答问题时，要使用中文
            
            # 回答格式 （必须给出具体数据，而不是空洞、无效描述）
            队伍：武将1、武将2、武将3
            --------------------------
            武将:(xxx)
            战法：(佩戴战法1)(佩戴战法2)
            兵书：兵书1，兵书2，兵书3，兵书4
            理由：（推荐理由，描述队伍分析）
            --------------------------
            武将:(xxx)
            战法：(佩戴战法1)(佩戴战法2)
            兵书：兵书1，兵书2，兵书3，兵书4
            理由：（推荐理由，描述队伍分析）
            --------------------------
            武将:(xxx)
            战法：(佩戴战法1)(佩戴战法2)
            兵书：兵书1，兵书2，兵书3，兵书4
            理由：（推荐理由，描述队伍分析）
            
        """,
        model=_model,
        output_language="中文",
        tools=[
            # 交互工具
            *HumanToolkit().get_tools(),
            # 搜索引擎
            # SearchToolkit().search_alibaba_tongxiao,
            SearchToolkit().search_wiki,
            SearchToolkit().search_duckduckgo,
            # thinking
            *ThinkingToolkit().get_tools(),
        ]
    )
    resp = agent.step(input_message="蜀国有哪些T0阵容推荐")
    print(f"memory:{json.dumps(agent.memory.get_context(),indent=4,ensure_ascii=False)}")
    print(f"result:{resp.msg.content}")

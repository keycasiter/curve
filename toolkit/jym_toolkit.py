import http
import json
from typing import Optional, List, Dict, Any
from urllib.parse import urlencode

import requests
from camel.toolkits import FunctionTool, BaseToolkit

import consts.jym
from model.jym import GetSgzGameZoneItemListResp
from util.cookie import load_cookies


class JymToolkit(BaseToolkit):
    def get_sgz_game_zone_item_list(self, min_price: Optional[str] = "0",
                                    max_price: Optional[str] = "9999999",
                                    ) -> List[Dict[str, Any]]:
        r"""查询交易猫网站(m.jiaoyimao.com)上《三国志战略版》游戏账号商品的方法

        Args:
            min_price (int): 商品最低价格
            max_price (int): 商品最高价格

        Returns:
            List[Dict[str, Any]]: A list of dictionaries where each dictionary
            Each dictionary contains the following key and value:
            - 'goods_id': 商品ID
            - 'real_title': 商品标题
            - 'server_name': 所在服务器
            - 'season_server_name': 赛季服
            - 'price': 价格
            - 'detail_url': 商品Url
        """
        # 带参数的 GET 请求
        params = {
            'gameId': consts.jym.game_id,
            'fcid': consts.jym.fc_id,
            'osid': consts.jym.os_id,
            'cid': consts.jym.cid,
            'platformId': consts.jym.platform_id,
            # 排序
            'sort': consts.jym.sort,
            'stdCatId': consts.jym.std_cat_id,
            'jymCatId': consts.jym.jym_cat_id,
            'filterLowQuality': consts.jym.filter_low_quality,
            # 分页，从1开始
            'page': 1,
        }
        # 价格区间 ["5000","12000"]
        # 'priceRange': '',
        if min_price or max_price:
            params['priceRange'] = f'["{min_price}","{max_price}"]'
        # 'extConditions': ,
        # 关键字
        # 'keyword': 'value2',
        # 'enforcePlat': 'value2',

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        # 读取 cookies
        cookies = load_cookies(
            cookie_file="/Users/bytedance/workspace/github.com/keycasiter/curve/project/jym/jym_cookie.json")

        # 发送请求
        response = requests.get(
            url=consts.jym.url_get_sgz_game_zone_item_list,
            params=urlencode(params),
            headers=headers,
            timeout=5,
        )
        if response.status_code == http.HTTPStatus.OK:
            # print(f"get_sgz_game_zone_item_list ==> response:{response.content.decode('utf-8')}")
            json_str = response.content.decode('utf-8')
            dict = json.loads(json_str)
            resp = GetSgzGameZoneItemListResp(**dict)

            data: List[Dict[str, Any]] = []

            for item in resp.result.goods_list:
                data.append({
                    "goods_id": item.goods_id,
                    "real_title": item.real_title,
                    "server_name": item.server_name,
                    "season_server_name": item.season_server_name,
                    "price": item.price,
                    "detail_url": item.detail_url
                })

            return data
        else:
            return ""

    def get_goods_detail_html(self, url: str) -> str:
        r"""查询交易猫网站(m.jiaoyimao.com)商品页面信息

        Args:
            url (str): 商品详情url

        Returns:
            (str): 交易猫商品的HTML页面
        """
        response = requests.get(url, timeout=5)
        if response.status_code == http.HTTPStatus.OK:
            # print(f"get_goods_detail_html ==> response:{response.content}")
            return response.content.decode("utf-8")
        else:
            return ""

    def get_tools(self) -> List[FunctionTool]:
        return [
            FunctionTool(self.get_sgz_game_zone_item_list),
            FunctionTool(self.get_goods_detail_html),
        ]

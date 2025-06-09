from pydantic import BaseModel, Field
from typing import List, Optional

class GetSgzGameZoneItemListRespResultGoodsInfo(BaseModel):
    goods_id: int = Field(..., description="商品ID",alias="goodsId")
    real_title: str = Field(..., description="商品标题",alias="realTitle")
    server_name: str = Field(..., description="当前所在服",alias="serverName")
    season_server_name: str = Field(..., description="赛季服",alias="seasonServerName")
    price: float = Field(..., description="价格",alias="price")
    detail_url: str = Field(..., description="商品Url链接",alias="detailUrl")

    class Config:
        # 允许从 JSON 字段名映射到 Python 属性名
        allow_population_by_field_name = True
        # 字段别名映射
        fields = {
            'goods_id': 'goodsId',
            'real_title': 'realTitle',
            'server_name': 'serverName',
            'season_server_name': 'seasonServerName',
            'detail_url': 'detailUrl'
        }

class GetSgzGameZoneItemListRespResult(BaseModel):
    total_cnt: int = Field(..., description="总数",alias="totalCnt")
    has_next_page: bool = Field(..., description="是否有下一页",alias="hasNextPage")
    goods_list: List[GetSgzGameZoneItemListRespResultGoodsInfo] = Field(..., description="商品列表",alias="goodsList")

    class Config:
        fields = {
            'total_cnt': 'totalCnt',
            'has_next_page': 'hasNextPage',
            'goods_list': 'goodsList'
        }

class GetSgzGameZoneItemListResp(BaseModel):
    success: bool = Field(..., description="是否成功")
    result: GetSgzGameZoneItemListRespResult = Field(..., description="结果")

    class Config:
        fields = {
            'success': 'success',
            'result': 'result'
        }
from camel.types import ModelPlatformType


class ModelConfig:
    # default model
    model_api_key = "0c6052f3-72df-48b3-9c29-2b57e0838919"
    model_url = "https://api-inference.modelscope.cn/v1/"
    # model_name = "Qwen/Qwen3-235B-A22B"
    model_name = "Qwen/Qwen2.5-VL-72B-Instruct"
    # model_name = "Qwen/Qwen2.5-72B-Instruct"
    model_platform = ModelPlatformType.MODELSCOPE
    temperature = 0.7
    max_tokens = 8192

    def __init__(self):
        self.model_api_key = None
        self.model_url = None
        self.model_name = None

class Qwen2_5Coder_32B_InstructConfig(ModelConfig):
    def __init__(self):
        super().__init__()
        self.model_api_key = "0c6052f3-72df-48b3-9c29-2b57e0838919"
        self.model_url = "https://api-inference.modelscope.cn/v1/"
        self.model_name = "Qwen/Qwen2.5-Coder-32B-Instruct"
        self.model_platform = ModelPlatformType.MODELSCOPE
        self.temperature = 0.7
        self.max_tokens = 8192
        # https://modelscope.cn/models/Qwen/Qwen2.5-Coder-32B-Instruct

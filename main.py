import pytest
pytest.main(['-s','-v',
             # '-m','smock',#只运行打标记的测试用例
             # "--reruns","2","--reruns-delay","5",#失败重运行机制
            "--alluredir=reports\\tmp"])
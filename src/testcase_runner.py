import os

from src.common.getpath import *
import pytest
get_path_obj = GetPath()
allure_results =get_path_obj.gent_allure_results_path()

# 执行pytest测试用例框架
# 参数说明:
# - '--alluredir': 指定Allure测试报告的测试结果存储目录
# - allure_results: Allure结果的具体路径变量，由GetPath类生成
# - '--clean-alluredir': 清理已存在的Allure结果目录，确保每次运行都是全新的报告数据
pytest.main(['--alluredir', allure_results, '--clean-alluredir'])

# 使用Allure命令行工具生成HTML格式的测试报告
# 命令参数说明:
# - 'allure generate': Allure报告的生成命令
# - {allure_results}: 输入目录，包含pytest运行后生成的Allure测试结果数据
# - '-o': 指定输出目录的参数标志(output)
# - {get_path_obj.get_reports_path()}: 输出目录路径，HTML报告将生成到此位置
# - '--clean': 清空输出目录中已存在的报告文件，确保生成全新的报告
os.system(f'allure generate {allure_results} -o {get_path_obj.get_reports_path()} --clean')

import os

def get_project_path():
    """获取项目的根路径（绝对）"""
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find("seleniumpythondemo\\")+len("seleniumpythondemo\\")]  # 获取myProject，也就是项目的根路径

    return rootPath
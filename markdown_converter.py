"""
Content Converter Tool for AWS China Region Content Bot
将URL内容转换为Markdown格式的专用工具
"""
import logging
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert

logger = logging.getLogger(__name__)

def convert_url_to_markdown(url: str, css_selector: str = 'article.blog-post') -> str:
    """
    将URL内容转换为Markdown格式
    
    Args:
        url: 要转换的URL地址
        css_selector: CSS选择器，用于选择要转换的HTML部分。如果为None，则转换整个页面
        
    Returns:
        转换后的Markdown内容
    """
    try:
        if css_selector:
            # 直接获取URL内容并使用BeautifulSoup处理
            logger.debug(f"开始获取URL内容: {url}")
            response = requests.get(url)
            response.raise_for_status()
            
            # 解析HTML
            soup = BeautifulSoup(response.content, "html.parser")
            
            # 选择特定部分
            selected_element = soup.select_one(css_selector)
            
            if selected_element:
                # 只转换选定的部分
                logger.debug(f"找到选择器 '{css_selector}' 指定的内容")
                markdown_content = md_convert(str(selected_element))
                return markdown_content
            else:
                logger.warning(f"未找到选择器 '{css_selector}' 指定的内容，将转换整个页面")
        
    except Exception as e:
        logger.error(f"URL转换失败: {str(e)}")

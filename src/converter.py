"""
Content Converter Tool for AWS China Region Content Bot
Tool for converting URL content to Markdown format
"""
import logging
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert

logger = logging.getLogger(__name__)

def convert_url_to_markdown(url: str, css_selector: str = 'article.blog-post') -> str:
    """
    Convert URL content to Markdown format
    
    Args:
        url: URL address to convert
        css_selector: CSS selector to select specific HTML parts. If None, converts the entire page
        
    Returns:
        Converted Markdown content
    """
    try:
        # Get URL content and parse HTML
        logger.debug(f"Starting to fetch URL content: {url}")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        
        # If selector exists, try to select specific part
        if css_selector:
            selected_element = soup.select_one(css_selector)
            if selected_element:
                logger.debug(f"Found content specified by selector '{css_selector}'")
                return md_convert(str(selected_element))
            logger.warning(f"Selector '{css_selector}' not found, converting entire page")
        
        # If no selector or selector not found, convert entire page
        return md_convert(str(soup))
        
    except Exception as e:
        logger.error(f"URL conversion failed: {str(e)}")
        raise
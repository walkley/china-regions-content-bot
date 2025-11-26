// 全局状态
let allReports = [];
let filteredReports = [];
let currentFilter = 'all';

// 配置 marked
marked.setOptions({
    highlight: function(code, lang) {
        if (lang && hljs.getLanguage(lang)) {
            return hljs.highlight(code, { language: lang }).value;
        }
        return hljs.highlightAuto(code).value;
    },
    breaks: true,
    gfm: true
});

// 自定义渲染器处理 Admonitions
const renderer = new marked.Renderer();
const originalParagraph = renderer.paragraph.bind(renderer);

renderer.paragraph = function(text) {
    // 处理 !!! 语法
    const admonitionMatch = text.match(/^!!! (\w+) "(.*?)"\s*([\s\S]*)/);
    if (admonitionMatch) {
        const [, type, title, content] = admonitionMatch;
        return `<div class="admonition ${type.toLowerCase()}">
            <div class="admonition-title">${title}</div>
            <div>${content}</div>
        </div>`;
    }
    return originalParagraph(text);
};

marked.use({ renderer });

// 解析 YAML Front Matter
function parseFrontMatter(markdown) {
    const match = markdown.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
    if (match) {
        const frontMatter = {};
        const lines = match[1].split('\n');
        lines.forEach(line => {
            const [key, ...valueParts] = line.split(':');
            if (key && valueParts.length) {
                frontMatter[key.trim()] = valueParts.join(':').trim();
            }
        });
        return { frontMatter, content: match[2] };
    }
    return { frontMatter: {}, content: markdown };
}

// 加载报告列表
async function loadReports() {
    try {
        const response = await fetch('reports.json');
        const data = await response.json();
        
        allReports = data.reports || [];
        filteredReports = [...allReports];
        
        updateStats(data.statistics);
        renderReportsList();
    } catch (error) {
        console.error('Failed to load reports:', error);
        document.getElementById('reports-list').innerHTML = 
            '<div class="empty">无法加载报告列表</div>';
    }
}

// 更新统计数据
function updateStats(stats) {
    document.getElementById('stat-total').textContent = stats.total || 0;
    document.getElementById('stat-high').textContent = stats.high || 0;
    document.getElementById('stat-moderate').textContent = stats.moderate || 0;
    document.getElementById('stat-low').textContent = stats.low || 0;
    document.getElementById('stat-not_applicable').textContent = stats.not_applicable || 0;
}

// 渲染报告列表
function renderReportsList() {
    const listContainer = document.getElementById('reports-list');
    
    if (filteredReports.length === 0) {
        listContainer.innerHTML = '<div class="empty">没有找到匹配的报告</div>';
        return;
    }
    
    listContainer.innerHTML = filteredReports.map(report => `
        <div class="report-item" data-url="${report.url}">
            <div>
                <div class="title">${report.title}</div>
                <div class="meta">
                    ${report.publish_date} | 
                    ${report.target_region} | 
                    可用服务: ${report.available_services}/${report.available_services + report.unavailable_services}
                </div>
            </div>
            <div class="badge ${report.feasibility.toLowerCase()}">${report.feasibility}</div>
        </div>
    `).join('');
    
    // 添加点击事件
    document.querySelectorAll('.report-item').forEach(item => {
        item.addEventListener('click', () => {
            const url = item.dataset.url;
            loadReportDetail(url);
        });
    });
}

// 加载报告详情
async function loadReportDetail(reportUrl) {
    try {
        const response = await fetch(reportUrl + 'report.md');
        const markdown = await response.text();
        
        const { frontMatter, content } = parseFrontMatter(markdown);
        
        // 渲染 Markdown
        const html = marked.parse(content);
        document.getElementById('markdown-content').innerHTML = html;
        
        // 渲染数学公式
        renderMathInElement(document.getElementById('markdown-content'), {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false},
                {left: '\\[', right: '\\]', display: true},
                {left: '\\(', right: '\\)', display: false}
            ]
        });
        
        // 切换视图
        document.getElementById('list-view').style.display = 'none';
        document.getElementById('detail-view').classList.add('active');
        
        // 滚动到顶部
        window.scrollTo(0, 0);
        
        // 更新 URL hash
        window.location.hash = reportUrl;
    } catch (error) {
        console.error('Failed to load report:', error);
        alert('无法加载报告详情');
    }
}

// 返回列表
function showList() {
    document.getElementById('list-view').style.display = 'block';
    document.getElementById('detail-view').classList.remove('active');
    window.location.hash = '';
    window.scrollTo(0, 0);
}

// 搜索功能
function handleSearch(query) {
    const lowerQuery = query.toLowerCase();
    filteredReports = allReports.filter(report => {
        const matchesSearch = report.title.toLowerCase().includes(lowerQuery);
        const matchesFilter = currentFilter === 'all' || report.feasibility === currentFilter;
        return matchesSearch && matchesFilter;
    });
    renderReportsList();
}

// 筛选功能
function handleFilter(filter) {
    currentFilter = filter;
    const searchQuery = document.getElementById('search-input').value;
    handleSearch(searchQuery);
    
    // 更新按钮状态
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.toggle('active', btn.dataset.filter === filter);
    });
}

// 事件监听
document.addEventListener('DOMContentLoaded', () => {
    // 加载报告
    loadReports();
    
    // 搜索
    document.getElementById('search-input').addEventListener('input', (e) => {
        handleSearch(e.target.value);
    });
    
    // 筛选
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            handleFilter(btn.dataset.filter);
        });
    });
    
    // 返回按钮
    document.getElementById('back-btn').addEventListener('click', (e) => {
        e.preventDefault();
        showList();
    });
    
    // 处理 URL hash
    if (window.location.hash) {
        const reportUrl = window.location.hash.substring(1);
        if (reportUrl) {
            loadReportDetail(reportUrl);
        }
    }
});

// 浏览器后退按钮支持
window.addEventListener('hashchange', () => {
    if (!window.location.hash) {
        showList();
    }
});
